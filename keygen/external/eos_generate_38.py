from crypto_coin import CryptoCoin
from aioeos.keys import EosKey

eos = EosKey()

address = eos.to_public()
wif = eos.to_wif()
seed = ''

coin = CryptoCoin(address, wif, seed)
print(coin)