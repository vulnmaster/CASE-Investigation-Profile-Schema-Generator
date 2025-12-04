"""
CASE Investigation Types Package

This package contains the configuration classes for different types of investigations
supported by the CASE Investigation Schema Generator.
"""

from .base_config import BaseInvestigationType, CaseClass, CaseProperty
from .case_investigation import CaseInvestigationConfig
from .child_abuse_investigation import ChildAbuseConfig
from .cyber_intrusion import CyberIntrusionConfig
from .insider_threat_investigation import InsiderThreatConfig
from .murder_investigation import MurderConfig

__all__ = [
    "CaseClass",
    "CaseProperty",
    "BaseInvestigationType",
    "CyberIntrusionConfig",
    "MurderConfig",
    "ChildAbuseConfig",
    "InsiderThreatConfig",
    "CaseInvestigationConfig",
]
