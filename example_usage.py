"""
Example Usage of CASE Investigation Schema Generator

This module demonstrates how to use the schema generator for different investigation types
and how to combine investigation-specific schemas with the core CASE investigation schema.

Examples include:
1. Generating basic investigation schemas
2. Creating investigation type specific schemas
3. Combining schemas for comprehensive coverage
4. Saving schemas to files
"""

from investigation_schema_generator import CaseSchemaGenerator, InvestigationType
from investigation_types.case_investigation import CaseInvestigationConfig

def generate_basic_schema():
    """Generate a basic CASE investigation schema"""
    generator = CaseSchemaGenerator()
    investigation_schema = generator.generate_investigation_schema(CaseInvestigationConfig())
    generator.save_schema(investigation_schema, "basic_investigation_schema.json")

def generate_cyber_intrusion_schema():
    """Generate a cyber intrusion specific schema"""
    generator = CaseSchemaGenerator()
    cyber_schema = generator.generate_investigation_schema(InvestigationType.CYBER_INTRUSION)
    generator.save_schema(cyber_schema, "cyber_intrusion_schema.json")

def generate_combined_schema():
    """Generate a combined schema with base investigation and specific type"""
    generator = CaseSchemaGenerator()
    
    # Generate base investigation schema
    investigation_schema = generator.generate_investigation_schema(CaseInvestigationConfig())
    
    # Generate specific investigation type schema
    murder_schema = generator.generate_investigation_schema(InvestigationType.MURDER)
    
    # Combine schemas
    combined_schema = {
        **investigation_schema,
        "definitions": {
            **investigation_schema["definitions"],
            **murder_schema["definitions"]
        }
    }
    
    generator.save_schema(combined_schema, "combined_murder_schema.json")

if __name__ == "__main__":
    # Example usage
    generate_basic_schema()
    generate_cyber_intrusion_schema()
    generate_combined_schema() 