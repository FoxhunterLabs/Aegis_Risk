from enum import Enum
from dataclasses import dataclass

class RiskLevel(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

@dataclass(frozen=True)
class RiskSignal:
    source: str
    level: RiskLevel
    confidence: float  # 0.0 – 1.0
