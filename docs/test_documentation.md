# Test Documentation

## Known Issues and Resolutions

### Schema Validation

#### 1. Circular Reference in Identity Objects
- **Issue**: Infinite recursion in schema validation due to required `createdBy` property
- **Resolution**: Modified schema to make `createdBy` optional in `core_UcoObject` while maintaining it in `core_IdentityAbstraction`. Used JSON-LD `@id` references for circular references.
- **Affected Tests**: `test_required_properties`, `test_circular_reference_handling`
- **Date Resolved**: March 20, 2024

#### 2. Class Hierarchy Preservation
- **Issue**: Breaking CASE ontology class hierarchy when fixing circular references
- **Resolution**: Restored proper inheritance through `allOf` in JSON Schema while keeping `createdBy` optional
- **Affected Tests**: `test_class_hierarchy`
- **Date Resolved**: March 20, 2024

### Data Conversion

#### 1. RDF Graph Validation
- **Issue**: Semantic preservation in JSON-RDF conversion
- **Resolution**: Implemented proper JSON-LD context and maintained CASE ontology URIs
- **Affected Tests**: `test_semantic_preservation`, `test_round_trip_conversion`
- **Date Resolved**: March 20, 2024

## Test Coverage History

### Latest Coverage Report (March 20, 2024)
- Overall Coverage: 100%
- Files: 9
- Lines: 147
- Missing: 0

## Test Execution Guidelines

### Running Tests
```bash
# Run all tests with coverage
pytest --cov=case_investigation_schema_generator tests/ -v

# Run specific test categories
pytest tests/unit/ -v
pytest tests/integration/ -v
pytest tests/validation/ -v
```

### Debugging Failed Tests
1. Check schema generation output in `tests/fixtures`
2. Verify CASE ontology compatibility
3. Review JSON Schema validation errors
4. Check RDF conversion output

## Adding New Tests

### Test Categories
1. Unit Tests: Add to appropriate file in `tests/unit/`
2. Integration Tests: Add to `tests/integration/`
3. Validation Tests: Add to `tests/validation/`

### Test Requirements
- Must include docstring explaining purpose
- Must verify CASE ontology compatibility
- Must check schema validation
- Must maintain coverage standards 