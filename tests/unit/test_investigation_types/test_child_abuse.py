import pytest
from case_investigation_schema_generator.investigation_types.child_abuse_investigation import (
    ChildAbuseConfig,
)


def test_child_abuse_config():
    """Test initialization and configuration of ChildAbuseConfig"""
    config = ChildAbuseConfig()

    # Test core classes are present
    assert "Investigation" in config.classes
    assert "UcoObject" in config.classes

    # Test core properties are present
    assert "createdBy" in config.properties
    assert "objectCreatedTime" in config.properties

    # Test child abuse specific properties
    investigation = config.classes["Investigation"]
    assert "deviceEvidence" in investigation.properties
    assert "victimIdentification" in investigation.properties


def test_child_abuse_config_initialization():
    """Test initialization of ChildAbuseConfig"""
    config = ChildAbuseConfig()

    # Verify core classes are inherited
    assert "UcoObject" in config.classes
    assert "Investigation" in config.classes

    # Verify child abuse specific classes
    assert "CSAMEvidence" in config.classes
    assert "ChildVictim" in config.classes
    assert "OffenderDevice" in config.classes
    assert "CyberTipReport" in config.classes


def test_child_abuse_class_properties():
    """Test properties of child abuse investigation classes"""
    config = ChildAbuseConfig()

    # Test CSAM evidence class
    csam_evidence = config.classes["CSAMEvidence"]
    assert csam_evidence.name == "CSAMEvidence"
    assert "hashValue" in csam_evidence.properties
    assert "classification" in csam_evidence.properties
    assert "discoveryMethod" in csam_evidence.properties

    # Test online platform class
    platform = config.classes["OnlinePlatform"]
    assert platform.name == "OnlinePlatform"
    assert "platformType" in platform.properties
    assert "userAccounts" in platform.properties
    assert "contentFound" in platform.properties


def test_child_abuse_properties():
    """Test child abuse investigation specific properties"""
    config = ChildAbuseConfig()

    # Test CSAM properties
    assert "hashValue" in config.properties
    hash_prop = config.properties["hashValue"]
    assert hash_prop.property_type == "DatatypeProperty"
    assert hash_prop.range == "xsd:string"
    assert hash_prop.required is True

    # Test incident properties
    assert "incidentType" in config.properties
    incident_prop = config.properties["incidentType"]
    assert incident_prop.property_type == "DatatypeProperty"
    assert incident_prop.range == "xsd:string"
    assert incident_prop.required is True


def test_device_evidence_mapping():
    """Test device evidence mapping in child abuse investigations"""
    config = ChildAbuseConfig()

    # Test offender device class
    assert "OffenderDevice" in config.classes
    offender_device = config.classes["OffenderDevice"]
    assert (
        offender_device.uri
        == "https://ontology.unifiedcyberontology.org/uco/observable/Device"
    )
    assert "deviceType" in offender_device.properties
    assert "encryptionStatus" in offender_device.properties

    # Test digital communication class
    assert "DigitalCommunication" in config.classes
    digital_comm = config.classes["DigitalCommunication"]
    assert (
        digital_comm.uri
        == "https://ontology.unifiedcyberontology.org/uco/observable/Message"
    )
    assert "communicationType" in digital_comm.properties
    assert "content" in digital_comm.properties
