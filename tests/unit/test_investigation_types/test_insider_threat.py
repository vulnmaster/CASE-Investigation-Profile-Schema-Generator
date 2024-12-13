import pytest
from case_investigation_schema_generator.investigation_types.insider_threat_investigation import InsiderThreatConfig

def test_insider_threat_config():
    """Test initialization and configuration of InsiderThreatConfig"""
    config = InsiderThreatConfig()
    
    # Test core classes are present
    assert "Investigation" in config.classes
    assert "UcoObject" in config.classes
    
    # Test core properties are present
    assert "createdBy" in config.properties
    assert "objectCreatedTime" in config.properties
    
    # Test insider threat specific properties
    investigation = config.classes["Investigation"]
    assert "systemMonitoring" in investigation.properties
    assert "userActivity" in investigation.properties

def test_insider_threat_config_initialization():
    """Test initialization of InsiderThreatConfig"""
    config = InsiderThreatConfig()
    
    # Verify core classes are inherited
    assert "UcoObject" in config.classes
    assert "Investigation" in config.classes
    
    # Verify insider threat specific classes
    assert "DataExfiltrationEvent" in config.classes
    assert "InsiderThreatActor" in config.classes
    assert "UserActivity" in config.classes
    assert "SecurityAlert" in config.classes

def test_insider_threat_class_properties():
    """Test properties of insider threat investigation classes"""
    config = InsiderThreatConfig()
    
    # Test data exfiltration class
    data_exfil = config.classes["DataExfiltrationEvent"]
    assert data_exfil.name == "DataExfiltrationEvent"
    assert "dataType" in data_exfil.properties
    assert "exfilMethod" in data_exfil.properties
    assert "detectionMethod" in data_exfil.properties
    
    # Test user activity class
    user_activity = config.classes["UserActivity"]
    assert user_activity.name == "UserActivity"
    assert "activityType" in user_activity.properties
    assert "timestamp" in user_activity.properties
    assert "resourcesAccessed" in user_activity.properties

def test_insider_threat_properties():
    """Test insider threat investigation specific properties"""
    config = InsiderThreatConfig()
    
    # Test threat properties
    assert "threatCategory" in config.properties
    threat_prop = config.properties["threatCategory"]
    assert threat_prop.property_type == "DatatypeProperty"
    assert threat_prop.range == "xsd:string"
    assert threat_prop.required is True
    
    # Test access control properties
    assert "accessLevel" in config.properties
    access_prop = config.properties["accessLevel"]
    assert access_prop.property_type == "DatatypeProperty"
    assert access_prop.range == "xsd:string"
    assert access_prop.required is True

def test_detection_tools():
    """Test detection tool aspects in insider threat investigations"""
    config = InsiderThreatConfig()
    
    # Test detection tool class
    assert "DetectionTool" in config.classes
    detection_tool = config.classes["DetectionTool"]
    assert detection_tool.uri == "https://ontology.unifiedcyberontology.org/uco/tool/Tool"
    assert "toolType" in detection_tool.properties
    assert "detectionCapabilities" in detection_tool.properties
    
    # Test security alert class
    assert "SecurityAlert" in config.classes
    security_alert = config.classes["SecurityAlert"]
    assert security_alert.uri == "https://ontology.unifiedcyberontology.org/uco/observable/ObservablePattern"
    assert "alertType" in security_alert.properties
    assert "severity" in security_alert.properties 