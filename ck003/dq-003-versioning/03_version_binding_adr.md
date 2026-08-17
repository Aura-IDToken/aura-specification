# ADR — DQ-003 Version Binding and Semantics

**Status:** PROPOSED — decision candidate, not yet normative/frozen  
**Date:** 2026-08-17  
**Scope:** Aura protocol versioning across Specification, Core and Guard

## 1. Decision context

The DQ-003 evidence snapshot establishes several distinct version namespaces:

- Specification repository release: `0.1.0`
- Versioning policy: `POL-VER-001 1.0-DRAFT`
- APS documents: e.g. `APS-200 1.0-DRAFT`, `APS-300 1.0-DRAFT`
- Core instrument lineage: `v3.3`
- Guard package/implementation: `1.3.0`
- Existing certificate `schema_version`: `1.0.0`
- Protocol `protocol_version`: no authoritative runtime value currently established

The snapshot explicitly does not establish equivalence between these namespaces. The purpose of this ADR is to define the intended binding before production remediation.

## 2. Decision

Aura SHALL treat `protocol_version` and `schema_version` as separate protocol namespaces.

### 2.1 `protocol_version`

`protocol_version` identifies the version of the **normative Aura protocol contract** governing the semantic interpretation of a canonical object and its evidence.

It SHALL NOT be inferred from:

- repository release version;
- Core instrument lineage (`v3.3`);
- Guard package version (`1.3.0`);
- an individual APS document version.

A protocol-version change is a protocol governance event and MUST be explicitly declared by the specification authority.

### 2.2 `schema_version`

`schema_version` identifies the version of the concrete canonical object schema/representation used to encode the object.

A schema change MAY occur without a protocol semantic change when compatibility is preserved. Conversely, a protocol change MAY require a schema change, but the two version numbers SHALL NOT be assumed to move in lockstep.

### 2.3 Implementation versions

Core and Guard implementation/package versions remain implementation metadata. They SHALL NOT be used as protocol identifiers.

Thus:

```text
Core v3.3        != protocol_version
Guard 1.3.0      != protocol_version
APS-200 1.0      != protocol_version
APS-300 1.0      != protocol_version
```

## 3. Binding rules

Every canonical object that falls under the common object contract SHALL carry both:

```text
protocol_version
schema_version
```

Their semantics SHALL be independently documented and validated.

The authoritative value of `protocol_version` SHALL come from the frozen protocol specification/governance record, not from runtime package metadata.

The authoritative value of `schema_version` SHALL come from the schema definition governing the object's representation.

## 4. Canonicalization and digest-domain consequence

Version fields are protocol data and therefore MUST be resolved before the canonical-byte boundary is entered.

The DQ-002 hash-domain decision establishes the cryptographic model:

```text
canonical object
      |
      v
canonical bytes
      |
      +--> leaf = SHA-256(0x00 || bytes)
      |
      +--> node = SHA-256(0x01 || left[32] || right[32])
```

This ADR does **not** independently redefine the DQ-002 hash algorithm.

Before implementation, the canonical serialization specification MUST explicitly state whether `protocol_version` and `schema_version` are mandatory members of the canonical object and therefore part of the hashed canonical byte sequence. The current evidence establishes that both fields are required by APS-200/APS-300, but this ADR does not silently invent serialization details that are not yet normatively frozen.

## 5. Compatibility rules

A change to `schema_version` SHALL indicate a change in schema/representation semantics according to the versioning policy.

A change to `protocol_version` SHALL indicate a change in the normative protocol contract.

Neither field may be silently rewritten by an implementation based on its own package version.

An implementation claiming conformance MUST reject, or explicitly classify as unsupported, a protocol version it does not implement. Silent downgrade or reinterpretation is prohibited.

## 6. Cross-repository contract

The three repositories have different responsibilities:

| Repository | Version authority |
|---|---|
| `aura-specification` | normative `protocol_version` and schema definitions |
| `aura-poc-a-core-v3.3` | implementation of the protocol contract; implementation/instrument lineage remains separate |
| `aura-guard-v1.3` | implementation/package version remains separate; consumes protocol/schema contract |

The specification repository is the source of truth for protocol semantics. Core and Guard MUST NOT independently mint competing protocol-version meanings.

## 7. Required implementation consequences

This ADR is a design decision candidate. No production implementation is changed by this document.

Before closure, the following artifacts are required:

1. normative declaration of the initial `protocol_version` value;
2. explicit canonical serialization rule for both version fields;
3. Core conformance fixture covering both fields;
4. Guard conformance fixture covering both fields;
5. CI gate proving identical interpretation across implementations;
6. update to the versioning policy if required.

## 8. Non-decisions

This ADR does NOT:

- select `0.1.0`, `1.0.0`, `3.3`, or `1.3.0` as the protocol version;
- change Core or Guard production code;
- freeze APS-200 or APS-300;
- redefine the DQ-002 Merkle/hash algorithm;
- authorize a protocol-version migration.

## 9. Rationale

The separation prevents a common class of interoperability failures in which repository, package, instrument, schema, and protocol versions are treated as interchangeable identifiers.

For Aura, the protocol version must describe the contract that two independent implementations are expected to interpret identically. Implementation lineage and packaging are operational metadata and therefore belong to a different namespace.

## 10. DQ-003 status

**03_version_binding_adr: PROPOSED / OPEN.**

The ADR is intentionally not marked ACCEPTED because the initial authoritative `protocol_version` value and final canonical serialization binding still require explicit normative closure.
