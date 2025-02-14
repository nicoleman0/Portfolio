import re
import pandas as pd

LOG_FILE = "/var/log/syslog" # Set path to your log file

# syslog format: <timestamp> <hostname> <program>: <message>
log_pattern = re.compile(r'(?P<date>\w+\s+\d+\s+\d+:\d+:\d+)\s+(?P<host>\S+)\s+(?P<process>\S+)\[(?P<pid>\d+)\]:\s(?P<message>.+)')

# Analyze the hosts that are generating the most logs
def parse_syslog(file_path):
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            match = log_pattern.match(line)
            if match:
                data.append(match.groupdict())

    return pd.DataFrame(data)

df = parse_syslog(LOG_FILE)
print (df.head()) # View parsed logs

# Analyze the processes that are generating the most logs
print(df['process'].value_counts().head(10))
