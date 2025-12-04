"""
CASE Investigation Schema Generator

This package provides functionality to generate JSON schemas that are semantically compatible
with the Cyber-investigation Analysis Standard Expression (CASE) ontology.
"""

from .investigation_schema_generator import CaseSchemaGenerator, InvestigationType

__version__ = "0.1.0"
__all__ = ["CaseSchemaGenerator", "InvestigationType"]
