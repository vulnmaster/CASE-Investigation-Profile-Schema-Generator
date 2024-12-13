#!/usr/bin/env python3
"""
Example Generator Script

Generates example JSONL files with data conforming to each investigation type schema.
Also validates the generated examples against their respective schemas.
"""

import os
import json
import jsonschema
from datetime import datetime, timedelta
from typing import Dict, List

def load_schema(schema_path: str) -> Dict:
    """Load a JSON schema from file"""
    with open(schema_path) as f:
        return json.load(f)

def generate_cyber_intrusion_examples() -> List[Dict]:
    """Generate example cyber intrusion investigations"""
    timestamp = datetime.now().isoformat()
    return [
        {
            "@context": {
                "case": "https://ontology.caseontology.org/case/case",
                "investigation": "https://ontology.caseontology.org/case/investigation",
                "core": "https://ontology.unifiedcyberontology.org/uco/core",
                "vocabulary": "https://ontology.caseontology.org/case/vocabulary",
                "xsd": "http://www.w3.org/2001/XMLSchema#"
            },
            "@id": "investigation-1",
            "@type": "Investigation",
            "name": "APT29 Intrusion Investigation",
            "description": "Investigation of suspected APT29 intrusion",
            "createdBy": {
                "@id": "investigator-1",
                "@type": "core:IdentityAbstraction",
                "name": "John Smith",
                "objectCreatedTime": timestamp,
                "specVersion": "1.0.0"
            },
            "objectCreatedTime": timestamp,
            "specVersion": "1.0.0",
            "investigativeActions": [
                {
                    "@id": "action-1",
                    "@type": "investigation:InvestigativeAction",
                    "name": "Network Traffic Analysis",
                    "description": "Analysis of suspicious network traffic",
                    "startTime": (datetime.now() - timedelta(hours=2)).isoformat(),
                    "endTime": (datetime.now() - timedelta(hours=1)).isoformat(),
                    "status": "Completed",
                    "objectCreatedTime": timestamp,
                    "specVersion": "1.0.0"
                }
            ],
            "observables": [
                {
                    "@id": "observable-1",
                    "@type": "observable:CyberItem",
                    "name": "Suspicious Network Connection",
                    "observableType": "NetworkTraffic",
                    "hasChanged": False,
                    "state": "Observed",
                    "objectCreatedTime": timestamp,
                    "specVersion": "1.0.0"
                }
            ]
        }
    ]

def generate_murder_examples() -> List[Dict]:
    """Generate example murder investigations"""
    timestamp = datetime.now().isoformat()
    return [
        {
            "@context": {
                "case": "https://ontology.caseontology.org/case/case",
                "investigation": "https://ontology.caseontology.org/case/investigation",
                "core": "https://ontology.unifiedcyberontology.org/uco/core",
                "vocabulary": "https://ontology.caseontology.org/case/vocabulary",
                "xsd": "http://www.w3.org/2001/XMLSchema#"
            },
            "@id": "investigation-2",
            "@type": "Investigation",
            "name": "Downtown Homicide Investigation",
            "description": "Investigation of homicide at 123 Main St",
            "createdBy": {
                "@id": "investigator-2",
                "@type": "core:IdentityAbstraction",
                "name": "Jane Doe",
                "objectCreatedTime": timestamp,
                "specVersion": "1.0.0"
            },
            "objectCreatedTime": timestamp,
            "specVersion": "1.0.0",
            "investigativeActions": [
                {
                    "@id": "action-2",
                    "@type": "investigation:InvestigativeAction",
                    "name": "Crime Scene Processing",
                    "description": "Initial crime scene documentation and evidence collection",
                    "startTime": (datetime.now() - timedelta(days=1)).isoformat(),
                    "endTime": (datetime.now() - timedelta(hours=20)).isoformat(),
                    "status": "Completed",
                    "objectCreatedTime": timestamp,
                    "specVersion": "1.0.0"
                }
            ],
            "physicalEvidence": [
                {
                    "@id": "evidence-1",
                    "@type": "case:PhysicalEvidence",
                    "name": "Weapon",
                    "evidenceType": "Knife",
                    "location": "Kitchen",
                    "condition": "Intact",
                    "objectCreatedTime": timestamp,
                    "specVersion": "1.0.0"
                }
            ]
        }
    ]

def generate_child_abuse_examples() -> List[Dict]:
    """Generate example child abuse investigations"""
    timestamp = datetime.now().isoformat()
    return [
        {
            "@context": {
                "case": "https://ontology.caseontology.org/case/case",
                "investigation": "https://ontology.caseontology.org/case/investigation",
                "core": "https://ontology.unifiedcyberontology.org/uco/core",
                "vocabulary": "https://ontology.caseontology.org/case/vocabulary",
                "xsd": "http://www.w3.org/2001/XMLSchema#"
            },
            "@id": "investigation-3",
            "@type": "Investigation",
            "name": "CyberTipline Report Investigation",
            "description": "Investigation based on NCMEC CyberTipline Report #12345",
            "createdBy": {
                "@id": "investigator-3",
                "@type": "core:IdentityAbstraction",
                "name": "Sarah Johnson",
                "objectCreatedTime": timestamp,
                "specVersion": "1.0.0"
            },
            "objectCreatedTime": timestamp,
            "specVersion": "1.0.0",
            "investigativeActions": [
                {
                    "@id": "action-3",
                    "@type": "investigation:InvestigativeAction",
                    "name": "Digital Device Analysis",
                    "description": "Forensic analysis of seized devices",
                    "startTime": (datetime.now() - timedelta(days=2)).isoformat(),
                    "endTime": (datetime.now() - timedelta(days=1)).isoformat(),
                    "status": "Completed",
                    "objectCreatedTime": timestamp,
                    "specVersion": "1.0.0"
                }
            ],
            "digitalEvidence": [
                {
                    "@id": "evidence-3",
                    "@type": "case:DigitalEvidence",
                    "name": "Image File",
                    "evidenceType": "CSAM",
                    "hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
                    "classification": "Category 1",
                    "objectCreatedTime": timestamp,
                    "specVersion": "1.0.0"
                }
            ],
            "victimIdentification": {
                "@id": "victim-1",
                "@type": "core:Identity",
                "name": "Protected Identity",
                "objectCreatedTime": timestamp,
                "specVersion": "1.0.0"
            }
        }
    ]

def generate_insider_threat_examples() -> List[Dict]:
    """Generate example insider threat investigations"""
    timestamp = datetime.now().isoformat()
    return [
        {
            "@context": {
                "case": "https://ontology.caseontology.org/case/case",
                "investigation": "https://ontology.caseontology.org/case/investigation",
                "core": "https://ontology.unifiedcyberontology.org/uco/core",
                "vocabulary": "https://ontology.caseontology.org/case/vocabulary",
                "xsd": "http://www.w3.org/2001/XMLSchema#"
            },
            "@id": "investigation-4",
            "@type": "Investigation",
            "name": "Data Exfiltration Investigation",
            "description": "Investigation of unauthorized data transfer by employee",
            "createdBy": {
                "@id": "investigator-4",
                "@type": "core:IdentityAbstraction",
                "name": "Michael Chen",
                "objectCreatedTime": timestamp,
                "specVersion": "1.0.0"
            },
            "objectCreatedTime": timestamp,
            "specVersion": "1.0.0",
            "investigativeActions": [
                {
                    "@id": "action-4",
                    "@type": "investigation:InvestigativeAction",
                    "name": "Network Log Analysis",
                    "description": "Analysis of network traffic logs for data exfiltration",
                    "startTime": (datetime.now() - timedelta(hours=12)).isoformat(),
                    "endTime": (datetime.now() - timedelta(hours=8)).isoformat(),
                    "status": "Completed",
                    "objectCreatedTime": timestamp,
                    "specVersion": "1.0.0"
                }
            ],
            "systemMonitoring": [
                {
                    "@id": "monitoring-1",
                    "@type": "case:SystemMonitoring",
                    "name": "Large File Transfer Alert",
                    "monitoringType": "DataTransfer",
                    "timestamp": (datetime.now() - timedelta(hours=10)).isoformat(),
                    "activity": "Upload of 2GB file to external storage",
                    "objectCreatedTime": timestamp,
                    "specVersion": "1.0.0"
                }
            ],
            "userActivity": [
                {
                    "@id": "activity-1",
                    "@type": "case:UserActivity",
                    "name": "Suspicious Login",
                    "activityType": "Authentication",
                    "timestamp": (datetime.now() - timedelta(hours=11)).isoformat(),
                    "description": "Off-hours system access from unusual location",
                    "objectCreatedTime": timestamp,
                    "specVersion": "1.0.0"
                }
            ]
        }
    ]

def validate_examples(examples: List[Dict], schema: Dict):
    """Validate examples against their schema"""
    validator = jsonschema.Draft7Validator(schema)
    for i, example in enumerate(examples, 1):
        try:
            validator.validate(example)
            print(f"Example {i} is valid")
        except jsonschema.exceptions.ValidationError as e:
            print(f"Example {i} validation error: {e.message}")

def main():
    """Generate and validate example files"""
    # Create examples directory if it doesn't exist
    os.makedirs("examples", exist_ok=True)
    
    # Generate and validate cyber intrusion examples
    cyber_schema = load_schema("schemas/cyberintrusion_investigation.json")
    cyber_examples = generate_cyber_intrusion_examples()
    print("\nValidating Cyber Intrusion examples:")
    validate_examples(cyber_examples, cyber_schema)
    
    # Save cyber intrusion examples
    with open("examples/cyber_intrusion_examples.jsonl", "w") as f:
        for example in cyber_examples:
            f.write(json.dumps(example) + "\n")
    
    # Generate and validate murder examples
    murder_schema = load_schema("schemas/murder_investigation.json")
    murder_examples = generate_murder_examples()
    print("\nValidating Murder Investigation examples:")
    validate_examples(murder_examples, murder_schema)
    
    # Save murder examples
    with open("examples/murder_investigation_examples.jsonl", "w") as f:
        for example in murder_examples:
            f.write(json.dumps(example) + "\n")
    
    # Generate and validate child abuse examples
    child_abuse_schema = load_schema("schemas/childabuse_investigation.json")
    child_abuse_examples = generate_child_abuse_examples()
    print("\nValidating Child Abuse Investigation examples:")
    validate_examples(child_abuse_examples, child_abuse_schema)
    
    # Save child abuse examples
    with open("examples/child_abuse_examples.jsonl", "w") as f:
        for example in child_abuse_examples:
            f.write(json.dumps(example) + "\n")
    
    # Generate and validate insider threat examples
    insider_threat_schema = load_schema("schemas/insiderthreat_investigation.json")
    insider_threat_examples = generate_insider_threat_examples()
    print("\nValidating Insider Threat Investigation examples:")
    validate_examples(insider_threat_examples, insider_threat_schema)
    
    # Save insider threat examples
    with open("examples/insider_threat_examples.jsonl", "w") as f:
        for example in insider_threat_examples:
            f.write(json.dumps(example) + "\n")
    
    print("\nGenerated example files:")
    print("- examples/cyber_intrusion_examples.jsonl")
    print("- examples/murder_investigation_examples.jsonl")
    print("- examples/child_abuse_examples.jsonl")
    print("- examples/insider_threat_examples.jsonl")

if __name__ == "__main__":
    main() 