from crypto_coin import CryptoCoin
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes, WifDecoder
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
    # Generate random mnemonic
    mnemonic = Bip39MnemonicGenerator.FromWordsNumber(12)

    # Generate seed from mnemonic
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

    # Generate BIP44 master keys
    bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BINANCE_COIN)

    address = bip_obj_mst.PublicKey().ToAddress()
    wif = bip_obj_mst.PrivateKey().ToExtended()
    seed = mnemonic
    return CryptoCoin(address, wif, seed)


coins = [generate_coin() for x in range(0, max_iterator_count)]

print(coins)