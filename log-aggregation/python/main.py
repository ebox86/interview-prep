from collections import defaultdict
import requests

# Set host if log file is on a remote host
host = ""

def aggregate():
    data = defaultdict(int)
    logs = []

    # Fetch logs from remote host if host is specified
    if host:
        response = requests.get(host)
        logs = response.text.splitlines()
    else:
        # Read logs from a local file
        with open('./log-aggregation/python/log_file.txt', 'r') as file:
            logs = file.readlines()

    # Process each log line
    for line in logs:
        line_parts = line.strip().split(' ')
        if len(line_parts) > 2:
            log_level = line_parts[2]  # Assuming the log level is always at the same position
            data[log_level] += 1

    return data

def format_output(data):
    formatted_data = []
    for log_level, count in data.items():
        formatted_data.append(f"{log_level}: {count} entries")
    return '\n'.join(formatted_data)


log_data = aggregate()
print(format_output(log_data))
