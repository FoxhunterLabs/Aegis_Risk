from .risk_types import RiskSignal, RiskLevel

def conservative_aggregate(signals: list[RiskSignal]) -> RiskLevel:
    """
    Order-independent, monotonic aggregation.
    Highest risk always wins.
    """
    if not signals:
        return RiskLevel.LOW

    return max(signal.level for signal in signals)
