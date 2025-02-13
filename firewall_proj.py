import random


def generate_random_ip():
    return f"192.168.1.{random.randint(0, 100)}"

def check_firewall_rules(ip, rules): 
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"

def main():
    firewall_rules = {
    "192.168.1.191": "block",
    "192.168.1.209": "block",
    "192.168.1.20": "block"
}

for _ in range(12):
    ip_address = generate_random_ip()
    action = check_firewall_rules(ip_address, firewall_rules)
    random_number = random.randint(0, 9999)
    print(f"IP Address: {ip_address}, Action: {action}, Random Num: {random_number}")


if __name__ == "__main__":
    main()