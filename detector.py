from rules import ATTACK_RULES

def detect_attack(payload):
    for attack, patterns in ATTACK_RULES.items():
        for pattern in patterns:
            if pattern.lower() in payload.lower():
                return attack
    return None
