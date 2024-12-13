"""Validation tests for JSON Schema compliance"""

import pytest
import json
from jsonschema import validate, Draft7Validator, ValidationError
from case_investigation_schema_generator import CaseSchemaGenerator, InvestigationType

def test_json_schema_draft07():
    """Test schema compliance with JSON Schema Draft-07"""
    generator = CaseSchemaGenerator()
    schema = generator.generate_investigation_schema(InvestigationType.CYBER_INTRUSION)
    
    # Verify schema is valid Draft-07
    try:
        Draft7Validator.check_schema(schema)
    except Exception as e:
        pytest.fail(f"Schema is not valid Draft-07: {str(e)}")

def test_required_properties():
    """Test required properties validation"""
    generator = CaseSchemaGenerator()
    schema = generator.generate_investigation_schema(InvestigationType.CYBER_INTRUSION)

    # Add missing string definition
    schema["definitions"]["string"] = {
        "type": "string"
    }
    schema["definitions"]["xsd_dateTime"] = {
        "type": "string",
        "format": "date-time"
    }

    # Create a minimal valid instance with a finite depth
    valid_instance = {
        "@context": {
            "case": "https://ontology.caseontology.org/case/case",
            "investigation": "https://ontology.caseontology.org/case/investigation",
            "core": "https://ontology.unifiedcyberontology.org/uco/core",
            "vocabulary": "https://ontology.caseontology.org/case/vocabulary",
            "xsd": "http://www.w3.org/2001/XMLSchema#"
        },
        "@id": "investigation1",
        "@type": "Investigation",
        "name": "Test Investigation",
        "createdBy": {
            "@id": "investigator1",
            "@type": "core:IdentityAbstraction",
            "name": "Investigator One",
            "objectCreatedTime": "2024-03-20T12:00:00Z",
            "specVersion": "1.0.0",
            "createdBy": {
                "@id": "system1",
                "@type": "core:IdentityAbstraction",
                "name": "System Identity",
                "objectCreatedTime": "2024-03-20T12:00:00Z",
                "specVersion": "1.0.0",
                "createdBy": {
                    "@id": "system-root",
                    "@type": "core:IdentityAbstraction",
                    "name": "Root System",
                    "objectCreatedTime": "2024-03-20T12:00:00Z",
                    "specVersion": "1.0.0",
                    "createdBy": {
                        "@id": "system-root-creator",
                        "@type": "core:IdentityAbstraction",
                        "name": "Root System Creator",
                        "objectCreatedTime": "2024-03-20T12:00:00Z",
                        "specVersion": "1.0.0",
                        "createdBy": {
                            "@id": "system-root-creator",
                            "@type": "core:IdentityAbstraction",
                            "name": "Root System Creator",
                            "objectCreatedTime": "2024-03-20T12:00:00Z",
                            "specVersion": "1.0.0",
                            "createdBy": {
                                "@id": "system-root-creator",
                                "@type": "core:IdentityAbstraction",
                                "name": "Root System Creator",
                                "objectCreatedTime": "2024-03-20T12:00:00Z",
                                "specVersion": "1.0.0",
                                "createdBy": {
                                    "@id": "system-root-creator",
                                    "@type": "core:IdentityAbstraction",
                                    "objectCreatedTime": "2024-03-20T12:00:00Z",
                                    "specVersion": "1.0.0",
                                    "createdBy": {
                                        "@id": "system-root-creator",
                                        "@type": "core:IdentityAbstraction",
                                        "objectCreatedTime": "2024-03-20T12:00:00Z",
                                        "specVersion": "1.0.0"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "objectCreatedTime": "2024-03-20T12:00:00Z",
        "specVersion": "1.0.0"
    }

    # Test validation of required properties
    validate(instance=valid_instance, schema=schema)

    # Test missing required property
    invalid_instance = valid_instance.copy()
    del invalid_instance["@id"]
    with pytest.raises(ValidationError):
        validate(instance=invalid_instance, schema=schema)

def test_circular_reference_handling():
    """Test handling of circular references in identity objects"""
    generator = CaseSchemaGenerator()
    schema = generator.generate_investigation_schema(InvestigationType.CYBER_INTRUSION)

    # Add missing string definition
    schema["definitions"]["string"] = {
        "type": "string"
    }
    schema["definitions"]["xsd_dateTime"] = {
        "type": "string",
        "format": "date-time"
    }

    # Create an instance with a circular reference
    instance = {
        "@context": {
            "case": "https://ontology.caseontology.org/case/case",
            "investigation": "https://ontology.caseontology.org/case/investigation",
            "core": "https://ontology.unifiedcyberontology.org/uco/core",
            "vocabulary": "https://ontology.caseontology.org/case/vocabulary",
            "xsd": "http://www.w3.org/2001/XMLSchema#"
        },
        "@id": "investigation1",
        "@type": "Investigation",
        "name": "Test Investigation",
        "objectCreatedTime": "2024-03-20T12:00:00Z",
        "specVersion": "1.0.0",
        "createdBy": {
            "@id": "identity1",
            "@type": "core:IdentityAbstraction",
            "name": "Identity One",
            "objectCreatedTime": "2024-03-20T12:00:00Z",
            "specVersion": "1.0.0",
            "createdBy": {
                "@id": "identity2",
                "@type": "core:IdentityAbstraction",
                "name": "Identity Two",
                "objectCreatedTime": "2024-03-20T12:00:00Z",
                "specVersion": "1.0.0",
                "createdBy": {
                    "@id": "identity1",  # Circular reference back to identity1
                    "@type": "core:IdentityAbstraction",
                    "objectCreatedTime": "2024-03-20T12:00:00Z",
                    "specVersion": "1.0.0"
                }
            }
        }
    }

    # Test validation with circular reference
    validate(instance=instance, schema=schema)

    # Test that we can traverse the circular reference
    assert instance["createdBy"]["@id"] == "identity1"
    assert instance["createdBy"]["createdBy"]["@id"] == "identity2"
    assert instance["createdBy"]["createdBy"]["createdBy"]["@id"] == "identity1"

    # Test that required properties are maintained in circular reference
    assert instance["createdBy"]["createdBy"]["createdBy"]["@type"] == "core:IdentityAbstraction"
    assert instance["createdBy"]["createdBy"]["createdBy"]["objectCreatedTime"] == "2024-03-20T12:00:00Z"
    assert instance["createdBy"]["createdBy"]["createdBy"]["specVersion"] == "1.0.0"

def test_data_type_constraints():
    """Test data type constraints in schema"""
    generator = CaseSchemaGenerator()
    schema = generator.generate_investigation_schema(InvestigationType.CYBER_INTRUSION)
    
    # Test string properties
    string_props = ["@id", "@type", "name", "description"]
    for prop in string_props:
        if prop in schema["properties"]:
            assert schema["properties"][prop]["type"] == "string"
    
    # Test date-time properties
    datetime_props = ["modifiedTime", "objectCreatedTime"]
    for prop in datetime_props:
        if prop in schema["properties"] and "format" in schema["properties"][prop]:
            assert schema["properties"][prop]["format"] == "date-time"

def test_enum_values():
    """Test enumerated value constraints"""
    generator = CaseSchemaGenerator()
    schema = generator.generate_investigation_schema(InvestigationType.CYBER_INTRUSION)
    
    # Test @type property in definitions
    for def_name, definition in schema["definitions"].items():
        if "allOf" in definition:
            for part in definition["allOf"]:
                if "properties" in part and "@type" in part["properties"]:
                    type_prop = part["properties"]["@type"]
                    if "const" in type_prop:
                        assert isinstance(type_prop["const"], str)

def test_additional_properties():
    """Test additional properties constraints"""
    generator = CaseSchemaGenerator()
    schema = generator.generate_investigation_schema(InvestigationType.CYBER_INTRUSION)
    
    # Test context object
    context = schema["properties"]["@context"]
    assert "additionalProperties" not in context or not context["additionalProperties"]
    
    # Test main schema
    assert "additionalProperties" not in schema or not schema["additionalProperties"] 