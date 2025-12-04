import pytest

from case_investigation_schema_generator.investigation_types.cyber_intrusion import (
    CyberIntrusionConfig,
)


def test_cyber_intrusion_config():
    """Test initialization and configuration of CyberIntrusionConfig"""
    config = CyberIntrusionConfig()

    # Test core classes are present
    assert "Investigation" in config.classes
    assert "UcoObject" in config.classes

    # Test core properties are present
    assert "createdBy" in config.properties
    assert "objectCreatedTime" in config.properties

    # Test cyber intrusion specific properties
    investigation = config.classes["Investigation"]
    assert "observables" in investigation.properties
    assert "investigativeActions" in investigation.properties


def test_cyber_intrusion_config_initialization():
    """Test initialization of CyberIntrusionConfig"""
    config = CyberIntrusionConfig()

    # Verify core classes are inherited
    assert "UcoObject" in config.classes
    assert "Investigation" in config.classes

    # Verify cyber intrusion specific classes
    assert "NetworkTraffic" in config.classes
    assert "File" in config.classes
    assert "EmailMessage" in config.classes
    assert "AttackPattern" in config.classes


def test_cyber_intrusion_class_properties():
    """Test properties of cyber intrusion classes"""
    config = CyberIntrusionConfig()

    # Test NetworkTraffic class
    network_traffic = config.classes["NetworkTraffic"]
    assert network_traffic.name == "NetworkTraffic"
    assert "src_port" in network_traffic.properties
    assert "dst_port" in network_traffic.properties
    assert "protocols" in network_traffic.properties

    # Test File class
    file_class = config.classes["File"]
    assert file_class.name == "File"
    assert "hashes" in file_class.properties
    assert "mime_type" in file_class.properties
    assert "size" in file_class.properties


def test_cyber_intrusion_properties():
    """Test cyber intrusion specific properties"""
    config = CyberIntrusionConfig()

    # Test common properties
    assert "type" in config.properties
    type_prop = config.properties["type"]
    assert type_prop.property_type == "DatatypeProperty"
    assert type_prop.range == "xsd:string"
    assert type_prop.required is True

    # Test hash property
    assert "hashes" in config.properties
    hash_prop = config.properties["hashes"]
    assert hash_prop.property_type == "ObjectProperty"
    assert hash_prop.range == "observable:Hash"


def test_stix_mapping():
    """Test STIX to CASE mapping"""
    config = CyberIntrusionConfig()

    # Test STIX object mappings
    assert "NetworkTraffic" in config.classes
    network_traffic = config.classes["NetworkTraffic"]
    assert (
        network_traffic.uri
        == "https://ontology.unifiedcyberontology.org/uco/observable/NetworkTraffic"
    )
    assert "src_ref" in network_traffic.properties
    assert "dst_ref" in network_traffic.properties

    # Test STIX indicator mapping
    assert "Indicator" in config.classes
    indicator = config.classes["Indicator"]
    assert (
        indicator.uri
        == "https://ontology.caseontology.org/case/investigation/Indicator"
    )
    assert "pattern" in indicator.properties
    assert "pattern_type" in indicator.properties
