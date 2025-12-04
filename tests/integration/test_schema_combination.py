"""Integration tests for schema combination functionality"""

import pytest
from case_investigation_schema_generator import CaseSchemaGenerator, InvestigationType


def test_combine_cyber_and_murder():
    """Test combining cyber intrusion and murder investigation schemas"""
    generator = CaseSchemaGenerator()

    # Generate individual schemas
    cyber_schema = generator.generate_investigation_schema(
        InvestigationType.CYBER_INTRUSION
    )
    murder_schema = generator.generate_investigation_schema(InvestigationType.MURDER)

    # Verify unique properties from each schema
    assert "observables" in cyber_schema["properties"]
    assert "physicalEvidence" in murder_schema["properties"]

    # Verify common properties are consistent
    assert (
        cyber_schema["properties"]["createdBy"]
        == murder_schema["properties"]["createdBy"]
    )
    assert (
        cyber_schema["properties"]["modifiedTime"]
        == murder_schema["properties"]["modifiedTime"]
    )


def test_property_inheritance():
    """Test property inheritance in generated schemas"""
    generator = CaseSchemaGenerator()
    schema = generator.generate_investigation_schema(InvestigationType.CYBER_INTRUSION)

    # Check UcoObject properties are inherited
    uco_object = schema["definitions"]["core_UcoObject"]
    assert "properties" in uco_object
    assert "@id" in uco_object["properties"]
    assert "createdBy" in uco_object["properties"]

    # Check inheritance in cyber observables
    network_traffic = schema["definitions"]["investigation_InvestigativeAction"]
    assert "allOf" in network_traffic
    assert {"$ref": "#/definitions/core_UcoObject"} in network_traffic["allOf"]


def test_multiple_investigation_types():
    """Test handling multiple investigation types"""
    generator = CaseSchemaGenerator()

    # Generate schemas for all investigation types
    schemas = {
        inv_type: generator.generate_investigation_schema(inv_type)
        for inv_type in InvestigationType
    }

    # Verify each schema has its unique properties while maintaining core properties
    assert "@context" in schemas[InvestigationType.CYBER_INTRUSION]["properties"]
    assert "@id" in schemas[InvestigationType.MURDER]["properties"]
    assert "@type" in schemas[InvestigationType.CHILD_ABUSE]["properties"]
    assert "createdBy" in schemas[InvestigationType.INSIDER_THREAT]["properties"]

    # Verify core properties are consistent across all schemas
    base_props = ["@context", "createdBy", "modifiedTime", "name"]
    for schema in schemas.values():
        for prop in base_props:
            assert prop in schema["properties"]


def test_schema_structure_validity():
    """Test the structure of combined schemas"""
    generator = CaseSchemaGenerator()
    schema = generator.generate_investigation_schema(InvestigationType.CYBER_INTRUSION)

    # Verify schema has all required sections
    assert "$schema" in schema
    assert "type" in schema
    assert "properties" in schema
    assert "definitions" in schema
    assert "required" in schema

    # Verify schema version
    assert schema["$schema"] == "http://json-schema.org/draft-07/schema#"

    # Verify type
    assert schema["type"] == "object"

    # Verify required properties
    assert "@context" in schema["required"]

    # Verify definitions section
    assert "core_UcoObject" in schema["definitions"]
    assert "core_IdentityAbstraction" in schema["definitions"]
