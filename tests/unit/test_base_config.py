import pytest
from case_investigation_schema_generator.investigation_types.base_config import (
    CaseClass,
    CaseProperty,
    BaseInvestigationType,
)


def test_case_class_creation():
    """Test creation of CaseClass instances"""
    case_class = CaseClass(
        name="TestClass",
        uri="https://example.org/TestClass",
        description="A test class",
        superclasses=["SuperClass"],
        properties=["prop1", "prop2"],
    )
    assert case_class.name == "TestClass"
    assert case_class.uri == "https://example.org/TestClass"
    assert case_class.description == "A test class"
    assert case_class.superclasses == ["SuperClass"]
    assert case_class.properties == ["prop1", "prop2"]


def test_case_property_creation():
    """Test creation of CaseProperty instances"""
    case_property = CaseProperty(
        name="testProp",
        uri="https://example.org/testProp",
        description="A test property",
        property_type="DatatypeProperty",
        range="xsd:string",
        required=True,
    )
    assert case_property.name == "testProp"
    assert case_property.uri == "https://example.org/testProp"
    assert case_property.description == "A test property"
    assert case_property.property_type == "DatatypeProperty"
    assert case_property.range == "xsd:string"
    assert case_property.required is True


def test_base_investigation_type_initialization():
    """Test initialization of BaseInvestigationType"""
    base_type = BaseInvestigationType()
    assert isinstance(base_type.classes, dict)
    assert isinstance(base_type.properties, dict)
    assert "UcoObject" in base_type.classes
    assert "Investigation" in base_type.classes
    assert "createdBy" in base_type.properties
    assert "objectCreatedTime" in base_type.properties


def test_invalid_case_class():
    """Test that invalid CaseClass creation raises appropriate errors"""
    with pytest.raises(TypeError):
        CaseClass(
            name="",  # Empty name
            uri="https://example.org/TestClass",
            description="A test class",
            properties=[],  # Missing required superclasses parameter
        )


def test_invalid_case_property():
    """Test that invalid CaseProperty creation raises appropriate errors"""
    with pytest.raises(TypeError):
        CaseProperty(
            name="testProp",
            uri="invalid-uri",
            description="A test property",
            required=True,  # Missing required property_type parameter
        )
