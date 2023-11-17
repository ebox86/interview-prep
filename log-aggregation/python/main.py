from collections import defaultdict
import requests

# Set host if log file is on a remote host
host = ""

def aggregate():
    # i like using defaultdict here because it automatically initializes each new key with a default value
    # note: you do have to specify a type for the values
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
            data[log_level] += 1 # using defaultdict allows us to increment values of undefined keys

    return data

def format_counts(data):
    formatted_data = []
    for log_level, count in data.items():
        formatted_data.append(f"{log_level}: {count} entries")
    return '\n'.join(formatted_data)


log_data = aggregate()
print(format_counts(log_data))
