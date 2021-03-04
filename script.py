from logic.keygen import generate_keys


def default_input(message, defaultVal):
    if defaultVal:
        return input("%s [%s] : " % (message, defaultVal)) or defaultVal
    else:
        return input("%s " % message)


def init():
    max_iterator_count = int(default_input("How many codes you want? ", "10"))
    coin = default_input("What crypto you making (BTC, ETH, ...)? ", "BTC").upper()
    laser_type = default_input("What laser is this (A, B, C)? ", "A").upper()
    generate_keys(count=max_iterator_count, coin=coin, laser=laser_type)


if __name__ == "__main__":
    init()
