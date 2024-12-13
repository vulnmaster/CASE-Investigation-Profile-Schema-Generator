# CASE Investigation Schema Generator

A Python-based tool for generating JSON schemas that are semantically compatible with the Cyber-investigation Automation Standardization Encapsulation (CASE) ontology. This tool supports different types of investigations and ensures proper mapping between domain-specific schemas and the CASE ontology.

## Features

- Generate JSON schemas for different investigation types
- Maintain semantic compatibility with CASE/UCO ontology
- Support multiple investigation types:
  - Cyber Intrusion (with STIX 2.1 mapping)
  - Murder (physical and digital evidence)
  - Child Abuse (including CSAM tracking)
  - Insider Threat (data exfiltration monitoring)
- Enable lossless conversion between JSON and RDF formats
- Preserve traceability to CASE ontology

## Requirements

- Python 3.7+
- Required packages:
  ```bash
  pip install typing dataclasses
  ```

## Project Structure

```
case-schema-generator/
├── investigation_types/
│   ├── __init__.py
│   ├── base_config.py              # Base classes and properties
│   ├── case_investigation.py       # Core CASE investigation schema
│   ├── cyber_intrusion.py         # Cyber intrusion (STIX mapping)
│   ├── murder_investigation.py    # Murder investigation
│   ├── child_abuse_investigation.py # Child abuse cases
│   └── insider_threat_investigation.py # Insider threats
├── investigation_schema_generator.py
└── example_usage.py
```

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/yourusername/case-schema-generator.git
cd case-schema-generator
```

2. Generate schemas:
```python
from investigation_schema_generator import CaseSchemaGenerator, InvestigationType
from investigation_types.case_investigation import CaseInvestigationConfig as OptionalCaseInvestigationConfig

# Create generator instance
generator = CaseSchemaGenerator()

# Generate base investigation schema
investigation_schema = generator.generate_investigation_schema(CaseInvestigationConfig())

# Generate specific investigation type schema
cyber_schema = generator.generate_investigation_schema(InvestigationType.CYBER_INTRUSION)

# Combine schemas
combined_schema = {
    **investigation_schema,
    "definitions": {
        **investigation_schema["definitions"],
        **cyber_schema["definitions"]
    }
}

# Save schema
generator.save_schema(combined_schema, "combined_schema.json")
```

## Investigation Types

### Core Investigation Schema
- Maps core CASE investigation classes
- Provides base properties for all investigations
- Includes standard investigative actions

### Cyber Intrusion
- Maps STIX 2.1 objects to CASE
- Supports network artifacts
- Includes attack patterns and indicators

### Murder Investigation
- Supports physical and digital evidence
- Location tracking and correlation
- Communication analysis
- Surveillance data integration

### Child Abuse Investigation
- CSAM tracking and analysis
- Online platform investigation
- Digital communication analysis
- CyberTipline integration

### Insider Threat Investigation
- Data exfiltration monitoring
- System misuse detection
- User behavior analysis
- Security alert tracking

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Adding New Investigation Types

1. Create a new configuration file in `investigation_types/`
2. Extend `BaseInvestigationType`
3. Map domain concepts to CASE classes
4. Register in `investigation_schema_generator.py`

## License

This project is licensed under the Apache 2 License by the Linux Foundation's Cyber Domain Ontology Project - see the LICENSE file for details.

## Acknowledgments

- CASE Ontology Community
- UCO (Unified Cyber Ontology)
- STIX 2.1 Specification

## Testing and Quality Assurance

### Running Tests

To run the test suite:

```bash
# Install test dependencies
pip install -r requirements-test.txt

# Run tests with coverage
pytest --cov=case_investigation_schema_generator tests/ -v

# Generate detailed test report
./scripts/generate_test_report.py
```

### Test Documentation

Test documentation, including known issues and resolutions, can be found in [docs/test_documentation.md](docs/test_documentation.md).

### Continuous Integration

This project uses GitHub Actions for continuous integration. The following checks are performed on each push and pull request:
- Test execution across Python versions 3.8-3.12
- Code coverage reporting
- Code formatting (black)
- Import sorting (isort)
- Linting (flake8)

### Test Reports

Test reports are generated in two formats:
1. JSON reports in the `reports/` directory
2. HTML coverage reports in the `coverage/` directory

To view the latest coverage report, open `coverage/index.html` in your browser after running the tests.