from crypto_coin import CryptoCoin
from pywallet import wallet
import json

seed = wallet.generate_mnemonic()
wallet = wallet.create_wallet(network="omni", seed=seed, children=1)
wif = wallet.get('wif')
address = wallet.get('address')
seed = wallet.get('seed')
coin = CryptoCoin(address, wif, seed)

print(coin)