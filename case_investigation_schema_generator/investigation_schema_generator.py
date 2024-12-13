"""
CASE Investigation Schema Generator

This module provides functionality to generate JSON schemas that are semantically compatible
with the Cyber-investigation Analysis Standard Expression (CASE) ontology.
It supports multiple investigation types and ensures proper mapping between domain-specific 
schemas and the CASE ontology.

Investigation Types Supported:
- Cyber Intrusion: Maps STIX 2.1 objects to CASE for cyber investigations
- Murder: Supports physical and digital evidence for homicide cases
- Child Abuse: Specialized for child abuse investigations with CSAM tracking
- Insider Threat: Focuses on internal security threats and data exfiltration
- See readme.md for more details on adding new investigation types

The generated schemas:
1. Maintain proper inheritance from CASE/UCO base objects
2. Include correct semantic definitions and relationships
3. Preserve required properties and constraints
4. Support validation of investigation-specific data
5. Enable lossless conversion between JSON and RDF formats

Author: Cpry Hall, Cyber Domain Ontology Project
License: Apache 2.0
"""

from typing import Dict, List, Optional
import json
from enum import Enum
from dataclasses import dataclass
from .investigation_types.cyber_intrusion import CyberIntrusionConfig
from .investigation_types.murder_investigation import MurderConfig
from .investigation_types.child_abuse_investigation import ChildAbuseConfig
from .investigation_types.insider_threat_investigation import InsiderThreatConfig

class InvestigationType(Enum):
    CYBER_INTRUSION = "CyberIntrusion"
    MURDER = "Murder" 
    CHILD_ABUSE = "ChildAbuse"
    INSIDER_THREAT = "InsiderThreat"

@dataclass
class CaseProperty:
    name: str
    property_type: str
    description: str
    required: bool = False
    range: Optional[str] = None

class CaseSchemaGenerator:
    def __init__(self):
        # Core properties from CASE/UCO that most objects inherit
        self.core_properties = [
            CaseProperty(
                name="@id",
                property_type="string",
                description="Unique identifier for this object",
                required=True
            ),
            CaseProperty(
                name="@type", 
                property_type="string",
                description="The type of this object (from CASE vocabulary)",
                required=True
            ),
            CaseProperty(
                name="createdBy",
                property_type="object",
                description="The identity that created this object",
                required=True,
                range="core:IdentityAbstraction"
            ),
            CaseProperty(
                name="description",
                property_type="string", 
                description="A description of this object"
            ),
            CaseProperty(
                name="modifiedTime",
                property_type="string",
                description="The time this object was last modified",
                range="xsd:dateTime"
            ),
            CaseProperty(
                name="name",
                property_type="string",
                description="The name of this object",
                required=True,
                range="string"
            ),
            CaseProperty(
                name="objectCreatedTime",
                property_type="string",
                description="When this object was created",
                required=True,
                range="xsd:dateTime"
            ),
            CaseProperty(
                name="specVersion",
                property_type="string",
                description="Version of UCO ontology specification used",
                required=True
            )
        ]

        self.investigation_configs = {
            InvestigationType.CYBER_INTRUSION: CyberIntrusionConfig(),
            InvestigationType.MURDER: MurderConfig(),
            InvestigationType.CHILD_ABUSE: ChildAbuseConfig(),
            InvestigationType.INSIDER_THREAT: InsiderThreatConfig()
        }

    def generate_investigation_schema(self, investigation_type: InvestigationType) -> Dict:
        """Generate a JSON schema for the specified investigation type"""
        
        schema = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "properties": {
                "@context": {
                    "type": "object",
                    "properties": {
                        "case": {"type": "string", "const": "https://ontology.caseontology.org/case/case"},
                        "investigation": {"type": "string", "const": "https://ontology.caseontology.org/case/investigation"},
                        "core": {"type": "string", "const": "https://ontology.unifiedcyberontology.org/uco/core"},
                        "vocabulary": {"type": "string", "const": "https://ontology.caseontology.org/case/vocabulary"},
                        "xsd": {"type": "string", "const": "http://www.w3.org/2001/XMLSchema#"}
                    },
                    "required": ["case", "investigation", "core", "vocabulary", "xsd"]
                }
            },
            "required": ["@context"],
            "definitions": self._generate_base_definitions()
        }

        # Add core properties
        properties = {}
        required = ["@context"]
        for prop in self.core_properties:
            properties[prop.name] = {
                "type": prop.property_type,
                "description": prop.description
            }
            if prop.range:
                if ":" in prop.range:
                    properties[prop.name]["$ref"] = f"#/definitions/{prop.range.replace(':', '_')}"
                else:
                    properties[prop.name]["$ref"] = f"#/definitions/{prop.range}"
            if prop.required:
                required.append(prop.name)

        # Add investigation-specific properties based on type
        if investigation_type == InvestigationType.CYBER_INTRUSION:
            self._add_cyber_intrusion_properties(properties)
        elif investigation_type == InvestigationType.MURDER:
            self._add_murder_properties(properties)
        elif investigation_type == InvestigationType.CHILD_ABUSE:
            self._add_child_abuse_properties(properties)
        elif investigation_type == InvestigationType.INSIDER_THREAT:
            self._add_insider_threat_properties(properties)

        schema["properties"].update(properties)
        schema["required"] = required
        
        return schema

    def _generate_base_definitions(self) -> Dict:
        """Generate base definitions for CASE/UCO objects"""
        return {
            "core_UcoObject": {
                "type": "object",
                "description": "Base object that all UCO objects inherit from",
                "properties": {
                    "@id": {"type": "string"},
                    "@type": {"type": "string"},
                    "createdBy": {"$ref": "#/definitions/core_IdentityAbstraction"},
                    "description": {"type": "string"},
                    "modifiedTime": {"type": "string", "format": "date-time"},
                    "name": {"type": "string"},
                    "objectCreatedTime": {"type": "string", "format": "date-time"},
                    "specVersion": {"type": "string"}
                },
                "required": ["@id", "@type", "objectCreatedTime", "specVersion"]
            },
            "core_IdentityAbstraction": {
                "type": "object",
                "description": "A grouping of identifying characteristics unique to an individual or organization",
                "allOf": [
                    {"$ref": "#/definitions/core_UcoObject"},
                    {
                        "properties": {
                            "@type": {"const": "core:IdentityAbstraction"},
                            "createdBy": {"$ref": "#/definitions/core_IdentityAbstraction"}
                        }
                    }
                ]
            },
            "investigation_InvestigativeAction": {
                "type": "object",
                "description": "An investigative action performed during the investigation",
                "allOf": [
                    {"$ref": "#/definitions/core_UcoObject"},
                    {
                        "properties": {
                            "@type": {"const": "investigation:InvestigativeAction"},
                            "startTime": {"type": "string", "format": "date-time"},
                            "endTime": {"type": "string", "format": "date-time"},
                            "status": {"type": "string"},
                            "authorizationIdentifier": {"type": "string"}
                        }
                    }
                ]
            }
        }

    def _add_cyber_intrusion_properties(self, properties: Dict):
        """Add properties specific to cyber intrusion investigations"""
        properties.update({
            "investigativeActions": {
                "type": "array",
                "items": {
                    "$ref": "#/definitions/investigation_InvestigativeAction"
                },
                "description": "Actions taken during the cyber intrusion investigation"
            },
            "observables": {
                "type": "array", 
                "items": {
                    "type": "object",
                    "allOf": [
                        {"$ref": "#/definitions/core_UcoObject"},
                        {
                            "properties": {
                                "@type": {"const": "observable:CyberItem"},
                                "observableType": {"type": "string"},
                                "hasChanged": {"type": "boolean"},
                                "state": {"type": "string"}
                            }
                        }
                    ]
                },
                "description": "Digital artifacts observed during investigation"
            },
            "subjects": {
                "type": "array",
                "items": {
                    "type": "object",
                    "allOf": [
                        {"$ref": "#/definitions/core_UcoObject"},
                        {
                            "properties": {
                                "@type": {"const": "core:Identity"},
                                "identityType": {"type": "string"},
                                "role": {"type": "string"}
                            }
                        }
                    ]
                },
                "description": "Subjects involved in the investigation"
            }
        })

    def _add_murder_properties(self, properties: Dict):
        """Add properties specific to murder investigations"""
        properties.update({
            "investigativeActions": {
                "type": "array",
                "items": {
                    "$ref": "#/definitions/investigation_InvestigativeAction"
                },
                "description": "Actions taken during the murder investigation"
            },
            "physicalEvidence": {
                "type": "array",
                "items": {
                    "type": "object",
                    "allOf": [
                        {"$ref": "#/definitions/core_UcoObject"},
                        {
                            "properties": {
                                "@type": {"const": "case:PhysicalEvidence"},
                                "evidenceType": {"type": "string"},
                                "location": {"type": "string"},
                                "condition": {"type": "string"}
                            }
                        }
                    ]
                },
                "description": "Physical evidence collected during investigation"
            }
        })

    def _add_child_abuse_properties(self, properties: Dict):
        """Add properties specific to child abuse investigations"""
        properties.update({
            "investigativeActions": {
                "type": "array",
                "items": {
                    "$ref": "#/definitions/investigation_InvestigativeAction"
                },
                "description": "Actions taken during the child abuse investigation"
            },
            "digitalEvidence": {
                "type": "array",
                "items": {
                    "type": "object",
                    "allOf": [
                        {"$ref": "#/definitions/core_UcoObject"},
                        {
                            "properties": {
                                "@type": {"const": "case:DigitalEvidence"},
                                "evidenceType": {"type": "string"},
                                "hash": {"type": "string"},
                                "classification": {"type": "string"}
                            }
                        }
                    ]
                },
                "description": "Digital evidence collected during investigation"
            }
        })

    def _add_insider_threat_properties(self, properties: Dict):
        """Add properties specific to insider threat investigations"""
        properties.update({
            "investigativeActions": {
                "type": "array",
                "items": {
                    "$ref": "#/definitions/investigation_InvestigativeAction"
                },
                "description": "Actions taken during the insider threat investigation"
            },
            "systemMonitoring": {
                "type": "array",
                "items": {
                    "type": "object",
                    "allOf": [
                        {"$ref": "#/definitions/core_UcoObject"},
                        {
                            "properties": {
                                "@type": {"const": "case:SystemMonitoring"},
                                "monitoringType": {"type": "string"},
                                "timestamp": {"type": "string", "format": "date-time"},
                                "activity": {"type": "string"}
                            }
                        }
                    ]
                },
                "description": "System monitoring data collected during investigation"
            }
        })

    def save_schema(self, schema: Dict, filename: str):
        """Save the generated schema to a file"""
        with open(filename, 'w') as f:
            json.dump(schema, f, indent=2) 