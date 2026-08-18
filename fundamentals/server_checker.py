servers = {
    "server01": "UP",
    "server02": "DOWN",
    "server03": "UP"
}

def check_server_status(status):
    if status == "UP":
        return "ONLINE"
    return "OFFLINE"

def display_server_status():
    for server, status in servers.items():
        print(f"{server}: {check_server_status(status)}")

if __name__ == "__main__":
    display_server_status()