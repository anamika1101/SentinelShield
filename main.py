from detector import detect_attack
from rate_limiter import check_rate_limit
from logger import log_event

print("SentinelShield – Intrusion Detection System")
print("-------------------------------------------")

ip = input("Enter IP address: ")
payload = input("Enter request payload: ")

abusive = check_rate_limit(ip)
attack = detect_attack(payload)

if abusive:
    result = "Blocked (Rate Limit Exceeded)"
elif attack:
    result = f"Blocked ({attack})"
else:
    result = "Allowed"

print("\nResult:", result)
log_event(ip, payload, result)
print("Log saved.")

print("\nResult:", result)
log_event(ip, payload, result)
print("Log saved.")

print("\n--- SentinelShield Summary / Dashboard ---")
print("• Request inspected successfully")
print("• Detection decision applied")
print("• Event logged with timestamp and IP")
print("• Check logs/security.log for detailed analysis")

  
