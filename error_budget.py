# Error Budget Calculator
# Calculates error budget remaining for a service

def calculate_error_budget(slo_target, actual_availability, total_minutes):
    # Calculate allowed downtime based on SLO
    allowed_downtime = total_minutes * (1 - slo_target / 100)
    
    # Calculate actual downtime
    actual_downtime = total_minutes * (1 - actual_availability / 100)
    
    # Calculate remaining budget
    remaining_budget = allowed_downtime - actual_downtime
    
    # Calculate percentage consumed
    if allowed_downtime > 0:
        budget_consumed = (actual_downtime / allowed_downtime) * 100
    else:
        budget_consumed = 100
    
    return {
        "allowed_downtime_mins": round(allowed_downtime, 2),
        "actual_downtime_mins": round(actual_downtime, 2),
        "remaining_budget_mins": round(remaining_budget, 2),
        "budget_consumed_pct": round(budget_consumed, 2)
    }

# Example - mobile login service
result = calculate_error_budget(
    slo_target=99.9,
    actual_availability=99.95,
    total_minutes=43200  # 30 days
)

print("--- Error Budget Report ---")
print(f"Allowed downtime:    {result['allowed_downtime_mins']} minutes")
print(f"Actual downtime:     {result['actual_downtime_mins']} minutes")
print(f"Remaining budget:    {result['remaining_budget_mins']} minutes")
print(f"Budget consumed:     {result['budget_consumed_pct']}%")

import sys
if result['budget_consumed_pct'] > 100:
    print("\nFAILED: Error budget exhausted - release freeze triggered")
    sys.exit(1)
else:
    print("\nPASSED: Error budget within limits")
    sys.exit(0)