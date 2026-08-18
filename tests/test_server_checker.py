from fundamentals.server_checker import check_server_status

def test_server_is_online():
    assert check_server_status("UP") == "OFFLINE"

def test_server_is_offline():
    assert check_server_status("DOWN") == "OFFLINE"
