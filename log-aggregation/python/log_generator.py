from datetime import datetime, timedelta
import random

# Function to generate a fake log entry
def generate_log_entry(start_time, line_number):
    # Define log levels and example messages
    log_levels = ["INFO", "WARNING", "ERROR"]
    messages = {
        "INFO": ["User logged in successfully.", "New user registered. Username: user123.", 
                 "System health check completed. No issues found.", "Backup process started."],
        "WARNING": ["Attempt to access unauthorized resource by user_id: 123.", 
                    "Memory usage exceeds 80% of capacity.", 
                    "Disk space on server 'server01' is below 10%."],
        "ERROR": ["Database connection failed. Retrying in 5 seconds.", 
                  "Unable to send email to user_id: 456.", 
                  "Failed to update configuration file."]
    }

    # Generate a timestamp for the log entry
    timestamp = start_time + timedelta(minutes=line_number)
    timestamp_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")

    # Randomly choose a log level and a corresponding message
    level = random.choice(log_levels)
    message = random.choice(messages[level])

    return f"{timestamp_str} {level} {message}"

# Generate 100 log entries
start_time = datetime.now()
fake_logs = [generate_log_entry(start_time, i) for i in range(1000)]

print("generating new log entries to file")
count = 0
log_file_name = "./log-aggregation/python/log_file.txt"
file = open(log_file_name, 'w')
for line in fake_logs:
    count+=1
    file.write(line + "\n")
file.close
print("wrote %s log entries to %s" % (count, log_file_name))
