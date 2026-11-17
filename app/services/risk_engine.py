def calculate_risk_score(critical_count: int, high_count: int) -> str:
    if critical_count > 0:
        return "CRITICAL"
    elif high_count > 2:
        return "HIGH"
    elif high_count > 0:
        return "MEDIUM"
    return "LOW"
