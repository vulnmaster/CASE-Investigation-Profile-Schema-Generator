# Test Plan: CASE Investigation Schema Generator

## Overview

This document outlines the testing strategy for the CASE Investigation Schema Generator. The test plan covers unit testing, integration testing, and validation testing to ensure the generated schemas are semantically compatible with the CASE ontology.

## Test Environment

### Requirements
- Python 3.7+
- pytest
- jsonschema validator
- RDF validator (for ontology compatibility)

### Setup
```bash
pip install pytest jsonschema rdflib
```

## Test Categories

### 1. Unit Tests

#### Base Configuration Tests
- [ ] Test CaseClass creation and validation
- [ ] Test CaseProperty creation and validation
- [ ] Test BaseInvestigationType initialization
- [ ] Test core properties loading

#### Schema Generator Tests
- [ ] Test schema generation base functionality
- [ ] Test JSON Schema compliance
- [ ] Test property inheritance
- [ ] Test schema combination

#### Investigation Type Tests

##### Cyber Intrusion
- [ ] Test STIX 2.1 mapping accuracy
- [ ] Validate cyber observable objects
- [ ] Test network artifact representations
- [ ] Verify attack pattern structures

##### Murder Investigation
- [ ] Test location data structures
- [ ] Validate evidence tracking
- [ ] Test digital device representation
- [ ] Verify surveillance data format

##### Child Abuse Investigation
- [ ] Test CSAM evidence handling
- [ ] Validate platform investigation structures
- [ ] Test communication analysis format
- [ ] Verify CyberTipline integration

##### Insider Threat Investigation
- [ ] Test data exfiltration monitoring
- [ ] Validate system misuse detection
- [ ] Test user behavior tracking
- [ ] Verify security alert structures

### 2. Integration Tests

#### Schema Combination Tests
- [ ] Test combining base schema with each investigation type
- [ ] Verify property inheritance in combined schemas
- [ ] Test multiple investigation type combinations
- [ ] Validate combined schema structure

#### CASE Ontology Compatibility
- [ ] Test URI resolution
- [ ] Verify class hierarchy preservation
- [ ] Test property range compatibility
- [ ] Validate semantic relationships

#### File Operations
- [ ] Test schema file generation
- [ ] Verify JSON formatting
- [ ] Test file naming conventions
- [ ] Validate file permissions

### 3. Validation Tests

#### Schema Validation
- [ ] Test against JSON Schema Draft-07
- [ ] Verify required properties
- [ ] Test data type constraints
- [ ] Validate enum values

#### Semantic Validation
- [ ] Test CASE ontology alignment
- [ ] Verify UCO core compatibility
- [ ] Test investigation namespace compliance
- [ ] Validate vocabulary usage

#### Data Conversion Tests
- [ ] Test JSON to RDF conversion
- [ ] Verify RDF graph validity
- [ ] Test round-trip conversion
- [ ] Validate semantic preservation

## Test Implementation

### Directory Structure
```
tests/
├── unit/
│   ├── test_base_config.py
│   ├── test_schema_generator.py
│   └── test_investigation_types/
│       ├── test_cyber_intrusion.py
│       ├── test_murder.py
│       ├── test_child_abuse.py
│       └── test_insider_threat.py
├── integration/
│   ├── test_schema_combination.py
│   ├── test_case_compatibility.py
│   └── test_file_operations.py
└── validation/
    ├── test_schema_validation.py
    ├── test_semantic_validation.py
    └── test_data_conversion.py
```

### Sample Test Case

```python
def test_cyber_intrusion_stix_mapping():
    """Test STIX 2.1 to CASE mapping in cyber intrusion schema"""
    generator = CaseSchemaGenerator()
    schema = generator.generate_investigation_schema(InvestigationType.CYBER_INTRUSION)
    
    # Verify STIX object mapping
    assert "definitions" in schema
    assert "observable_NetworkTraffic" in schema["definitions"]
    assert "observable_IPv4Address" in schema["definitions"]
    
    # Test property mapping
    network_traffic = schema["definitions"]["observable_NetworkTraffic"]
    assert "properties" in network_traffic
    assert "src_port" in network_traffic["properties"]
    assert "dst_port" in network_traffic["properties"]
```

## Test Execution

### Running Tests
```bash
# Run all tests
pytest

# Run specific test category
pytest tests/unit/
pytest tests/integration/
pytest tests/validation/

# Run with coverage
pytest --cov=investigation_types tests/
```

### Continuous Integration
- GitHub Actions workflow for automated testing
- Coverage reporting
- Linting checks
- Schema validation checks

## Success Criteria

1. All unit tests pass with 90%+ coverage
2. Integration tests verify schema combinations
3. Generated schemas validate against JSON Schema Draft-07
4. RDF conversion preserves all semantic relationships
5. CASE ontology compatibility verified

## Test Maintenance

1. Update tests when adding new investigation types
2. Maintain test data fixtures
3. Review and update test coverage regularly
4. Document test failures and resolutions

## Reporting

Generate test reports including:
1. Test coverage metrics
2. Failed test cases
3. Schema validation results
4. Semantic compatibility checks

## References

1. CASE Ontology Documentation
2. JSON Schema Specification
3. STIX 2.1 Specification
4. pytest Documentation
