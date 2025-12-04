"""
Configuration for murder investigations.
Maps murder investigation specific classes and properties to CASE ontology,
with special focus on digital evidence and location tracking.
"""

from .base_config import BaseInvestigationType, CaseClass, CaseProperty


class MurderConfig(BaseInvestigationType):
    def __init__(self):
        super().__init__()
        self._init_murder_classes()
        self._init_murder_properties()

    def _init_murder_classes(self):
        """Initialize murder investigation specific classes"""
        self.classes.update(
            {
                "CrimeScene": CaseClass(
                    name="CrimeScene",
                    uri="https://ontology.unifiedcyberontology.org/uco/location/Location",
                    description="Physical location where the crime occurred",
                    superclasses=["location:Location"],
                    properties=[
                        "latitude",
                        "longitude",
                        "address",
                        "sceneType",
                        "securitySystems",
                        "accessPoints",
                        "digitalDevicesPresent",
                    ],
                ),
                "PhysicalEvidence": CaseClass(
                    name="PhysicalEvidence",
                    uri="https://ontology.caseontology.org/case/investigation/ProvenanceRecord",
                    description="Physical evidence collected during investigation",
                    superclasses=["investigation:ProvenanceRecord"],
                    properties=[
                        "evidenceType",
                        "chainOfCustody",
                        "collectionLocation",
                        "forensicAnalysis",
                        "digitalDocumentation",
                    ],
                ),
                "VictimDevice": CaseClass(
                    name="VictimDevice",
                    uri="https://ontology.unifiedcyberontology.org/uco/observable/Device",
                    description="Digital device belonging to the victim",
                    superclasses=["observable:Device"],
                    properties=[
                        "deviceType",
                        "owner",
                        "lastAccessed",
                        "dataExtracted",
                        "encryptionStatus",
                        "relevantFiles",
                        "communicationHistory",
                    ],
                ),
                "DigitalCommunication": CaseClass(
                    name="DigitalCommunication",
                    uri="https://ontology.unifiedcyberontology.org/uco/observable/Message",
                    description="Digital communications relevant to investigation",
                    superclasses=["observable:Message"],
                    properties=[
                        "communicationType",
                        "sender",
                        "recipient",
                        "timestamp",
                        "content",
                        "platform",
                        "relevance",
                        "threatContent",
                    ],
                ),
                "LocationHistory": CaseClass(
                    name="LocationHistory",
                    uri="https://ontology.unifiedcyberontology.org/uco/location/LocationHistory",
                    description="Historical location data from devices",
                    superclasses=["location:Location"],
                    properties=[
                        "device",
                        "timestamp",
                        "coordinates",
                        "accuracy",
                        "source",
                        "activity",
                        "correlatedEvents",
                    ],
                ),
                "OnlineActivity": CaseClass(
                    name="OnlineActivity",
                    uri="https://ontology.unifiedcyberontology.org/uco/observable/BrowserHistory",
                    description="Web browsing and online activities",
                    superclasses=["observable:BrowserHistory"],
                    properties=[
                        "searchTerms",
                        "visitedURLs",
                        "timestamp",
                        "device",
                        "accountUsed",
                        "relevantSearches",
                        "suspiciousActivity",
                    ],
                ),
                "SurveillanceData": CaseClass(
                    name="SurveillanceData",
                    uri="https://ontology.unifiedcyberontology.org/uco/observable/ObservableObject",
                    description="Data from surveillance systems",
                    superclasses=["observable:ObservableObject"],
                    properties=[
                        "systemType",
                        "location",
                        "timeRange",
                        "capturedEvents",
                        "dataFormat",
                        "relevantFootage",
                        "retentionPeriod",
                    ],
                ),
            }
        )

    def _init_murder_properties(self):
        """Initialize murder investigation specific properties"""
        self.properties.update(
            {
                "evidenceType": CaseProperty(
                    name="evidenceType",
                    uri="https://ontology.caseontology.org/case/vocabulary/EvidenceType",
                    description="Type of forensic evidence",
                    property_type="DatatypeProperty",
                    range="xsd:string",
                    required=True,
                ),
                "locationTimestamp": CaseProperty(
                    name="locationTimestamp",
                    uri="https://ontology.unifiedcyberontology.org/uco/location/locationTimestamp",
                    description="Timestamp for location data",
                    property_type="DatatypeProperty",
                    range="xsd:dateTime",
                    required=True,
                ),
                "deviceOwner": CaseProperty(
                    name="deviceOwner",
                    uri="https://ontology.unifiedcyberontology.org/uco/observable/deviceOwner",
                    description="Owner of the digital device",
                    property_type="ObjectProperty",
                    range="core:Identity",
                ),
                "communicationContent": CaseProperty(
                    name="communicationContent",
                    uri="https://ontology.unifiedcyberontology.org/uco/observable/content",
                    description="Content of digital communication",
                    property_type="DatatypeProperty",
                    range="xsd:string",
                ),
                "relevanceAssessment": CaseProperty(
                    name="relevanceAssessment",
                    uri="https://ontology.caseontology.org/case/investigation/relevanceAssessment",
                    description="Assessment of evidence relevance to investigation",
                    property_type="DatatypeProperty",
                    range="xsd:string",
                ),
                "digitalDocumentation": CaseProperty(
                    name="digitalDocumentation",
                    uri="https://ontology.caseontology.org/case/investigation/digitalDocumentation",
                    description="Digital documentation of physical evidence",
                    property_type="ObjectProperty",
                    range="observable:File",
                ),
                "suspiciousActivity": CaseProperty(
                    name="suspiciousActivity",
                    uri="https://ontology.caseontology.org/case/vocabulary/SuspiciousActivityType",
                    description="Indicators of suspicious online activity",
                    property_type="DatatypeProperty",
                    range="xsd:string",
                ),
            }
        )
