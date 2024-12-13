"""Integration tests for CASE ontology compatibility"""

import pytest
from rdflib import Graph, URIRef, Namespace
from case_investigation_schema_generator import CaseSchemaGenerator, InvestigationType

# Constants for namespace URIs
CASE = "https://ontology.caseontology.org/case/case"
UCO_CORE = "https://ontology.unifiedcyberontology.org/uco/core"
INVESTIGATION = "https://ontology.caseontology.org/case/investigation"

def test_uri_resolution():
    """Test URI resolution and namespace consistency"""
    generator = CaseSchemaGenerator()
    schema = generator.generate_investigation_schema(InvestigationType.CYBER_INTRUSION)
    
    # Check context URIs match CASE/UCO namespaces
    context = schema["properties"]["@context"]["properties"]
    assert context["case"]["const"] == CASE
    assert context["core"]["const"] == UCO_CORE
    assert context["investigation"]["const"] == INVESTIGATION
    
    # Check class URIs
    definitions = schema["definitions"]
    assert "core_UcoObject" in definitions
    assert "investigation_InvestigativeAction" in definitions

def test_class_hierarchy():
    """Test preservation of CASE/UCO class hierarchy"""
    generator = CaseSchemaGenerator()
    schema = generator.generate_investigation_schema(InvestigationType.CYBER_INTRUSION)
    
    # Check UcoObject is parent of all classes
    for class_def in schema["definitions"].values():
        if "allOf" in class_def:
            refs = [ref.get("$ref", "") for ref in class_def["allOf"]]
            assert any("#/definitions/core_UcoObject" in ref for ref in refs)
    
    # Check specific inheritance chains
    investigative_action = schema["definitions"]["investigation_InvestigativeAction"]
    assert {"$ref": "#/definitions/core_UcoObject"} in investigative_action["allOf"]

def test_property_range_compatibility():
    """Test property range compatibility with CASE/UCO"""
    generator = CaseSchemaGenerator()
    schema = generator.generate_investigation_schema(InvestigationType.CYBER_INTRUSION)
    
    # Check core property ranges
    props = schema["properties"]
    assert props["createdBy"]["$ref"] == "#/definitions/core_IdentityAbstraction"
    assert props["modifiedTime"]["$ref"] == "#/definitions/xsd_dateTime"
    
    # Check investigation-specific property ranges
    observables = props["observables"]["items"]["allOf"]
    assert any("core_UcoObject" in str(ref) for ref in observables)

def test_semantic_relationships():
    """Test semantic relationship preservation"""
    generator = CaseSchemaGenerator()
    schema = generator.generate_investigation_schema(InvestigationType.CYBER_INTRUSION)
    
    # Check relationship properties in definitions
    defs = schema["definitions"]
    
    # Check UcoObject relationships
    uco_object = defs["core_UcoObject"]
    assert "createdBy" in uco_object["properties"]
    assert "modifiedTime" in uco_object["properties"]
    
    # Check investigation action relationships
    action = defs["investigation_InvestigativeAction"]
    action_props = action["allOf"][1]["properties"]
    assert "startTime" in action_props
    assert "endTime" in action_props
    assert "status" in action_props

def test_vocabulary_compatibility():
    """Test compatibility with CASE vocabulary terms"""
    generator = CaseSchemaGenerator()
    schema = generator.generate_investigation_schema(InvestigationType.CYBER_INTRUSION)
    
    # Check vocabulary namespace in context
    context = schema["properties"]["@context"]["properties"]
    assert "vocabulary" in context
    assert context["vocabulary"]["const"] == "https://ontology.caseontology.org/case/vocabulary"
    
    # Check vocabulary terms in properties
    defs = schema["definitions"]
    if "investigation_InvestigativeAction" in defs:
        action = defs["investigation_InvestigativeAction"]
        action_props = action["allOf"][1]["properties"]
        assert "status" in action_props  # Investigation status vocabulary 