from crypto_coin import CryptoCoin
from py_crypto_hd_wallet import HdWallet, HdWalletFactory, HdWalletSaver, HdWalletCoins, HdWalletWordsNum
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
    hd_wallet_fact = HdWalletFactory(HdWalletCoins.BINANCE_COIN)
    hd_wallet = hd_wallet_fact.CreateRandom("binanc_wallet", HdWalletWordsNum.WORDS_NUM_24)
    hd_wallet.Generate(addr_num=1)

    wall = json.loads(hd_wallet.ToJson())
    address = wall["addresses"]["address_1"]["address"]
    wif = wall["master_key"]["raw_priv"]  # TODO
    seed = wall["mnemonic"]
    return CryptoCoin(address, wif, seed)


coins = [generate_coin() for x in range(0, max_iterator_count)]

print(coins)
