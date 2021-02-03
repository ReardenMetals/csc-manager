from crypto_coin import CryptoCoin
from py_crypto_hd_wallet import HdWallet, HdWalletFactory, HdWalletSaver, HdWalletCoins, HdWalletWordsNum
from pywallet import wallet
import json

hd_wallet_fact = HdWalletFactory(HdWalletCoins.BINANCE_COIN)

hd_wallet = hd_wallet_fact.CreateRandom("binanc_wallet", HdWalletWordsNum.WORDS_NUM_24)
hd_wallet.Generate(addr_num = 1)

wall = json.loads(hd_wallet.ToJson())
address = wall["addresses"]["address_1"]["address"]
wif = wall["master_key"]["raw_priv"]#TODO
seed = wall["mnemonic"]
coin = CryptoCoin(address, wif, seed)


print(coin)