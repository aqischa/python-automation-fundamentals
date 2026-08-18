with open("automation/application.log", "r") as logfile:
    error_count = 0
    for line in logfile:
        if "ERROR" in line:
            error_count += 1

print(f"Total errors in logfile: {error_count}")