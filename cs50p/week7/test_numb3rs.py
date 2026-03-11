from numb3rs import validate


def test_validate():
    true_ips = ["127.0.0.1", "0.0.0.0", "255.255.255.255"]
    for ip in true_ips:
        assert validate(ip) == True

    falsy_ips = ["512.512.512.512", "1.2.3.1000", "192.168.001.1", "192.168.00.1", "cat"]
    for ip in falsy_ips:
        assert validate(ip) == False