from .risk_types import RiskSignal, RiskLevel

def ml_caution_advisory(anomaly_score: float) -> RiskSignal | None:
    """
    ML MAY ONLY INCREASE CAUTION.
    Never returns LOW.
    Never authorizes action.
    """
    if anomaly_score < 0.5:
        return None

    if anomaly_score < 0.75:
        level = RiskLevel.MEDIUM
    else:
        level = RiskLevel.HIGH

    return RiskSignal(
        source="ml_advisory",
        level=level,
        confidence=min(1.0, anomaly_score)
    )
