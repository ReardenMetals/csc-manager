from crypto_coin import CryptoCoin
from pybitcoin import BitcoinPrivateKey
import json
from sys import argv

class ClubCoinPublicKey(BitcoinPrivateKey):
    _pubkeyhash_version_byte = 0x1c
    _wif_version_byte = 0x99

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
    private_key = ClubCoinPublicKey.from_passphrase()
    # private_key._compressed = True
    wif = private_key.to_wif()
    address = private_key.public_key().address()
    seed = private_key.passphrase()
    return CryptoCoin(address, wif, seed)


coins = [generate_coin() for x in range(0, max_iterator_count)]

print(coins)
