from aegis_risk.risk_types import RiskSignal, RiskLevel
from aegis_risk.core import synthesize_risk
from aegis_risk.ml_advisory import ml_caution_advisory

signals = [
    RiskSignal("geometry", RiskLevel.MEDIUM, 0.9),
]

ml_signal = ml_caution_advisory(anomaly_score=0.82)
if ml_signal:
    signals.append(ml_signal)

final_risk = synthesize_risk(signals)

print("FINAL RISK:", final_risk.name)
print("HUMAN REVIEW REQUIRED:", final_risk.value >= RiskLevel.HIGH.value)
