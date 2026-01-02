from dataclasses import dataclass
from .risk_types import RiskLevel

@dataclass(frozen=True)
class RiskResult:
    level: RiskLevel
    requires_human_review: bool
