from aegis_risk.risk_types import RiskSignal, RiskLevel
from aegis_risk.core import synthesize_risk

def test_order_independence():
    a = RiskSignal("a", RiskLevel.MEDIUM, 0.8)
    b = RiskSignal("b", RiskLevel.HIGH, 0.6)

    assert synthesize_risk([a, b]) == synthesize_risk([b, a])
