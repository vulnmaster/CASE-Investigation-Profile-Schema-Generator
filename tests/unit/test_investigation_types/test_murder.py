import pytest

from case_investigation_schema_generator.investigation_types.murder_investigation import (
    MurderConfig,
)


def test_murder_config():
    """Test initialization and configuration of MurderConfig"""
    config = MurderConfig()

    # Test core classes are present
    assert "Investigation" in config.classes
    assert "UcoObject" in config.classes

    # Test core properties are present
    assert "createdBy" in config.properties
    assert "objectCreatedTime" in config.properties

    # Test murder specific properties
    investigation = config.classes["Investigation"]
    assert "physicalEvidence" in investigation.properties
    assert "investigativeActions" in investigation.properties


def test_murder_config_initialization():
    """Test initialization of MurderConfig"""
    config = MurderConfig()

    # Verify core classes are inherited
    assert "UcoObject" in config.classes
    assert "Investigation" in config.classes

    # Verify murder investigation specific classes
    assert "CrimeScene" in config.classes
    assert "PhysicalEvidence" in config.classes
    assert "VictimDevice" in config.classes
    assert "LocationHistory" in config.classes


def test_murder_class_properties():
    """Test properties of murder investigation classes"""
    config = MurderConfig()

    # Test PhysicalEvidence class
    phys_evidence = config.classes["PhysicalEvidence"]
    assert phys_evidence.name == "PhysicalEvidence"
    assert "evidenceType" in phys_evidence.properties
    assert "chainOfCustody" in phys_evidence.properties
    assert "collectionLocation" in phys_evidence.properties

    # Test CrimeScene class
    crime_scene = config.classes["CrimeScene"]
    assert crime_scene.name == "CrimeScene"
    assert "latitude" in crime_scene.properties
    assert "longitude" in crime_scene.properties
    assert "securitySystems" in crime_scene.properties


def test_murder_properties():
    """Test murder investigation specific properties"""
    config = MurderConfig()

    # Test evidence properties
    assert "evidenceType" in config.properties
    evidence_type_prop = config.properties["evidenceType"]
    assert evidence_type_prop.property_type == "DatatypeProperty"
    assert evidence_type_prop.range == "xsd:string"
    assert evidence_type_prop.required is True

    # Test location properties
    assert "locationTimestamp" in config.properties
    timestamp_prop = config.properties["locationTimestamp"]
    assert timestamp_prop.property_type == "DatatypeProperty"
    assert timestamp_prop.range == "xsd:dateTime"


def test_digital_evidence_mapping():
    """Test digital evidence mapping in murder investigations"""
    config = MurderConfig()

    # Test victim device class
    assert "VictimDevice" in config.classes
    victim_device = config.classes["VictimDevice"]
    assert (
        victim_device.uri
        == "https://ontology.unifiedcyberontology.org/uco/observable/Device"
    )
    assert "deviceType" in victim_device.properties
    assert "dataExtracted" in victim_device.properties

    # Test digital communication
    assert "DigitalCommunication" in config.classes
    digital_comm = config.classes["DigitalCommunication"]
    assert (
        digital_comm.uri
        == "https://ontology.unifiedcyberontology.org/uco/observable/Message"
    )
    assert "communicationType" in digital_comm.properties
    assert "content" in digital_comm.properties
