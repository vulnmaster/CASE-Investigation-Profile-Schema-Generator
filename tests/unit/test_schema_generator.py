"""Unit tests for schema generator"""

import os
import json
import pytest
from case_investigation_schema_generator import CaseSchemaGenerator, InvestigationType


def test_schema_generator_initialization():
    """Test initialization of CaseSchemaGenerator"""
    generator = CaseSchemaGenerator()
    assert generator.investigation_configs is not None
    assert InvestigationType.CYBER_INTRUSION in generator.investigation_configs
    assert InvestigationType.MURDER in generator.investigation_configs
    assert InvestigationType.CHILD_ABUSE in generator.investigation_configs
    assert InvestigationType.INSIDER_THREAT in generator.investigation_configs


def test_generate_base_definitions():
    """Test generation of base schema definitions"""
    generator = CaseSchemaGenerator()
    definitions = generator._generate_base_definitions()

    # Verify core definitions exist
    assert "core_UcoObject" in definitions
    assert "core_IdentityAbstraction" in definitions
    assert "investigation_InvestigativeAction" in definitions

    # Verify UcoObject structure
    uco_object = definitions["core_UcoObject"]
    assert uco_object["type"] == "object"
    assert "properties" in uco_object
    assert "@id" in uco_object["properties"]
    assert "@type" in uco_object["properties"]
    assert "createdBy" in uco_object["properties"]


def test_generate_cyber_intrusion_schema():
    """Test generation of cyber intrusion investigation schema"""
    generator = CaseSchemaGenerator()
    schema = generator.generate_investigation_schema(InvestigationType.CYBER_INTRUSION)

    # Verify schema structure
    assert "$schema" in schema
    assert "type" in schema
    assert "properties" in schema
    assert "@context" in schema["properties"]

    # Verify cyber intrusion specific properties
    properties = schema["properties"]
    assert "investigativeActions" in properties
    assert "observables" in properties
    assert "subjects" in properties


def test_schema_context():
    """Test schema @context generation"""
    generator = CaseSchemaGenerator()
    schema = generator.generate_investigation_schema(InvestigationType.CYBER_INTRUSION)

    context = schema["properties"]["@context"]
    assert context["type"] == "object"
    assert "properties" in context

    # Verify required namespaces
    context_props = context["properties"]
    assert "case" in context_props
    assert "investigation" in context_props
    assert "core" in context_props
    assert "vocabulary" in context_props
    assert "xsd" in context_props


def test_required_properties():
    """Test that required properties are correctly specified"""
    generator = CaseSchemaGenerator()
    schema = generator.generate_investigation_schema(InvestigationType.CYBER_INTRUSION)

    # Verify required properties are listed
    assert "required" in schema
    required_props = schema["required"]
    assert "@context" in required_props
    assert "@id" in required_props
    assert "@type" in required_props
    assert "createdBy" in required_props
    assert "objectCreatedTime" in required_props


def test_all_investigation_types():
    """Test schema generation for all investigation types"""
    generator = CaseSchemaGenerator()

    # Test each investigation type
    for inv_type in InvestigationType:
        schema = generator.generate_investigation_schema(inv_type)
        assert schema is not None
        assert "properties" in schema
        assert "@context" in schema["properties"]
        assert "required" in schema


def test_murder_investigation_schema():
    """Test generation of murder investigation schema"""
    generator = CaseSchemaGenerator()
    schema = generator.generate_investigation_schema(InvestigationType.MURDER)

    # Verify murder-specific properties
    properties = schema["properties"]
    assert "investigativeActions" in properties
    assert "physicalEvidence" in properties
    assert (
        properties["physicalEvidence"]["items"]["allOf"][1]["properties"]["@type"][
            "const"
        ]
        == "case:PhysicalEvidence"
    )


def test_child_abuse_investigation_schema():
    """Test generation of child abuse investigation schema"""
    generator = CaseSchemaGenerator()
    schema = generator.generate_investigation_schema(InvestigationType.CHILD_ABUSE)

    # Verify child abuse specific properties
    properties = schema["properties"]
    assert "investigativeActions" in properties
    assert "digitalEvidence" in properties
    assert (
        properties["digitalEvidence"]["items"]["allOf"][1]["properties"]["@type"][
            "const"
        ]
        == "case:DigitalEvidence"
    )


def test_insider_threat_investigation_schema():
    """Test generation of insider threat investigation schema"""
    generator = CaseSchemaGenerator()
    schema = generator.generate_investigation_schema(InvestigationType.INSIDER_THREAT)

    # Verify insider threat specific properties
    properties = schema["properties"]
    assert "investigativeActions" in properties
    assert "systemMonitoring" in properties
    assert (
        properties["systemMonitoring"]["items"]["allOf"][1]["properties"]["@type"][
            "const"
        ]
        == "case:SystemMonitoring"
    )


def test_save_schema(tmp_path):
    """Test saving schema to file"""
    generator = CaseSchemaGenerator()
    schema = generator.generate_investigation_schema(InvestigationType.CYBER_INTRUSION)

    # Create a temporary file path
    schema_file = tmp_path / "test_schema.json"

    # Save the schema
    generator.save_schema(schema, str(schema_file))

    # Verify file exists and contains valid JSON
    assert os.path.exists(schema_file)
    with open(schema_file) as f:
        loaded_schema = json.load(f)

    # Verify schema content
    assert loaded_schema == schema


def test_schema_property_references():
    """Test schema property references are correctly formatted"""
    generator = CaseSchemaGenerator()
    schema = generator.generate_investigation_schema(InvestigationType.MURDER)

    # Test property with colon in range (replaced with underscore)
    createdBy = schema["properties"]["createdBy"]
    assert createdBy["$ref"] == "#/definitions/core_IdentityAbstraction"

    # Test property with colon in range (replaced with underscore)
    modifiedTime = schema["properties"]["modifiedTime"]
    assert modifiedTime["$ref"] == "#/definitions/xsd_dateTime"

    # Test property without colon in range
    name = schema["properties"]["name"]
    assert name["$ref"] == "#/definitions/string"

    # Test nested property without range
    physicalEvidence = schema["properties"]["physicalEvidence"]
    evidenceType = physicalEvidence["items"]["allOf"][1]["properties"]["evidenceType"]
    assert evidenceType["type"] == "string"
