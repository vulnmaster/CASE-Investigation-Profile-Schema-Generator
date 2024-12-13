"""
Configuration for child abuse investigations.
Maps child abuse specific concepts to CASE ontology, with special focus on digital evidence
and online exploitation aspects.
"""

from .base_config import BaseInvestigationType, CaseClass, CaseProperty

class ChildAbuseConfig(BaseInvestigationType):
    def __init__(self):
        super().__init__()
        self._init_abuse_classes()
        self._init_abuse_properties()
    
    def _init_abuse_classes(self):
        """Initialize child abuse specific classes"""
        self.classes.update({
            "ChildVictim": CaseClass(
                name="ChildVictim",
                uri="https://ontology.caseontology.org/case/investigation/Victim",
                description="Child victim of abuse",
                superclasses=["core:Role"],
                properties=[
                    "age", "guardian", "schoolInformation", "medicalHistory",
                    "onlinePlatformsUsed", "deviceAccess", "vulnerabilityFactors"
                ]
            ),
            "AbuseIncident": CaseClass(
                name="AbuseIncident",
                uri="https://ontology.caseontology.org/case/investigation/InvestigativeAction",
                description="Documented incident of abuse",
                superclasses=["investigation:InvestigativeAction"],
                properties=[
                    "incidentType", "location", "dateTime", "witnesses",
                    "digitalEvidence", "platformsInvolved", "reportingSource"
                ]
            ),
            "CSAMEvidence": CaseClass(
                name="CSAMEvidence",
                uri="https://ontology.caseontology.org/case/investigation/ProvenanceRecord",
                description="Child Sexual Abuse Material evidence",
                superclasses=["investigation:ProvenanceRecord"],
                properties=[
                    "hashValue", "classification", "source", "discoveryMethod",
                    "forensicTooling", "chainOfCustody", "ncmecReport"
                ]
            ),
            "OnlinePlatform": CaseClass(
                name="OnlinePlatform",
                uri="https://ontology.unifiedcyberontology.org/uco/observable/Application",
                description="Digital platform used in abuse",
                superclasses=["observable:Application"],
                properties=[
                    "platformType", "userAccounts", "contentFound", 
                    "accessDates", "communicationMethods"
                ]
            ),
            "DigitalCommunication": CaseClass(
                name="DigitalCommunication",
                uri="https://ontology.unifiedcyberontology.org/uco/observable/Message",
                description="Digital communications related to abuse",
                superclasses=["observable:Message"],
                properties=[
                    "communicationType", "participants", "content",
                    "timestamp", "platform", "attachments"
                ]
            ),
            "OffenderDevice": CaseClass(
                name="OffenderDevice",
                uri="https://ontology.unifiedcyberontology.org/uco/observable/Device",
                description="Digital device used by offender",
                superclasses=["observable:Device"],
                properties=[
                    "deviceType", "storageCapacity", "encryptionStatus",
                    "networkConnections", "installedApps", "forensicImage"
                ]
            ),
            "CyberTipReport": CaseClass(
                name="CyberTipReport",
                uri="https://ontology.caseontology.org/case/investigation/ProvenanceRecord",
                description="NCMEC CyberTipline report",
                superclasses=["investigation:ProvenanceRecord"],
                properties=[
                    "reportId", "reportingESP", "incidentType", 
                    "reportDate", "contentLocation", "ipAddresses"
                ]
            )
        })

    def _init_abuse_properties(self):
        """Initialize child abuse specific properties"""
        self.properties.update({
            "incidentType": CaseProperty(
                name="incidentType",
                uri="https://ontology.caseontology.org/case/vocabulary/IncidentType",
                description="Type of abuse incident",
                property_type="DatatypeProperty",
                range="xsd:string",
                required=True
            ),
            "hashValue": CaseProperty(
                name="hashValue",
                uri="https://ontology.unifiedcyberontology.org/uco/observable/hash",
                description="Cryptographic hash of CSAM evidence",
                property_type="DatatypeProperty",
                range="xsd:string",
                required=True
            ),
            "platformType": CaseProperty(
                name="platformType",
                uri="https://ontology.caseontology.org/case/vocabulary/PlatformType",
                description="Type of online platform",
                property_type="DatatypeProperty",
                range="xsd:string"
            ),
            "communicationType": CaseProperty(
                name="communicationType",
                uri="https://ontology.caseontology.org/case/vocabulary/CommunicationType",
                description="Type of digital communication",
                property_type="DatatypeProperty",
                range="xsd:string"
            ),
            "ncmecReport": CaseProperty(
                name="ncmecReport",
                uri="https://ontology.caseontology.org/case/investigation/ncmecReport",
                description="Reference to NCMEC CyberTipline report",
                property_type="ObjectProperty",
                range="investigation:ProvenanceRecord"
            ),
            "forensicTooling": CaseProperty(
                name="forensicTooling",
                uri="https://ontology.unifiedcyberontology.org/uco/tool/Tool",
                description="Forensic tools used in evidence analysis",
                property_type="ObjectProperty",
                range="tool:Tool"
            )
        }) 