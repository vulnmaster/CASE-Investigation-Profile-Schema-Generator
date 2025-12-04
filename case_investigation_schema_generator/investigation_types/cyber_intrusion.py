# investigation_types/cyber_intrusion.py

"""
Configuration for cyber intrusion investigations.
Maps STIX 2.1 objects and properties to CASE ontology for semantic interoperability
between STIX and CASE in cyber intrusion investigations.
"""

from .base_config import BaseInvestigationType, CaseClass, CaseProperty


class CyberIntrusionConfig(BaseInvestigationType):
    """
    This class defines the configuration for cyber intrusion investigations.
    It maps STIX 2.1 objects and properties to the CASE ontology, enabling semantic
    interoperability and alignment between STIX and CASE for handling cyber intrusion data.
    """

    def __init__(self):
        super().__init__()
        self._init_cyber_classes()
        self._init_cyber_properties()

    def _init_cyber_classes(self):
        """Initialize cyber intrusion specific classes mapping STIX to CASE"""
        self.classes.update(
            {
                # STIX Cyber Observable Objects mapped to CASE/UCO
                "Artifact": CaseClass(
                    name="Artifact",
                    uri="https://ontology.unifiedcyberontology.org/uco/observable/File",
                    description="Raw binary data or file content",
                    superclasses=["observable:Observable"],
                    properties=[
                        "mime_type",
                        "payload_bin",
                        "url",
                        "hashes",
                        "encryption_algorithm",
                    ],
                ),
                "AutonomousSystem": CaseClass(
                    name="AutonomousSystem",
                    uri="https://ontology.unifiedcyberontology.org/uco/observable/AutonomousSystem",
                    description="An autonomous system (AS) in BGP routing",
                    superclasses=["observable:Observable"],
                    properties=["number", "name", "rir"],
                ),
                "Directory": CaseClass(
                    name="Directory",
                    uri="https://ontology.unifiedcyberontology.org/uco/observable/Directory",
                    description="Directory/folder in a file system",
                    superclasses=["observable:Observable"],
                    properties=["path", "path_enc", "created", "modified", "accessed"],
                ),
                "DomainName": CaseClass(
                    name="DomainName",
                    uri="https://ontology.unifiedcyberontology.org/uco/observable/DomainName",
                    description="Network domain name",
                    superclasses=["observable:Observable"],
                    properties=["value", "resolves_to_refs"],
                ),
                "EmailAddress": CaseClass(
                    name="EmailAddress",
                    uri="https://ontology.unifiedcyberontology.org/uco/observable/EmailAddress",
                    description="Email address",
                    superclasses=["observable:Observable"],
                    properties=["value", "display_name"],
                ),
                "EmailMessage": CaseClass(
                    name="EmailMessage",
                    uri="https://ontology.unifiedcyberontology.org/uco/observable/EmailMessage",
                    description="Email message",
                    superclasses=["observable:Observable"],
                    properties=[
                        "is_multipart",
                        "date",
                        "content_type",
                        "from_ref",
                        "sender_ref",
                        "to_refs",
                        "cc_refs",
                        "bcc_refs",
                        "subject",
                        "received_lines",
                        "additional_header_fields",
                        "body",
                        "body_multipart",
                        "raw_email_ref",
                    ],
                ),
                "File": CaseClass(
                    name="File",
                    uri="https://ontology.unifiedcyberontology.org/uco/observable/File",
                    description="Properties of a file",
                    superclasses=["observable:Observable"],
                    properties=[
                        "hashes",
                        "size",
                        "name",
                        "name_enc",
                        "magic_number_hex",
                        "mime_type",
                        "created",
                        "modified",
                        "accessed",
                        "parent_directory_ref",
                        "content_ref",
                        "is_encrypted",
                        "encryption_algorithm",
                        "decryption_key",
                    ],
                ),
                "IPv4Address": CaseClass(
                    name="IPv4Address",
                    uri="https://ontology.unifiedcyberontology.org/uco/observable/IPv4Address",
                    description="IPv4 network address",
                    superclasses=["observable:Observable"],
                    properties=["value", "resolves_to_refs", "belongs_to_refs"],
                ),
                "IPv6Address": CaseClass(
                    name="IPv6Address",
                    uri="https://ontology.unifiedcyberontology.org/uco/observable/IPv6Address",
                    description="IPv6 network address",
                    superclasses=["observable:Observable"],
                    properties=["value", "resolves_to_refs", "belongs_to_refs"],
                ),
                "NetworkTraffic": CaseClass(
                    name="NetworkTraffic",
                    uri="https://ontology.unifiedcyberontology.org/uco/observable/NetworkTraffic",
                    description="Network traffic data",
                    superclasses=["observable:Observable"],
                    properties=[
                        "start",
                        "end",
                        "is_active",
                        "src_ref",
                        "dst_ref",
                        "src_port",
                        "dst_port",
                        "protocols",
                        "src_byte_count",
                        "dst_byte_count",
                        "src_packets",
                        "dst_packets",
                        "ipfix",
                        "src_payload_ref",
                        "dst_payload_ref",
                        "encapsulates_refs",
                        "encapsulated_by_ref",
                    ],
                ),
                # STIX Attack Pattern mapped to CASE
                "AttackPattern": CaseClass(
                    name="AttackPattern",
                    uri="https://ontology.caseontology.org/case/investigation/AttackPattern",
                    description="A type of TTP that describes ways that adversaries attempt to compromise targets",
                    superclasses=["action:Action"],
                    properties=[
                        "name",
                        "description",
                        "kill_chain_phases",
                        "external_references",
                    ],
                ),
                # STIX Indicator mapped to CASE
                "Indicator": CaseClass(
                    name="Indicator",
                    uri="https://ontology.caseontology.org/case/investigation/Indicator",
                    description="Pattern used to detect suspicious or malicious cyber activity",
                    superclasses=["observable:Observable"],
                    properties=[
                        "pattern",
                        "pattern_type",
                        "pattern_version",
                        "valid_from",
                        "valid_until",
                        "kill_chain_phases",
                    ],
                ),
            }
        )

    def _init_cyber_properties(self):
        """Initialize cyber intrusion specific properties mapping STIX to CASE"""
        self.properties.update(
            {
                # Common STIX properties mapped to CASE/UCO
                "type": CaseProperty(
                    name="type",
                    uri="https://ontology.unifiedcyberontology.org/uco/core/type",
                    description="The type of object",
                    property_type="DatatypeProperty",
                    range="xsd:string",
                    required=True,
                ),
                "id": CaseProperty(
                    name="id",
                    uri="https://ontology.unifiedcyberontology.org/uco/core/id",
                    description="Unique identifier for object",
                    property_type="DatatypeProperty",
                    range="xsd:string",
                    required=True,
                ),
                # Network-related properties
                "value": CaseProperty(
                    name="value",
                    uri="https://ontology.unifiedcyberontology.org/uco/observable/value",
                    description="Value of the observable object",
                    property_type="DatatypeProperty",
                    range="xsd:string",
                    required=True,
                ),
                "hashes": CaseProperty(
                    name="hashes",
                    uri="https://ontology.unifiedcyberontology.org/uco/observable/hash",
                    description="Cryptographic hash values",
                    property_type="ObjectProperty",
                    range="observable:Hash",
                ),
                # Time-related properties
                "created": CaseProperty(
                    name="created",
                    uri="https://ontology.unifiedcyberontology.org/uco/core/created",
                    description="Timestamp of creation",
                    property_type="DatatypeProperty",
                    range="xsd:dateTime",
                ),
                "modified": CaseProperty(
                    name="modified",
                    uri="https://ontology.unifiedcyberontology.org/uco/core/modified",
                    description="Timestamp of last modification",
                    property_type="DatatypeProperty",
                    range="xsd:dateTime",
                ),
            }
        )
