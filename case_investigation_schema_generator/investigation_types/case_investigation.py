"""
CASE Investigation Namespace Configuration.
Maps core investigation classes and properties from the CASE ontology investigation namespace.
This can be combined with specific investigation type schemas for richer investigation documentation.
"""

from .base_config import BaseInvestigationType, CaseClass, CaseProperty

class CaseInvestigationConfig(BaseInvestigationType):
    def __init__(self):
        super().__init__()
        self._init_investigation_classes()
        self._init_investigation_properties()
    
    def _init_investigation_classes(self):
        """Initialize CASE investigation namespace classes"""
        self.classes.update({
            "Attorney": CaseClass(
                name="Attorney",
                uri="https://ontology.caseontology.org/case/investigation/Attorney",
                description="A legal professional involved in the investigation",
                superclasses=["core:Role"],
                properties=["barNumber", "jurisdiction", "representedParty"]
            ),
            "Authorization": CaseClass(
                name="Authorization",
                uri="https://ontology.caseontology.org/case/investigation/Authorization",
                description="Legal authorization for investigative actions",
                superclasses=["core:UcoObject"],
                properties=["authorizationType", "authorizationIdentifier", "authorizedBy", 
                          "validFrom", "validUntil", "scope"]
            ),
            "Examiner": CaseClass(
                name="Examiner",
                uri="https://ontology.caseontology.org/case/investigation/Examiner",
                description="Person who performs forensic examination of evidence",
                superclasses=["core:Role"],
                properties=["certification", "organization", "examinerType"]
            ),
            "ExaminerActionLifecycle": CaseClass(
                name="ExaminerActionLifecycle",
                uri="https://ontology.caseontology.org/case/investigation/ExaminerActionLifecycle",
                description="Timeline of actions performed by an examiner",
                superclasses=["core:ActionLifecycle"],
                properties=["examiner", "authorization", "toolsUsed"]
            ),
            "Investigation": CaseClass(
                name="Investigation",
                uri="https://ontology.caseontology.org/case/investigation/Investigation",
                description="A structured investigation of circumstances",
                superclasses=["core:UcoObject"],
                properties=["focus", "investigationStatus", "investigationType", 
                          "startTime", "endTime", "investigativeActions"]
            ),
            "InvestigativeAction": CaseClass(
                name="InvestigativeAction",
                uri="https://ontology.caseontology.org/case/investigation/InvestigativeAction",
                description="An action taken as part of an investigation",
                superclasses=["action:Action"],
                properties=["authorization", "performer", "startTime", "endTime", 
                          "location", "objects", "result"]
            ),
            "Investigator": CaseClass(
                name="Investigator",
                uri="https://ontology.caseontology.org/case/investigation/Investigator",
                description="Person conducting the investigation",
                superclasses=["core:Role"],
                properties=["badgeNumber", "organization", "investigatorType"]
            ),
            "ProvenanceRecord": CaseClass(
                name="ProvenanceRecord",
                uri="https://ontology.caseontology.org/case/investigation/ProvenanceRecord",
                description="Record of the origins and custody of evidence",
                superclasses=["core:UcoObject"],
                properties=["exhibitNumber", "custody", "priorLocation", 
                          "transferTime", "transferredBy"]
            ),
            "Subject": CaseClass(
                name="Subject",
                uri="https://ontology.caseontology.org/case/investigation/Subject",
                description="Person of investigative interest",
                superclasses=["core:Role"],
                properties=["subjectType", "isConfidential", "aliases"]
            ),
            "SubjectActionLifecycle": CaseClass(
                name="SubjectActionLifecycle",
                uri="https://ontology.caseontology.org/case/investigation/SubjectActionLifecycle",
                description="Timeline of actions performed by a subject",
                superclasses=["core:ActionLifecycle"],
                properties=["subject", "actionType", "location"]
            ),
            "VictimActionLifecycle": CaseClass(
                name="VictimActionLifecycle",
                uri="https://ontology.caseontology.org/case/investigation/VictimActionLifecycle",
                description="Timeline of actions related to a victim",
                superclasses=["core:ActionLifecycle"],
                properties=["victim", "impactSeverity", "victimImpact"]
            )
        })

    def _init_investigation_properties(self):
        """Initialize CASE investigation namespace properties"""
        self.properties.update({
            "authorizationType": CaseProperty(
                name="authorizationType",
                uri="https://ontology.caseontology.org/case/investigation/authorizationType",
                description="Type of legal authorization",
                property_type="DatatypeProperty",
                range="xsd:string",
                required=True
            ),
            "investigationStatus": CaseProperty(
                name="investigationStatus",
                uri="https://ontology.caseontology.org/case/investigation/investigationStatus",
                description="Current status of the investigation",
                property_type="DatatypeProperty",
                range="xsd:string",
                required=True
            ),
            "exhibitNumber": CaseProperty(
                name="exhibitNumber",
                uri="https://ontology.caseontology.org/case/investigation/exhibitNumber",
                description="Identifier assigned to evidence exhibit",
                property_type="DatatypeProperty",
                range="xsd:string",
                required=True
            )
        }) 