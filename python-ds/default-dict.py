from collections import defaultdict

logs = ["Error", "Error", "Info", "Error", "Warning", "Warning", "Info", "Error", "Error", "Info", "Error", "Warning", "Warning", "Info", "Error", "Error", "Info", "Error", "Warning", "Warning", "Info", "Error", "Error", "Info", "Error"]
log_count = defaultdict(int)
for level in logs:
    log_count[level]+=1
for key, value in log_count.items():
    print("level:\t\t", key)
    print("occurances:\t", value)