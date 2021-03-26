from keygen.crypto_coin import CryptoCoin
from keygen.crypto_coin_service import CoinService
import pywaves as pw


class WavesCoinService(CoinService):

    def generate(self):
        pw.setOffline()
        addr = pw.Address()
        address = addr.address.decode("utf-8")
        private_key = addr.privateKey.decode("utf-8")
        seed = addr.seed
        return CryptoCoin(address, private_key, seed)


    def get_coin(self, private_key):
        pw.setOffline()
        addr = pw.Address(privateKey=private_key)
        address = addr.address.decode("utf-8")
        private_key = addr.privateKey.decode("utf-8")
        seed = addr.seed
        return CryptoCoin(address, private_key, seed)
