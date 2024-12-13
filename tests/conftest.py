"""Test configuration and fixtures"""

from case_investigation_schema_generator.investigation_types.base_config import CaseClass, CaseProperty, BaseInvestigationType
import pytest

@pytest.fixture
def case_class():
    """Create a test CaseClass instance"""
    return CaseClass(
        name="TestClass",
        uri="https://example.org/test",
        description="Test class",
        superclasses=["UcoObject"],
        properties=["prop1", "prop2"]
    )

@pytest.fixture
def case_property():
    """Create a test CaseProperty instance"""
    return CaseProperty(
        name="testProp",
        uri="https://example.org/test/prop",
        description="Test property",
        property_type="string",
        range="xsd:string",
        required=True
    )

@pytest.fixture
def base_investigation_type():
    """Fixture providing a BaseInvestigationType instance"""
    return BaseInvestigationType() 