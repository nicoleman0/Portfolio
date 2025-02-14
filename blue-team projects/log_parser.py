import re
import pandas as pd

LOG_FILE = "/var/log/syslog"

log_pattern = re.compile(
    r'(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:[+-]\d{2}:\d{2})?)\s+'
    r'(?P<host>\S+)\s+'
    r'(?P<process>[^\[\]:]+)(?:\[(?P<pid>\d+)\])?:\s'
    r'(?P<message>.+)'
)

parsed_logs = []

with open(LOG_FILE, "r") as f:
    for line in f:
        match = log_pattern.search(line)
        if match:
            parsed_logs.append(match.groupdict())

# Create DataFrame
df = pd.DataFrame(parsed_logs)

# Debugging: Print column names and first rows
print("DataFrame columns:", df.columns)
print(df.head())

# Check if 'process' column exists before accessing it
if 'process' in df.columns:
    print(df['process'].value_counts().head(10))
else:
    print("Column 'process' not found.")
