status_code = 500

if status_code == 200:
    print("Request successful.")
elif status_code == 404:
    print("Resource not found")
else:
    print("Something went wrong")