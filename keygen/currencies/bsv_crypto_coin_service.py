from keygen.crypto_coin import CryptoCoin
from keygen.crypto_coin_service import CoinService

import bitsv


class BsvCoinService(CoinService):

    def generate(self):
        key = bitsv.Key()
        wif = key.to_wif()
        address = key.address
        return CryptoCoin(address, wif)

    def get_coin(self, private_key):
        key = bitsv.Key(wif=private_key)
        wif = key.to_wif()
        address = key.address
        return CryptoCoin(address, wif)
