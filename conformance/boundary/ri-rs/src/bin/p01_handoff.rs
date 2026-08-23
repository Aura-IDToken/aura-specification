//! Controlled P-01 Handoff — RI-RS receiver side.
//!
//! Consumes the issued P-01 artifact octets, drives the BC-02.3 receiver, and
//! emits a BC-02.1 receipt plus R-VAL-001..012 schema/receipt validation
//! results.
//!
//! This binary is an adapter and evidence emitter. It does NOT execute
//! B-VAL-014, §4.5, or any conformance procedure, and it does not derive
//! PASS/FAIL for protocol conformance.

use base64::{engine::general_purpose::STANDARD as B64, Engine as _};
use serde_json::{Map, Value};
use sha2::{Digest, Sha256};
use std::env;
use std::fs;
use std::process::ExitCode;

use ri_rs_receiver::{receive, validate_schema, BoundaryReceipt, HandoffStatus, SCHEMA_ID};

/// BC-02.1 §12 deterministic transport serialization.
///
/// Lexicographic member order, compact form, explicit fields, Base64 transport
/// encoding for `raw_octets`. The digest is never computed over this form.
fn transport_json(r: &BoundaryReceipt) -> Value {
    fn obj(pairs: Vec<(&str, Value)>) -> Value {
        let mut m = Map::new();
        for (k, v) in pairs {
            m.insert(k.to_owned(), v);
        }
        Value::Object(m)
    }
    let status = match r.handoff.status {
        HandoffStatus::TRANSFERRED => "TRANSFERRED",
        HandoffStatus::NOT_TRANSFERRED => "NOT_TRANSFERRED",
        HandoffStatus::ERROR => "ERROR",
    };
    obj(vec![
        (
            "adapter",
            obj(vec![
                ("adapter_id", Value::from(r.adapter.adapter_id.clone())),
                ("adapter_version", Value::from(r.adapter.adapter_version.clone())),
            ]),
        ),
        (
            "environment",
            obj(vec![
                ("environment_id", Value::from(r.environment.environment_id.clone())),
                ("platform", Value::from(r.environment.platform.clone())),
                ("runtime", Value::from(r.environment.runtime.clone())),
            ]),
        ),
        (
            "fixture",
            obj(vec![
                (
                    "fixture_artifact_identity",
                    Value::from(r.fixture.fixture_artifact_identity.clone()),
                ),
                ("fixture_id", Value::from(r.fixture.fixture_id.clone())),
            ]),
        ),
        (
            "handoff",
            obj(vec![
                ("method", Value::from(r.handoff.method.clone())),
                ("status", Value::from(status)),
            ]),
        ),
        (
            "received",
            obj(vec![
                ("octet_length", Value::from(r.received.octet_length)),
                ("raw_octets", Value::from(B64.encode(&r.received.raw_octets))),
                ("recomputed_sha256", Value::from(r.received.recomputed_sha256.clone())),
            ]),
        ),
        (
            "receiver",
            obj(vec![
                ("implementation_id", Value::from(r.receiver.implementation_id.clone())),
                (
                    "implementation_version",
                    Value::from(r.receiver.implementation_version.clone()),
                ),
                ("language", Value::from(r.receiver.language.clone())),
                ("receiver_id", Value::from(r.receiver.receiver_id.clone())),
                ("source_commit", Value::from(r.receiver.source_commit.clone())),
            ]),
        ),
        ("schema_id", Value::from(r.schema_id.clone())),
        ("schema_version", Value::from(r.schema_version)),
    ])
}

fn keys_lexicographic(v: &Value) -> bool {
    match v {
        Value::Object(m) => {
            let ks: Vec<&String> = m.keys().collect();
            ks.windows(2).all(|w| w[0].as_bytes() < w[1].as_bytes())
                && m.values().all(keys_lexicographic)
        }
        Value::Array(a) => a.iter().all(keys_lexicographic),
        _ => true,
    }
}

fn no_nulls(v: &Value) -> bool {
    match v {
        Value::Null => false,
        Value::Object(m) => m.values().all(no_nulls),
        Value::Array(a) => a.iter().all(no_nulls),
        _ => true,
    }
}

fn no_insignificant_whitespace(s: &str) -> bool {
    let mut in_str = false;
    let mut esc = false;
    for c in s.chars() {
        if in_str {
            if esc {
                esc = false;
            } else if c == '\\' {
                esc = true;
            } else if c == '"' {
                in_str = false;
            }
        } else if c == '"' {
            in_str = true;
        } else if c.is_whitespace() {
            return false;
        }
    }
    true
}

fn collect(v: &Value, keys: &mut Vec<String>, vals: &mut Vec<String>) {
    match v {
        Value::Object(m) => {
            for (k, sub) in m {
                keys.push(k.clone());
                collect(sub, keys, vals);
            }
        }
        Value::Array(a) => a.iter().for_each(|s| collect(s, keys, vals)),
        Value::String(s) => vals.push(s.clone()),
        _ => {}
    }
}

struct Report {
    failed: bool,
}

impl Report {
    fn assert(&mut self, id: &str, scope: &str, ok: bool, detail: &str) {
        let verdict = if ok { "PASS" } else { "FAIL" };
        if !ok {
            self.failed = true;
        }
        println!("{id}  {verdict}  {scope} — {detail}");
    }
}

fn main() -> ExitCode {
    let args: Vec<String> = env::args().collect();
    if args.len() < 3 {
        eprintln!("usage: p01_handoff <artifact-path> <receipt-out-path>");
        return ExitCode::FAILURE;
    }
    let artifact_path = &args[1];
    let receipt_out = &args[2];

    let ev = |k: &str, d: &str| env::var(k).unwrap_or_else(|_| d.to_owned());

    // Raw octet intake. The file is read as bytes. It is never parsed as JSON,
    // never decoded from hex or Base64, and never re-serialized.
    let raw_octets: Vec<u8> = match fs::read(artifact_path) {
        Ok(b) => b,
        Err(e) => {
            eprintln!("RI-RS EXECUTION BLOCKED: cannot read issued artifact: {e}");
            return ExitCode::FAILURE;
        }
    };
    let intake = raw_octets.clone();

    println!("== RI-RS intake ==");
    println!("artifact_path       : {artifact_path}");
    println!("octets_read         : {}", raw_octets.len());
    println!(
        "octets_hex          : {}",
        raw_octets.iter().map(|b| format!("{b:02x}")).collect::<String>()
    );
    println!();

    let receipt = receive(
        ev("FIXTURE_ID", "FIX-DIGEST-P01"),
        ev("FIXTURE_ARTIFACT_IDENTITY", "FIX-DIGEST-P01.canonical.json"),
        ev("HANDOFF_METHOD", "local-octet-transfer"),
        raw_octets,
        ev("RECEIVER_ID", "RI-RS"),
        ev("IMPLEMENTATION_ID", "aura-ri-rs"),
        ev("IMPLEMENTATION_VERSION", "1.0.0"),
        ev("SOURCE_COMMIT", "UNSET"),
        ev("ADAPTER_ID", "BC-02.3-RS-P01-HANDOFF-ADAPTER"),
        ev("ADAPTER_VERSION", "1.0.0"),
        ev("ENVIRONMENT_ID", "UNSET"),
        ev("PLATFORM", "UNSET"),
        ev("RUNTIME", "UNSET"),
    );

    let schema_validation = validate_schema(&receipt);
    let json = transport_json(&receipt);
    let serialized = serde_json::to_string(&json).expect("transport serialization");
    let serialized_again = serde_json::to_string(&transport_json(&receipt)).expect("re-serialize");

    let mut keys = Vec::new();
    let mut vals = Vec::new();
    collect(&json, &mut keys, &mut vals);

    println!("== R-VAL-001..012 (schema/receipt validation only) ==");
    let mut rep = Report { failed: false };

    rep.assert(
        "R-VAL-001",
        "schema identity/version present",
        receipt.schema_id == SCHEMA_ID && receipt.schema_version == 1,
        &format!("schema_id={} schema_version={}", receipt.schema_id, receipt.schema_version),
    );

    rep.assert(
        "R-VAL-002",
        "fixture identity fields present",
        !receipt.fixture.fixture_id.is_empty()
            && !receipt.fixture.fixture_artifact_identity.is_empty()
            && receipt.fixture.fixture_id == "FIX-DIGEST-P01",
        &format!(
            "fixture_id={} fixture_artifact_identity={}",
            receipt.fixture.fixture_id, receipt.fixture.fixture_artifact_identity
        ),
    );

    let status_str = json["handoff"]["status"].as_str().unwrap_or("");
    let closed_domain = matches!(status_str, "TRANSFERRED" | "NOT_TRANSFERRED" | "ERROR");
    let prohibited = matches!(status_str, "PASS" | "FAIL" | "CONFORMANT" | "NON_CONFORMANT");
    rep.assert(
        "R-VAL-003",
        "handoff state belongs to closed domain",
        closed_domain && !prohibited && status_str == "TRANSFERRED",
        &format!("status={status_str} (domain: TRANSFERRED|NOT_TRANSFERRED|ERROR)"),
    );

    let decoded = B64
        .decode(json["received"]["raw_octets"].as_str().unwrap_or(""))
        .unwrap_or_default();
    rep.assert(
        "R-VAL-004",
        "received length is explicit",
        receipt.received.octet_length == intake.len()
            && receipt.received.octet_length == receipt.received.raw_octets.len()
            && receipt.received.octet_length == decoded.len(),
        &format!(
            "octet_length={} intake={} raw_octets={} b64_decoded={}",
            receipt.received.octet_length,
            intake.len(),
            receipt.received.raw_octets.len(),
            decoded.len()
        ),
    );

    // Independently recompute over the octets read from disk. The receiver was
    // given no digest input of any kind: receive() takes octets only.
    let independent: String = Sha256::digest(&intake).iter().map(|b| format!("{b:02x}")).collect();
    rep.assert(
        "R-VAL-005",
        "recomputed hash is receiver-derived",
        receipt.received.recomputed_sha256 == independent && schema_validation.is_ok(),
        &format!(
            "receiver_derived={} independent_recompute={} validate_schema={}",
            receipt.received.recomputed_sha256,
            independent,
            match &schema_validation {
                Ok(()) => "ok".to_owned(),
                Err(e) => format!("err: {e}"),
            }
        ),
    );

    rep.assert(
        "R-VAL-006",
        "receiver identity preserved",
        !receipt.receiver.receiver_id.is_empty() && receipt.receiver.receiver_id != "UNSET",
        &format!("receiver_id={} language={}", receipt.receiver.receiver_id, receipt.receiver.language),
    );

    rep.assert(
        "R-VAL-007",
        "implementation identity preserved",
        !receipt.receiver.implementation_id.is_empty()
            && !receipt.receiver.implementation_version.is_empty()
            && !receipt.receiver.source_commit.is_empty()
            && receipt.receiver.source_commit != "UNSET"
            && receipt.receiver.implementation_id != receipt.receiver.receiver_id,
        &format!(
            "implementation_id={} implementation_version={} source_commit={}",
            receipt.receiver.implementation_id,
            receipt.receiver.implementation_version,
            receipt.receiver.source_commit
        ),
    );

    rep.assert(
        "R-VAL-008",
        "adapter identity preserved",
        !receipt.adapter.adapter_id.is_empty()
            && !receipt.adapter.adapter_version.is_empty()
            && receipt.adapter.adapter_id != receipt.receiver.implementation_id,
        &format!(
            "adapter_id={} adapter_version={}",
            receipt.adapter.adapter_id, receipt.adapter.adapter_version
        ),
    );

    rep.assert(
        "R-VAL-009",
        "environment identity preserved",
        !receipt.environment.environment_id.is_empty()
            && receipt.environment.environment_id != "UNSET"
            && receipt.environment.platform != "UNSET"
            && receipt.environment.runtime != "UNSET",
        &format!(
            "environment_id={} platform={} runtime={}",
            receipt.environment.environment_id,
            receipt.environment.platform,
            receipt.environment.runtime
        ),
    );

    rep.assert(
        "R-VAL-010",
        "raw material is not silently reconstructed",
        receipt.received.raw_octets == intake && decoded == intake,
        &format!(
            "receipt octets == octets read from issued artifact ({} octets); Base64 transport decodes to the same octets",
            intake.len()
        ),
    );

    let lex = keys_lexicographic(&json);
    let compact = no_insignificant_whitespace(&serialized);
    let nulls_ok = no_nulls(&json);
    rep.assert(
        "R-VAL-011",
        "deterministic serialization possible",
        serialized == serialized_again && lex && compact && nulls_ok,
        &format!(
            "stable_repeat={} lexicographic_keys={} compact={} null_free={} bytes={}",
            serialized == serialized_again,
            lex,
            compact,
            nulls_ok,
            serialized.len()
        ),
    );

    let forbidden_keys = [
        "conformance_result",
        "conformance",
        "acceptance_state",
        "expected_acceptance",
        "digest_output_state",
        "expected_digest_output",
        "verdict",
        "outcome",
        "pass",
        "fail",
        "result",
    ];
    let forbidden_values = ["PASS", "FAIL", "CONFORMANT", "NON_CONFORMANT"];
    let bad_key = keys.iter().find(|k| forbidden_keys.contains(&k.to_lowercase().as_str()));
    let bad_val = vals
        .iter()
        .find(|v| forbidden_values.contains(&v.to_uppercase().as_str()));
    let top_level: Vec<String> = json.as_object().unwrap().keys().cloned().collect();
    let expected_top = [
        "adapter",
        "environment",
        "fixture",
        "handoff",
        "received",
        "receiver",
        "schema_id",
        "schema_version",
    ];
    rep.assert(
        "R-VAL-012",
        "no conformance-result authority",
        bad_key.is_none() && bad_val.is_none() && top_level == expected_top,
        &format!(
            "forbidden_key={:?} forbidden_value={:?} field_set_exact={}",
            bad_key,
            bad_val,
            top_level == expected_top
        ),
    );

    println!();
    if let Err(e) = fs::write(receipt_out, format!("{serialized}\n")) {
        eprintln!("cannot write receipt: {e}");
        return ExitCode::FAILURE;
    }
    println!("== BC-02.1 receipt (deterministic transport form) ==");
    println!("{serialized}");
    println!();
    println!("receipt written to: {receipt_out}");
    println!();
    println!("B-VAL-014 NOT EXECUTED");
    println!("§4.5 NO RESULT");
    println!("CONFORMANCE NOT DETERMINED");

    if rep.failed {
        ExitCode::FAILURE
    } else {
        ExitCode::SUCCESS
    }
}
