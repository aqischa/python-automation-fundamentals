server_name = ["server01", "server02", "server03"]
server_status = ["UP", "DOWN", "UP"]

def check_status(server_status):
    if server_status == "UP":
        return "ONLINE"
    return "OFFLINE"

for server, status in zip(server_name, server_status):
    print(f"{server}: {check_status(status)}")

## Better Solution using dictionary
print("Better Solution using dictionary:")

servers = {
    "server01": "UP",
    "server02": "DOWN",
    "server03": "UP"
}

def check_server_status(status):
    if status == "UP":
        return "ONLINE"
    return "OFFLINE"

for server, status in servers.items():
    print(f"{server}: {check_server_status(status)}")