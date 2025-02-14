import re

LOG_FILE = "/var/log/auth.log"
FAILED_LOGIN_PATTERN = r"Failed password for (\S+) from (\S+) port (\d+)"

def find_failed_logins():
    with open(LOG_FILE, "r") as f:
        for line in f:
            match = re.search(FAILED_LOGIN_PATTERN, line)
            if match:
                user, ip, port = match.groups()
                print(f"Failed login attempt by {user} from {ip} on port {port}")

find_failed_logins()
