from crypto_coin import CryptoCoin
import pywaves as pw
import json
from sys import argv

def toNumber(input):
    try:
        return int(input)
    except ValueError:
        print("Please input valid integer! {}".format(input))
        return None


max_iterator_count = 1
if len(argv) >= 2:
    max_iterator_count = toNumber(argv[1])


def generate_coin():
    pw.setOffline()
    addr = pw.Address()
    return CryptoCoin(addr.address, addr.privateKey, addr.seed)


coins = [generate_coin() for x in range(0, max_iterator_count)]

print(coins)
