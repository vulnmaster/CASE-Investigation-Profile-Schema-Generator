"""
Base configuration for CASE investigation types.
Defines common structures and utilities used across all investigation types.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class CaseClass:
    """Represents a class from the CASE ontology"""

    name: str
    uri: str
    description: str
    superclasses: List[str]
    properties: List[str]


@dataclass
class CaseProperty:
    """Represents a property from the CASE ontology"""

    name: str
    uri: str
    description: str
    property_type: str
    range: Optional[str] = None
    required: bool = False


class BaseInvestigationType:
    """Base class for all investigation type configurations"""

    def __init__(self):
        self.classes: Dict[str, CaseClass] = {}
        self.properties: Dict[str, CaseProperty] = {}
        self._init_core_classes()
        self._init_core_properties()

    def _init_core_classes(self):
        """Initialize core CASE/UCO classes used across all investigation types"""
        self.classes.update(
            {
                "UcoObject": CaseClass(
                    name="UcoObject",
                    uri="https://ontology.unifiedcyberontology.org/uco/core/UcoObject",
                    description="Base class for all UCO objects",
                    superclasses=["UcoThing"],
                    properties=[
                        "createdBy",
                        "description",
                        "externalReference",
                        "hasFacet",
                        "modifiedTime",
                        "name",
                        "objectCreatedTime",
                        "specVersion",
                        "tag",
                    ],
                ),
                "Investigation": CaseClass(
                    name="Investigation",
                    uri="https://ontology.caseontology.org/case/investigation/Investigation",
                    description="A structured investigation of a cyber-related set of circumstances",
                    superclasses=["UcoObject"],
                    properties=[
                        "investigativeActions",
                        "subjects",
                        "provenance",
                        "observables",
                        "physicalEvidence",
                        "deviceEvidence",
                        "systemMonitoring",
                        "userActivity",
                        "victimIdentification",
                    ],
                ),
            }
        )

    def _init_core_properties(self):
        """Initialize core CASE/UCO properties used across all investigation types"""
        self.properties.update(
            {
                "createdBy": CaseProperty(
                    name="createdBy",
                    uri="https://ontology.unifiedcyberontology.org/uco/core/createdBy",
                    description="The identity that created this object",
                    property_type="ObjectProperty",
                    range="core:IdentityAbstraction",
                    required=True,
                ),
                "objectCreatedTime": CaseProperty(
                    name="objectCreatedTime",
                    uri="https://ontology.unifiedcyberontology.org/uco/core/objectCreatedTime",
                    description="Time at which the object was created",
                    property_type="DatatypeProperty",
                    range="xsd:dateTime",
                    required=True,
                ),
            }
        )
