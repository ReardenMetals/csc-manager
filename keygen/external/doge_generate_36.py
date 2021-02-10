from crypto_coin import CryptoCoin
from pywallet import wallet
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
    seed = wallet.generate_mnemonic()
    w = wallet.create_wallet(network="doge", seed=seed, children=1)
    wif = w.get('wif')
    address = w.get('address')
    seed = w.get('seed')
    return CryptoCoin(address, wif, seed)

coins = [generate_coin() for x in range(0, max_iterator_count)]

print(coins)