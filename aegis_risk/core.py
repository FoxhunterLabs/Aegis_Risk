from .risk_types import RiskSignal, RiskLevel
from .aggregation import conservative_aggregate

def synthesize_risk(signals: list[RiskSignal]) -> RiskLevel:
    """
    Deterministic risk synthesis.
    No policy.
    No decisions.
    """
    return conservative_aggregate(signals)
