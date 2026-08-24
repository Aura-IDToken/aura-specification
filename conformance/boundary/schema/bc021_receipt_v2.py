"""BC-02.1 — Common Receipt Schema, reference implementation of schema_version 2.

Scope: BC-02.1 PRE-01 minimal schema correction. This module is a **schema-layer
construction artifact**. It is not RI-PY, not RI-RS, and not a receiver
production artifact; nothing here is imported by, or changes the semantics of,
either reference receiver.

Authority: NONE. This module cannot emit PASS, FAIL, CONFORMANT,
NON_CONFORMANT, a CONF-003 section 4.5 result, or a B-VAL-014 result. It does
not execute conformance, and successful schema validation is not conformance.

What v2 corrects
----------------
BC-02.1 v1 carried a single digest field, ``received.recomputed_sha256``. BC-02
section 14 states B-VAL-014 over two operands, ``receipt_digest`` and
``input_segment_sha256``. Under v1 those two operands could only be satisfied by
reading one field twice, which would make their equality a tautology rather than
an observation.

v2 records the two operands as separate fields, each derived from its own source
material by its own calculation path, each carrying its own provenance:

    PATH B   received transfer unit
                 -> received.raw_octets            (the actual receiver buffer)
                 -> SHA-256
                 -> digest_operands.receipt_digest

    PATH A   received transfer unit
                 -> decode(input_segment.raw_input_encoding)
                 -> input_segment.octets           (the input segment)
                 -> SHA-256
                 -> digest_operands.input_segment_sha256

The two paths never exchange a computed value. Their equality, where it later
holds, is an observed result and never an assignment.

Per AGENTS.md rule 4, no validation outcome in this module relies on ``assert``.
"""

from __future__ import annotations

import base64
import binascii
import hashlib
import inspect
import json
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Tuple, Union

SCHEMA_ID = "BC-02.1-COMMON-RECEIPT"
SCHEMA_VERSION = 2

LANGUAGE = "Python"

#: BC-02.1 v1 section 6. Base64 is the JSON transport encoding of an octet
#: sequence. It is a representation of raw material, never a digest input.
RAW_OCTET_TRANSPORT_ENCODING = "base64"

#: Explicit, closed references naming where each operand's raw source material
#: is recorded in the receipt. An operand names its material; it never carries a
#: second copy of it.
RECEIVED_BUFFER_REF = "received.raw_octets"
INPUT_SEGMENT_REF = "input_segment.octets"

RECEIPT_DIGEST_PATH = (
    "received transfer unit -> received.raw_octets -> SHA-256 "
    "-> digest_operands.receipt_digest.value"
)
INPUT_SEGMENT_SHA256_PATH = (
    "received transfer unit -> decode(input_segment.raw_input_encoding) "
    "-> input_segment.octets -> SHA-256 "
    "-> digest_operands.input_segment_sha256.value"
)

#: BC-02.1 v1 section 14 / R-INV-04. Keys that would carry result authority.
FORBIDDEN_RECEIPT_KEYS = frozenset(
    {
        "conformance_result",
        "conformance",
        "acceptance_state",
        "expected_acceptance",
        "digest_output_state",
        "expected_digest_output",
        "result",
        "verdict",
        "outcome",
        "pass",
        "fail",
    }
)

#: BC-02.1 v1 section 5. Values prohibited anywhere in the receipt.
FORBIDDEN_RECEIPT_VALUES = frozenset({"PASS", "FAIL", "CONFORMANT", "NON_CONFORMANT"})

_HEX_DIGITS = frozenset("0123456789abcdef")


class ReceiptConstructionError(Exception):
    """Raised when receipt construction is impossible. Not a conformance result."""


class HandoffStatus(Enum):
    """BC-02.1 v1 section 5 closed engineering domain. Handoff state only."""

    TRANSFERRED = "TRANSFERRED"
    NOT_TRANSFERRED = "NOT_TRANSFERRED"
    ERROR = "ERROR"


class RawInputEncoding(Enum):
    """Encoding of the input segment inside the received transfer unit.

    Domain taken verbatim from the BC-02 section 14 B-VAL-014 formal condition,
    ``raw_input_encoding in {identity, base64, base16}``. Recording the encoding
    does not decide B-VAL-014 and does not change its meaning.
    """

    IDENTITY = "identity"
    BASE64 = "base64"
    BASE16 = "base16"


class DigestSource(Enum):
    """How a digest operand's value came to exist.

    ``COPIED_FROM_OTHER_OPERAND`` is deliberately representable. A source field
    that can only ever hold one value records nothing; naming the prohibited
    case is what makes its absence checkable. This reference implementation has
    no code path that produces it.
    """

    RECEIVER_RECOMPUTED = "RECEIVER_RECOMPUTED"
    EXTERNALLY_SUPPLIED = "EXTERNALLY_SUPPLIED"
    COPIED_FROM_OTHER_OPERAND = "COPIED_FROM_OTHER_OPERAND"


class SourceMaterial(Enum):
    """Closed domain naming which raw material an operand was derived from."""

    RECEIVED_BUFFER = "RECEIVED_BUFFER"
    INPUT_SEGMENT = "INPUT_SEGMENT"


class UnresolvedState(Enum):
    """BC-02.1 v1 section 10 states, made representable rather than collapsed.

    v1 required ``missing value != UNKNOWN != ABSENT`` but provided no way to
    write any of them down, while prohibiting ``null``. That is the schema
    deficiency this type records. It is an engineering representation of an
    unbound value; it introduces no protocol state and no normative requirement.
    """

    UNKNOWN = "UNKNOWN"
    ABSENT = "ABSENT"
    ERROR = "ERROR"
    REJECT = "REJECT"


@dataclass(frozen=True)
class UnresolvedValue:
    """An explicitly unbound field value. Never ``null``, never an empty string.

    In v2 the only field whose value may be an ``UnresolvedValue`` is
    ``fixture.issuance_id``.
    """

    state: UnresolvedState
    detail: str


#: A field that is either bound to a string or explicitly unresolved.
MaybeUnresolved = Union[str, UnresolvedValue]


@dataclass(frozen=True)
class ComputedBy:
    """Per-operand provenance chain, BC-02.1 PRE-01 section 7.

    Recorded on the operand so that ``operand -> receiver -> implementation ->
    adapter -> source commit -> environment`` is resolvable from the operand
    itself, not only from the receipt as a whole.
    """

    receiver_id: str
    implementation_id: str
    adapter_id: str
    source_commit: str
    environment_id: str


@dataclass(frozen=True)
class DigestOperand:
    """One B-VAL-014 digest operand together with its source and provenance."""

    value: str
    source: DigestSource
    source_material: SourceMaterial
    source_material_ref: str
    source_material_octet_length: int
    calculation_path: str
    computed_by: ComputedBy


@dataclass(frozen=True)
class DigestOperands:
    """The two operands, held as separate fields of separate provenance."""

    receipt_digest: DigestOperand
    input_segment_sha256: DigestOperand


@dataclass(frozen=True)
class FixtureIdentity:
    """BC-02.1 v2 section 4.

    ``fixture_artifact_identity`` is SHA-256 of the exact issued artifact octets.
    ``fixture_artifact_name`` is a label and is never an identity.
    """

    fixture_id: str
    fixture_artifact_identity: str
    fixture_artifact_name: str
    issuance_id: MaybeUnresolved


@dataclass(frozen=True)
class Handoff:
    status: HandoffStatus
    method: str


@dataclass(frozen=True)
class ReceivedMaterial:
    """PATH B raw material: the octets the receiver actually holds."""

    octet_length: int
    raw_octets: bytes


@dataclass(frozen=True)
class InputSegment:
    """PATH A raw material: the input segment extracted from the transfer unit."""

    octet_length: int
    octets: bytes
    raw_input_encoding: RawInputEncoding


@dataclass(frozen=True)
class ReceiverIdentity:
    receiver_id: str
    implementation_id: str
    implementation_version: str
    source_commit: str
    language: str = LANGUAGE


@dataclass(frozen=True)
class AdapterIdentity:
    adapter_id: str
    adapter_version: str


@dataclass(frozen=True)
class EnvironmentIdentity:
    environment_id: str
    platform: str
    runtime: str


@dataclass(frozen=True)
class BoundaryReceipt:
    """BC-02.1 v2 logical model. Evidence input, never a conformance result."""

    fixture: FixtureIdentity
    handoff: Handoff
    received: ReceivedMaterial
    input_segment: InputSegment
    digest_operands: DigestOperands
    receiver: ReceiverIdentity
    adapter: AdapterIdentity
    environment: EnvironmentIdentity
    schema_id: str = SCHEMA_ID
    schema_version: int = SCHEMA_VERSION


def _require_octets(material: Any, label: str) -> bytes:
    """Reject text where octets are required.

    A ``str`` argument is how a hexadecimal or Base64 rendering would silently
    become digest input. BC-02.1 PRE-01 section 10 prohibits that substitution.
    """
    if isinstance(material, str):
        raise ReceiptConstructionError(
            "{0} must be octets, not text; a textual rendering (hex, Base64) is "
            "not a valid digest input".format(label)
        )
    if not isinstance(material, (bytes, bytearray, memoryview)):
        raise ReceiptConstructionError("{0} must be an octet sequence".format(label))
    return bytes(material)


def _independent_copy(material: bytes) -> bytes:
    """Return an octet-equal copy that is a distinct object from ``material``.

    ``bytes(b)`` may return the same immutable object. Routing through a
    ``bytearray`` forces a distinct object, so that "the two paths hold two
    buffers" is checkable at object level and not merely asserted in prose.
    """
    return bytes(bytearray(material))


def _sha256_hex(material: bytes) -> str:
    """The single digest primitive. Distinct inputs, never a shared value."""
    return hashlib.sha256(material).hexdigest()


def _is_sha256_hex(value: Any) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(character in _HEX_DIGITS for character in value)
    )


def extract_input_segment(
    transfer_unit: bytes, raw_input_encoding: RawInputEncoding
) -> bytes:
    """Controlled decode of the received transfer unit into the input segment.

    This is PATH A's only source of material. It never reads, receives, or
    returns a digest, and it has no access to PATH B's buffer or value.
    """
    material = _require_octets(transfer_unit, "transfer unit")
    if not isinstance(raw_input_encoding, RawInputEncoding):
        raise ReceiptConstructionError(
            "raw_input_encoding must belong to the closed domain {0}".format(
                sorted(member.value for member in RawInputEncoding)
            )
        )
    if raw_input_encoding is RawInputEncoding.IDENTITY:
        return _independent_copy(material)
    try:
        if raw_input_encoding is RawInputEncoding.BASE64:
            return _independent_copy(base64.b64decode(material, validate=True))
        return _independent_copy(base64.b16decode(material, casefold=True))
    except (binascii.Error, ValueError) as exc:
        raise ReceiptConstructionError(
            "input-segment extraction failed under encoding {0}: {1}".format(
                raw_input_encoding.value, exc
            )
        )


class BoundaryReceiver:
    """Constructs BC-02.1 v2 receipts from a transfer unit handed to it.

    Provenance is bound once, at construction, so one receipt cannot silently
    mix identities. The per-handoff surface is fixture identity, transfer
    method, transfer unit, and the declared raw-input encoding.

    Both digest operands are derived internally by two separate observers.
    ``receive()`` exposes no digest parameter, so a caller cannot supply either
    operand, and neither observer can see the other's material or value.
    """

    def __init__(
        self,
        receiver: ReceiverIdentity,
        adapter: AdapterIdentity,
        environment: EnvironmentIdentity,
    ) -> None:
        for label, identity in (
            ("receiver", receiver),
            ("adapter", adapter),
            ("environment", environment),
        ):
            if identity is None:
                raise ReceiptConstructionError("{0} identity is required".format(label))
        self._receiver = receiver
        self._adapter = adapter
        self._environment = environment

    @property
    def receiver_identity(self) -> ReceiverIdentity:
        return self._receiver

    @property
    def adapter_identity(self) -> AdapterIdentity:
        return self._adapter

    @property
    def environment_identity(self) -> EnvironmentIdentity:
        return self._environment

    def _computed_by(self) -> ComputedBy:
        return ComputedBy(
            receiver_id=self._receiver.receiver_id,
            implementation_id=self._receiver.implementation_id,
            adapter_id=self._adapter.adapter_id,
            source_commit=self._receiver.source_commit,
            environment_id=self._environment.environment_id,
        )

    def _observe_received_buffer(self, received_buffer: bytes) -> DigestOperand:
        """PATH B. Sees the receiver buffer only. Never sees PATH A."""
        material = _require_octets(received_buffer, "received buffer")
        return DigestOperand(
            value=_sha256_hex(material),
            source=DigestSource.RECEIVER_RECOMPUTED,
            source_material=SourceMaterial.RECEIVED_BUFFER,
            source_material_ref=RECEIVED_BUFFER_REF,
            source_material_octet_length=len(material),
            calculation_path=RECEIPT_DIGEST_PATH,
            computed_by=self._computed_by(),
        )

    def _observe_input_segment(self, input_segment: bytes) -> DigestOperand:
        """PATH A. Sees the input segment only. Never sees PATH B."""
        material = _require_octets(input_segment, "input segment")
        return DigestOperand(
            value=_sha256_hex(material),
            source=DigestSource.RECEIVER_RECOMPUTED,
            source_material=SourceMaterial.INPUT_SEGMENT,
            source_material_ref=INPUT_SEGMENT_REF,
            source_material_octet_length=len(material),
            calculation_path=INPUT_SEGMENT_SHA256_PATH,
            computed_by=self._computed_by(),
        )

    def receive(
        self,
        fixture: FixtureIdentity,
        method: str,
        transfer_unit: bytes,
        raw_input_encoding: RawInputEncoding = RawInputEncoding.IDENTITY,
        status: HandoffStatus = HandoffStatus.TRANSFERRED,
    ) -> BoundaryReceipt:
        """Observe a handoff of ``transfer_unit`` and construct the v2 receipt."""
        if not isinstance(fixture, FixtureIdentity):
            raise ReceiptConstructionError("fixture identity is required")
        if not isinstance(status, HandoffStatus):
            raise ReceiptConstructionError(
                "handoff status must belong to the closed BC-02.1 domain"
            )
        if not isinstance(method, str) or not method:
            raise ReceiptConstructionError("handoff method is required")
        _validate_fixture(fixture)

        material = _require_octets(transfer_unit, "transfer unit")

        # PATH B material, then PATH A material. Two buffers, two objects.
        received_buffer = _independent_copy(material)
        input_segment = extract_input_segment(material, raw_input_encoding)
        if received_buffer is input_segment:
            raise ReceiptConstructionError(
                "the two operand source buffers must be distinct objects"
            )

        # Two observers, two call sites, no value passed between them.
        receipt_digest = self._observe_received_buffer(received_buffer)
        input_segment_sha256 = self._observe_input_segment(input_segment)

        receipt = BoundaryReceipt(
            fixture=fixture,
            handoff=Handoff(status=status, method=method),
            received=ReceivedMaterial(
                octet_length=len(received_buffer),
                raw_octets=received_buffer,
            ),
            input_segment=InputSegment(
                octet_length=len(input_segment),
                octets=input_segment,
                raw_input_encoding=raw_input_encoding,
            ),
            digest_operands=DigestOperands(
                receipt_digest=receipt_digest,
                input_segment_sha256=input_segment_sha256,
            ),
            receiver=self._receiver,
            adapter=self._adapter,
            environment=self._environment,
        )
        _reject_result_authority(receipt)
        return receipt

    @classmethod
    def digest_input_is_caller_supplied(cls) -> bool:
        """True if any ``receive()`` parameter could carry a digest. Always False."""
        return _signature_admits_digest(cls.receive)

    @classmethod
    def operand_observers_are_independent(cls) -> bool:
        """True when neither operand observer can receive the other's value.

        Checks that the two observers are distinct callables and that neither
        signature admits a digest, an expected value, or the other operand.
        """
        path_b = cls._observe_received_buffer
        path_a = cls._observe_input_segment
        if path_a is path_b:
            return False
        if _signature_admits_digest(path_a) or _signature_admits_digest(path_b):
            return False
        parameters_a = set(inspect.signature(path_a).parameters)
        parameters_b = set(inspect.signature(path_b).parameters)
        return parameters_a - {"self"} != parameters_b - {"self"}


def _signature_admits_digest(function: Any) -> bool:
    suspect = ("sha", "digest", "hash", "expected", "checksum", "operand")
    for name in inspect.signature(function).parameters:
        lowered = name.lower()
        if any(token in lowered for token in suspect):
            return True
    return False


def _validate_fixture(fixture: FixtureIdentity) -> None:
    """Fixture identity rules, BC-02.1 v2 section 4."""
    if not fixture.fixture_id:
        raise ReceiptConstructionError("fixture_id is required")
    if not _is_sha256_hex(fixture.fixture_artifact_identity):
        raise ReceiptConstructionError(
            "fixture_artifact_identity must be SHA-256 of the exact issued "
            "artifact octets, as 64 lowercase hexadecimal digits; a file name "
            "is a fixture_artifact_name, not an identity"
        )
    if not isinstance(fixture.fixture_artifact_name, str) or not fixture.fixture_artifact_name:
        raise ReceiptConstructionError("fixture_artifact_name is required")
    issuance_id = fixture.issuance_id
    if isinstance(issuance_id, UnresolvedValue):
        if not isinstance(issuance_id.state, UnresolvedState):
            raise ReceiptConstructionError(
                "unresolved state must belong to the closed domain {0}".format(
                    sorted(member.value for member in UnresolvedState)
                )
            )
        if not issuance_id.detail:
            raise ReceiptConstructionError(
                "an unresolved value must record why it is unresolved"
            )
        return
    if not isinstance(issuance_id, str) or not issuance_id:
        raise ReceiptConstructionError(
            "issuance_id must be a non-empty string or an explicit "
            "UnresolvedValue; null and the empty string are prohibited"
        )


def _reject_result_authority(receipt: BoundaryReceipt) -> None:
    """Refuse to construct a receipt carrying a conformance classification."""
    _, values = walk(transport_mapping(receipt))
    offending = sorted(
        {
            value
            for value in values
            if isinstance(value, str) and value.upper() in FORBIDDEN_RECEIPT_VALUES
        }
    )
    if offending:
        raise ReceiptConstructionError(
            "a receipt cannot carry a conformance classification: {0}".format(offending)
        )


def transport_mapping(receipt: BoundaryReceipt) -> Dict[str, Any]:
    """BC-02.1 v2 section 12 transport mapping.

    Every field explicit, no implicit defaults, no ``null``, raw material
    carried as the declared Base64 transport encoding.
    """
    if not isinstance(receipt.handoff.status, HandoffStatus):
        raise ReceiptConstructionError(
            "handoff status must belong to the closed BC-02.1 domain to be serialized"
        )
    raw_octets = _require_octets(receipt.received.raw_octets, "received.raw_octets")
    segment_octets = _require_octets(receipt.input_segment.octets, "input_segment.octets")
    return {
        "schema_id": receipt.schema_id,
        "schema_version": receipt.schema_version,
        "adapter": {
            "adapter_id": receipt.adapter.adapter_id,
            "adapter_version": receipt.adapter.adapter_version,
        },
        "digest_operands": {
            "input_segment_sha256": _operand_mapping(
                receipt.digest_operands.input_segment_sha256
            ),
            "receipt_digest": _operand_mapping(receipt.digest_operands.receipt_digest),
        },
        "environment": {
            "environment_id": receipt.environment.environment_id,
            "platform": receipt.environment.platform,
            "runtime": receipt.environment.runtime,
        },
        "fixture": {
            "fixture_artifact_identity": receipt.fixture.fixture_artifact_identity,
            "fixture_artifact_name": receipt.fixture.fixture_artifact_name,
            "fixture_id": receipt.fixture.fixture_id,
            "issuance_id": _maybe_unresolved_mapping(receipt.fixture.issuance_id),
        },
        "handoff": {
            "method": receipt.handoff.method,
            "status": receipt.handoff.status.value,
        },
        "input_segment": {
            "octet_length": receipt.input_segment.octet_length,
            "octets": base64.b64encode(segment_octets).decode("ascii"),
            "raw_input_encoding": receipt.input_segment.raw_input_encoding.value,
        },
        "received": {
            "octet_length": receipt.received.octet_length,
            "raw_octets": base64.b64encode(raw_octets).decode("ascii"),
        },
        "receiver": {
            "implementation_id": receipt.receiver.implementation_id,
            "implementation_version": receipt.receiver.implementation_version,
            "language": receipt.receiver.language,
            "receiver_id": receipt.receiver.receiver_id,
            "source_commit": receipt.receiver.source_commit,
        },
    }


def _operand_mapping(operand: DigestOperand) -> Dict[str, Any]:
    if not isinstance(operand.source, DigestSource):
        raise ReceiptConstructionError(
            "digest source must belong to the closed domain {0}".format(
                sorted(member.value for member in DigestSource)
            )
        )
    if not isinstance(operand.source_material, SourceMaterial):
        raise ReceiptConstructionError(
            "source material must belong to the closed domain {0}".format(
                sorted(member.value for member in SourceMaterial)
            )
        )
    return {
        "calculation_path": operand.calculation_path,
        "computed_by": {
            "adapter_id": operand.computed_by.adapter_id,
            "environment_id": operand.computed_by.environment_id,
            "implementation_id": operand.computed_by.implementation_id,
            "receiver_id": operand.computed_by.receiver_id,
            "source_commit": operand.computed_by.source_commit,
        },
        "source": operand.source.value,
        "source_material": operand.source_material.value,
        "source_material_octet_length": operand.source_material_octet_length,
        "source_material_ref": operand.source_material_ref,
        "value": operand.value,
    }


def _maybe_unresolved_mapping(value: MaybeUnresolved) -> Any:
    """Render a bound string as a string, an unbound value as an explicit state.

    ``null`` is never emitted, and an unresolved value is never rendered as a
    bare string, so UNKNOWN, ABSENT, ERROR and REJECT remain distinguishable
    from each other and from a bound value.
    """
    if isinstance(value, UnresolvedValue):
        return {"detail": value.detail, "state": value.state.value}
    return value


def serialize_receipt(receipt: BoundaryReceipt) -> bytes:
    """Deterministic BC-02.1 v2 section 12 receipt serialization."""
    mapping = transport_mapping(receipt)
    _, values = walk(mapping)
    if any(value is None for value in values):
        raise ReceiptConstructionError("null is prohibited in a BC-02.1 receipt")
    return json.dumps(
        mapping,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")


def decode_transport_octets(encoded: str) -> bytes:
    """Reverse the Base64 transport encoding. Makes the representation checkable."""
    return base64.b64decode(encoded.encode("ascii"), validate=True)


def walk(node: Any) -> Tuple[List[str], List[Any]]:
    """Collect every key and every leaf value in a transport mapping."""
    keys: List[str] = []
    values: List[Any] = []
    if isinstance(node, dict):
        for key, child in node.items():
            keys.append(key)
            sub_keys, sub_values = walk(child)
            keys.extend(sub_keys)
            values.extend(sub_values)
    elif isinstance(node, (list, tuple)):
        for child in node:
            sub_keys, sub_values = walk(child)
            keys.extend(sub_keys)
            values.extend(sub_values)
    else:
        values.append(node)
    return keys, values
