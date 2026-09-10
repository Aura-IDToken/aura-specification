//! BC-02.3 — RI-RS Receiver v1
//!
//! Construction-only receiver for the common BC-02.1 receipt schema.
//! This module MUST NOT execute conformance, B-VAL-014, or §4.5.

use sha2::{Digest, Sha256};
use serde::{Deserialize, Serialize};

pub const SCHEMA_ID: &str = "BC-02.1-COMMON-RECEIPT";
pub const SCHEMA_VERSION: u32 = 1;

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct BoundaryReceipt {
    pub schema_id: String,
    pub schema_version: u32,
    pub fixture: Fixture,
    pub handoff: Handoff,
    pub received: Received,
    pub receiver: Receiver,
    pub adapter: Adapter,
    pub environment: Environment,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct Fixture {
    pub fixture_id: String,
    pub fixture_artifact_identity: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct Handoff {
    pub status: HandoffStatus,
    pub method: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub enum HandoffStatus {
    TRANSFERRED,
    NOT_TRANSFERRED,
    ERROR,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct Received {
    pub octet_length: usize,
    /// Logical octets actually received by RI-RS.
    /// JSON transport encoding, where used, is handled outside this field.
    pub raw_octets: Vec<u8>,
    pub recomputed_sha256: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct Receiver {
    pub receiver_id: String,
    pub implementation_id: String,
    pub language: String,
    pub implementation_version: String,
    pub source_commit: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct Adapter {
    pub adapter_id: String,
    pub adapter_version: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct Environment {
    pub environment_id: String,
    pub platform: String,
    pub runtime: String,
}

/// Construct a receipt from octets actually supplied to the receiver.
/// No expected digest, parsed object, reconstructed JSON, or textual encoding
/// is used as digest input.
pub fn receive(
    fixture_id: String,
    fixture_artifact_identity: String,
    method: String,
    raw_octets: Vec<u8>,
    receiver_id: String,
    implementation_id: String,
    implementation_version: String,
    source_commit: String,
    adapter_id: String,
    adapter_version: String,
    environment_id: String,
    platform: String,
    runtime: String,
) -> BoundaryReceipt {
    let digest = Sha256::digest(&raw_octets);
    let recomputed_sha256 = digest.iter().map(|b| format!("{b:02x}")).collect();
    let octet_length = raw_octets.len();

    BoundaryReceipt {
        schema_id: SCHEMA_ID.to_owned(),
        schema_version: SCHEMA_VERSION,
        fixture: Fixture { fixture_id, fixture_artifact_identity },
        handoff: Handoff { status: HandoffStatus::TRANSFERRED, method },
        received: Received { octet_length, raw_octets, recomputed_sha256 },
        receiver: Receiver {
            receiver_id,
            implementation_id,
            language: "Rust".to_owned(),
            implementation_version,
            source_commit,
        },
        adapter: Adapter { adapter_id, adapter_version },
        environment: Environment { environment_id, platform, runtime },
    }
}

/// Schema-level validation only. This is NOT a conformance result.
pub fn validate_schema(receipt: &BoundaryReceipt) -> Result<(), &'static str> {
    if receipt.schema_id != SCHEMA_ID || receipt.schema_version != SCHEMA_VERSION {
        return Err("R-VAL-001: schema identity/version invalid");
    }
    if receipt.fixture.fixture_id.is_empty() || receipt.fixture.fixture_artifact_identity.is_empty() {
        return Err("R-VAL-002: fixture identity incomplete");
    }
    if receipt.handoff.method.is_empty() {
        return Err("R-VAL-003: handoff method missing");
    }
    if receipt.received.octet_length != receipt.received.raw_octets.len() {
        return Err("R-VAL-004: received length mismatch");
    }
    let digest = Sha256::digest(&receipt.received.raw_octets);
    let expected: String = digest.iter().map(|b| format!("{b:02x}")).collect();
    if expected != receipt.received.recomputed_sha256 {
        return Err("R-VAL-005: receiver-derived hash mismatch");
    }
    if receipt.receiver.receiver_id.is_empty()
        || receipt.receiver.implementation_id.is_empty()
        || receipt.receiver.source_commit.is_empty()
    {
        return Err("R-VAL-006/007: receiver provenance incomplete");
    }
    if receipt.adapter.adapter_id.is_empty() || receipt.adapter.adapter_version.is_empty() {
        return Err("R-VAL-008: adapter identity incomplete");
    }
    if receipt.environment.environment_id.is_empty()
        || receipt.environment.platform.is_empty()
        || receipt.environment.runtime.is_empty()
    {
        return Err("R-VAL-009: environment identity incomplete");
    }
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    fn receipt() -> BoundaryReceipt {
        receive(
            "FIX-DIGEST-P01".into(), "ISSUED-P01-ARTIFACT".into(), "local-octet-transfer".into(),
            vec![0x00, 0x01, 0xFE, 0xFF], "ri-rs-01".into(), "aura-ri-rs".into(),
            "1.0.0".into(), "construction-test".into(), "bc02.3-rs-adapter".into(),
            "1.0.0".into(), "test-env".into(), "test-platform".into(), "rust-test-runtime".into(),
        )
    }

    #[test] fn r_val_001_schema_identity() { let r = receipt(); assert_eq!(r.schema_id, SCHEMA_ID); assert_eq!(r.schema_version, 1); }
    #[test] fn r_val_002_fixture_identity() { let r = receipt(); assert!(!r.fixture.fixture_id.is_empty() && !r.fixture.fixture_artifact_identity.is_empty()); }
    #[test] fn r_val_003_closed_handoff_domain() { assert!(matches!(receipt().handoff.status, HandoffStatus::TRANSFERRED | HandoffStatus::NOT_TRANSFERRED | HandoffStatus::ERROR)); }
    #[test] fn r_val_004_length_explicit() { let r = receipt(); assert_eq!(r.received.octet_length, 4); }
    #[test] fn r_val_005_hash_from_raw_octets() { assert!(validate_schema(&receipt()).is_ok()); }
    #[test] fn r_val_006_receiver_provenance() { assert!(!receipt().receiver.receiver_id.is_empty()); }
    #[test] fn r_val_007_implementation_provenance() { assert!(!receipt().receiver.implementation_id.is_empty() && !receipt().receiver.source_commit.is_empty()); }
    #[test] fn r_val_008_adapter_identity() { assert!(!receipt().adapter.adapter_id.is_empty()); }
    #[test] fn r_val_009_environment_identity() { assert!(!receipt().environment.environment_id.is_empty()); }
    #[test] fn r_val_010_raw_material_not_reconstructed() { let r = receipt(); assert_eq!(r.received.raw_octets, vec![0x00, 0x01, 0xFE, 0xFF]); }
    #[test] fn r_val_011_deterministic_serialization() { let r = receipt(); let a = serde_json::to_vec(&r).unwrap(); let b = serde_json::to_vec(&r).unwrap(); assert_eq!(a, b); }
    #[test] fn r_val_012_no_conformance_authority_field() { let r = serde_json::to_value(receipt()).unwrap(); let object = r.as_object().unwrap(); assert!(!object.contains_key("conformance_result")); assert!(!object.contains_key("pass")); assert!(!object.contains_key("fail")); }
}
