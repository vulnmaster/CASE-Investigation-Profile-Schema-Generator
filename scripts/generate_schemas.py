#!/usr/bin/env python3
"""
Schema Generator Script

Generates JSON schemas for each investigation type and saves them to the schemas directory.
"""

import os
import json
from case_investigation_schema_generator import CaseSchemaGenerator, InvestigationType

def add_basic_definitions(schema):
    """Add basic type definitions to schema"""
    schema["definitions"].update({
        "string": {
            "type": "string"
        },
        "xsd_dateTime": {
            "type": "string",
            "format": "date-time"
        }
    })
    return schema

def main():
    """Generate schemas for all investigation types"""
    # Create schemas directory if it doesn't exist
    os.makedirs("schemas", exist_ok=True)
    
    generator = CaseSchemaGenerator()
    
    # Generate base investigation schema
    base_schema = generator.generate_investigation_schema(InvestigationType.CYBER_INTRUSION)
    base_schema = add_basic_definitions(base_schema)
    with open("schemas/base_investigation.json", "w") as f:
        json.dump(base_schema, f, indent=2)
    
    # Generate type-specific schemas
    for inv_type in InvestigationType:
        schema = generator.generate_investigation_schema(inv_type)
        schema = add_basic_definitions(schema)
        filename = f"schemas/{inv_type.value.lower()}_investigation.json"
        with open(filename, "w") as f:
            json.dump(schema, f, indent=2)
    
    print("Generated schemas:")
    print("- schemas/base_investigation.json")
    for inv_type in InvestigationType:
        print(f"- schemas/{inv_type.value.lower()}_investigation.json")

if __name__ == "__main__":
    main() 