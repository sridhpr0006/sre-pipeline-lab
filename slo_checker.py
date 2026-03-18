# SLO Availability Checker
# Checks which services are breaching SLO target

def check_slo_breaches(services, slo_target=99.0):
    # Create empty list for breaching services
    breaches = []
    
    # Check each service against SLO target
    for service, availability in services.items():
        if availability < slo_target:
            breaches.append((service, availability))
    
    return breaches

# Example data - trading platform services
services = {
    "mobile_login": 99.95,
    "payments":     98.50,
    "trading":      99.10,
    "mobile_app":   97.80
}

# Run the check
breaches = check_slo_breaches(services)

# Print results
print("--- SLO Breach Report ---")
if breaches:
    for service, availability in breaches:
        print(f"{service}: {availability:.2f}% - BREACH")
else:
    print("All services meeting SLO targets")

# Exit with error code if breaches found
import sys
if breaches:
    print(f"\nFAILED: {len(breaches)} services breaching SLO")
    sys.exit(1)
else:
    print("\nPASSED: All services meeting SLO targets")
    sys.exit(0)