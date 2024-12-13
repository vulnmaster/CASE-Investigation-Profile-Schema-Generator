"""
Configuration for insider threat investigations.
Maps insider threat specific concepts to CASE ontology, focusing on internal threats,
data exfiltration, and system misuse detection.
"""

from .base_config import BaseInvestigationType, CaseClass, CaseProperty

class InsiderThreatConfig(BaseInvestigationType):
    def __init__(self):
        super().__init__()
        self._init_insider_classes()
        self._init_insider_properties()
    
    def _init_insider_classes(self):
        """Initialize insider threat specific classes"""
        self.classes.update({
            "InsiderThreatActor": CaseClass(
                name="InsiderThreatActor",
                uri="https://ontology.caseontology.org/case/investigation/Subject",
                description="Employee or contractor under investigation",
                superclasses=["investigation:Subject"],
                properties=[
                    "employeeId", "accessLevel", "department", "role",
                    "threatCategory", "riskLevel", "supervisorContact",
                    "employmentStatus", "clearanceLevel"
                ]
            ),
            "DataExfiltrationEvent": CaseClass(
                name="DataExfiltrationEvent",
                uri="https://ontology.caseontology.org/case/investigation/InvestigativeAction",
                description="Data exfiltration activity detection",
                superclasses=["investigation:InvestigativeAction"],
                properties=[
                    "dataType", "dataVolume", "exfilMethod", "destination",
                    "detectionMethod", "impactAssessment", "preventiveMeasures"
                ]
            ),
            "SystemMisuseEvent": CaseClass(
                name="SystemMisuseEvent",
                uri="https://ontology.unifiedcyberontology.org/uco/observable/ObservableAction",
                description="Unauthorized system access or misuse",
                superclasses=["observable:ObservableAction"],
                properties=[
                    "systemAffected", "misuseType", "unauthorized_actions",
                    "impactLevel", "detectionSource"
                ]
            ),
            "SecurityAlert": CaseClass(
                name="SecurityAlert",
                uri="https://ontology.unifiedcyberontology.org/uco/observable/ObservablePattern",
                description="Security system generated alert",
                superclasses=["observable:ObservablePattern"],
                properties=[
                    "alertType", "severity", "triggerCondition", 
                    "detectionSystem", "falsePositiveStatus"
                ]
            ),
            "UserActivity": CaseClass(
                name="UserActivity",
                uri="https://ontology.unifiedcyberontology.org/uco/observable/UserSession",
                description="User activity monitoring record",
                superclasses=["observable:UserSession"],
                properties=[
                    "activityType", "timestamp", "location", "device",
                    "resourcesAccessed", "behaviorPattern"
                ]
            ),
            "SensitiveResource": CaseClass(
                name="SensitiveResource",
                uri="https://ontology.unifiedcyberontology.org/uco/observable/ObservableObject",
                description="Protected organizational resource",
                superclasses=["observable:ObservableObject"],
                properties=[
                    "resourceType", "classification", "accessControls",
                    "dataOwner", "protectionLevel"
                ]
            ),
            "DetectionTool": CaseClass(
                name="DetectionTool",
                uri="https://ontology.unifiedcyberontology.org/uco/tool/Tool",
                description="Insider threat detection software/tool",
                superclasses=["tool:Tool"],
                properties=[
                    "toolType", "detectionCapabilities", "alertThresholds",
                    "configurationSettings", "effectivenessMetrics"
                ]
            )
        })

    def _init_insider_properties(self):
        """Initialize insider threat specific properties"""
        self.properties.update({
            "threatCategory": CaseProperty(
                name="threatCategory",
                uri="https://ontology.caseontology.org/case/vocabulary/ThreatCategory",
                description="Category of insider threat (Pawn, Goof, Collaborator, Lone Wolf)",
                property_type="DatatypeProperty",
                range="xsd:string",
                required=True
            ),
            "exfilMethod": CaseProperty(
                name="exfilMethod",
                uri="https://ontology.caseontology.org/case/vocabulary/ExfiltrationMethod",
                description="Method used for data exfiltration",
                property_type="DatatypeProperty",
                range="xsd:string"
            ),
            "behaviorPattern": CaseProperty(
                name="behaviorPattern",
                uri="https://ontology.unifiedcyberontology.org/uco/observable/behaviorPattern",
                description="Pattern of user behavior",
                property_type="ObjectProperty",
                range="observable:ObservablePattern"
            ),
            "detectionSource": CaseProperty(
                name="detectionSource",
                uri="https://ontology.unifiedcyberontology.org/uco/tool/detectionSource",
                description="Source system that detected the threat",
                property_type="ObjectProperty",
                range="tool:Tool"
            ),
            "accessLevel": CaseProperty(
                name="accessLevel",
                uri="https://ontology.caseontology.org/case/vocabulary/AccessLevel",
                description="User's system access level",
                property_type="DatatypeProperty",
                range="xsd:string",
                required=True
            ),
            "impactAssessment": CaseProperty(
                name="impactAssessment",
                uri="https://ontology.caseontology.org/case/vocabulary/ImpactAssessment",
                description="Assessment of potential damage",
                property_type="DatatypeProperty",
                range="xsd:string"
            ),
            "resourcesAccessed": CaseProperty(
                name="resourcesAccessed",
                uri="https://ontology.unifiedcyberontology.org/uco/observable/resourcesAccessed",
                description="Resources accessed during activity",
                property_type="ObjectProperty",
                range="observable:ObservableObject"
            )
        }) 