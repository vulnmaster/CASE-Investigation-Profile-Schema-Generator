import pytest

from case_investigation_schema_generator.investigation_types.case_investigation import (
    CaseInvestigationConfig,
)


def test_case_investigation_config():
    """Test initialization and configuration of CaseInvestigationConfig"""
    config = CaseInvestigationConfig()

    # Test core classes are present
    assert "Investigation" in config.classes
    assert "UcoObject" in config.classes

    # Test core properties are present
    assert "createdBy" in config.properties
    assert "objectCreatedTime" in config.properties

    # Test case-specific properties
    investigation = config.classes["Investigation"]
    assert "investigationType" in investigation.properties


def test_case_investigation_config_initialization():
    """Test initialization of CaseInvestigationConfig"""
    config = CaseInvestigationConfig()

    # Verify core classes are inherited
    assert "UcoObject" in config.classes
    assert "Investigation" in config.classes

    # Verify case investigation specific classes
    assert "Attorney" in config.classes
    assert "Examiner" in config.classes
    assert "Investigator" in config.classes
    assert "ProvenanceRecord" in config.classes


def test_case_investigation_class_properties():
    """Test properties of case investigation classes"""
    config = CaseInvestigationConfig()

    # Test Investigation class
    investigation = config.classes["Investigation"]
    assert investigation.name == "Investigation"
    assert "investigationStatus" in investigation.properties
    assert "investigationType" in investigation.properties
    assert "investigativeActions" in investigation.properties

    # Test InvestigativeAction class
    action = config.classes["InvestigativeAction"]
    assert action.name == "InvestigativeAction"
    assert "authorization" in action.properties
    assert "performer" in action.properties
    assert "result" in action.properties


def test_case_investigation_properties():
    """Test case investigation specific properties"""
    config = CaseInvestigationConfig()

    # Test authorization properties
    assert "authorizationType" in config.properties
    auth_prop = config.properties["authorizationType"]
    assert auth_prop.property_type == "DatatypeProperty"
    assert auth_prop.range == "xsd:string"
    assert auth_prop.required is True

    # Test investigation status property
    assert "investigationStatus" in config.properties
    status_prop = config.properties["investigationStatus"]
    assert status_prop.property_type == "DatatypeProperty"
    assert status_prop.range == "xsd:string"
    assert status_prop.required is True


def test_role_classes():
    """Test role-based classes in case investigation"""
    config = CaseInvestigationConfig()

    # Test Attorney class
    attorney = config.classes["Attorney"]
    assert (
        attorney.uri == "https://ontology.caseontology.org/case/investigation/Attorney"
    )
    assert attorney.superclasses == ["core:Role"]
    assert "barNumber" in attorney.properties
    assert "jurisdiction" in attorney.properties

    # Test Examiner class
    examiner = config.classes["Examiner"]
    assert (
        examiner.uri == "https://ontology.caseontology.org/case/investigation/Examiner"
    )
    assert examiner.superclasses == ["core:Role"]
    assert "certification" in examiner.properties
    assert "examinerType" in examiner.properties


def test_lifecycle_classes():
    """Test lifecycle tracking classes"""
    config = CaseInvestigationConfig()

    # Test ExaminerActionLifecycle
    examiner_lifecycle = config.classes["ExaminerActionLifecycle"]
    assert examiner_lifecycle.superclasses == ["core:ActionLifecycle"]
    assert "examiner" in examiner_lifecycle.properties
    assert "toolsUsed" in examiner_lifecycle.properties

    # Test SubjectActionLifecycle
    subject_lifecycle = config.classes["SubjectActionLifecycle"]
    assert subject_lifecycle.superclasses == ["core:ActionLifecycle"]
    assert "subject" in subject_lifecycle.properties
    assert "actionType" in subject_lifecycle.properties
