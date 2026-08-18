def check_status(status_code):
    if status_code == 200:
        return "PASS"
    return "FAIL"

print(check_status(200))
print(check_status(500))