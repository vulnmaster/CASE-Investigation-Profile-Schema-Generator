"""Tests for JSON-RDF data conversion and semantic preservation"""

import pytest
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, XSD
import json
from case_investigation_schema_generator import CaseSchemaGenerator, InvestigationType

# Define namespaces
CASE = Namespace("https://ontology.caseontology.org/case/")
UCO_CORE = Namespace("https://ontology.unifiedcyberontology.org/uco/core/")
UCO_OBSERVABLE = Namespace("https://ontology.unifiedcyberontology.org/uco/observable/")

def create_test_instance():
    """Create a test investigation instance"""
    return {
        "@context": {
            "case": str(CASE),
            "investigation": str(CASE) + "investigation/",
            "core": str(UCO_CORE),
            "vocabulary": str(CASE) + "vocabulary/",
            "xsd": str(XSD)
        },
        "@id": "investigation1",
        "@type": "Investigation",
        "name": "Test Investigation",
        "createdBy": {
            "@id": "investigator1",
            "@type": "core:IdentityAbstraction",
            "name": "John Doe"
        },
        "objectCreatedTime": "2024-03-20T12:00:00Z",
        "specVersion": "1.0.0",
        "investigativeActions": [
            {
                "@id": "action1",
                "@type": "investigation:InvestigativeAction",
                "name": "Evidence Collection",
                "startTime": "2024-03-20T12:30:00Z",
                "endTime": "2024-03-20T13:30:00Z",
                "status": "Completed"
            }
        ]
    }

def json_to_rdf(json_data):
    """Convert JSON-LD like data to RDF"""
    g = Graph()
    
    # Bind namespaces
    g.bind("case", CASE)
    g.bind("core", UCO_CORE)
    g.bind("observable", UCO_OBSERVABLE)
    
    # Add main investigation
    inv_uri = URIRef(json_data["@id"])
    g.add((inv_uri, RDF.type, CASE.Investigation))
    g.add((inv_uri, CASE.name, Literal(json_data["name"])))
    
    # Add created by
    created_by = json_data["createdBy"]
    creator_uri = URIRef(created_by["@id"])
    g.add((inv_uri, UCO_CORE.createdBy, creator_uri))
    g.add((creator_uri, RDF.type, UCO_CORE.IdentityAbstraction))
    g.add((creator_uri, CASE.name, Literal(created_by["name"])))
    
    # Add timestamps
    g.add((inv_uri, UCO_CORE.objectCreatedTime, 
           Literal(json_data["objectCreatedTime"], datatype=XSD.dateTime)))
    
    # Add actions
    for action in json_data["investigativeActions"]:
        action_uri = URIRef(action["@id"])
        g.add((action_uri, RDF.type, CASE.InvestigativeAction))
        g.add((action_uri, CASE.name, Literal(action["name"])))
        g.add((action_uri, CASE.startTime, 
               Literal(action["startTime"], datatype=XSD.dateTime)))
        g.add((action_uri, CASE.endTime, 
               Literal(action["endTime"], datatype=XSD.dateTime)))
        g.add((action_uri, CASE.status, Literal(action["status"])))
        g.add((inv_uri, CASE.investigativeActions, action_uri))
    
    return g

def test_json_to_rdf_conversion():
    """Test conversion from JSON to RDF"""
    # Create test instance
    json_data = create_test_instance()
    
    # Convert to RDF
    g = json_to_rdf(json_data)
    
    # Verify basic graph properties
    assert len(g) > 0, "Graph should not be empty"
    
    # Verify investigation type
    inv_uri = URIRef("investigation1")
    assert (inv_uri, RDF.type, CASE.Investigation) in g
    
    # Verify creator
    creator_uri = URIRef("investigator1")
    assert (inv_uri, UCO_CORE.createdBy, creator_uri) in g
    assert (creator_uri, RDF.type, UCO_CORE.IdentityAbstraction) in g

def test_rdf_graph_validity():
    """Test validity of generated RDF graph"""
    json_data = create_test_instance()
    g = json_to_rdf(json_data)
    
    # Test required triples
    inv_uri = URIRef("investigation1")
    required_predicates = [
        RDF.type,
        CASE.name,
        UCO_CORE.createdBy,
        UCO_CORE.objectCreatedTime
    ]
    
    for pred in required_predicates:
        assert any(g.triples((inv_uri, pred, None))), f"Missing required predicate: {pred}"

def test_round_trip_conversion():
    """Test round-trip conversion (JSON -> RDF -> JSON)"""
    original_json = create_test_instance()
    
    # Convert to RDF
    g = json_to_rdf(original_json)
    
    # Convert back to JSON-like structure
    inv_uri = URIRef("investigation1")
    reconstructed = {
        "@context": original_json["@context"],
        "@id": str(inv_uri),
        "@type": "Investigation",
        "name": str(next(g.objects(inv_uri, CASE.name))),
        "createdBy": {
            "@id": str(next(g.objects(inv_uri, UCO_CORE.createdBy))),
            "@type": "core:IdentityAbstraction"
        },
        "objectCreatedTime": str(next(g.objects(inv_uri, UCO_CORE.objectCreatedTime)))
    }
    
    # Compare essential properties
    assert reconstructed["@id"] == original_json["@id"]
    assert reconstructed["name"] == original_json["name"]
    # Compare timestamps ignoring timezone format differences
    assert reconstructed["objectCreatedTime"].replace("+00:00", "Z") == original_json["objectCreatedTime"]

def test_semantic_preservation():
    """Test preservation of semantic relationships"""
    json_data = create_test_instance()
    g = json_to_rdf(json_data)
    
    # Test investigation-action relationship
    inv_uri = URIRef("investigation1")
    action_uri = URIRef("action1")
    
    # Verify action relationship
    assert (inv_uri, CASE.investigativeActions, action_uri) in g
    
    # Verify action properties
    assert (action_uri, RDF.type, CASE.InvestigativeAction) in g
    assert (action_uri, CASE.startTime, None) in g
    assert (action_uri, CASE.endTime, None) in g
    assert (action_uri, CASE.status, Literal("Completed")) in g 