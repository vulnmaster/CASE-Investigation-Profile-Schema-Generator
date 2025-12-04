"""
CASE Investigation Types Package

This package contains the configuration classes for different types of investigations
supported by the CASE Investigation Schema Generator.
"""

from .base_config import CaseClass, CaseProperty, BaseInvestigationType
from .cyber_intrusion import CyberIntrusionConfig
from .murder_investigation import MurderConfig
from .child_abuse_investigation import ChildAbuseConfig
from .insider_threat_investigation import InsiderThreatConfig
from .case_investigation import CaseInvestigationConfig

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
