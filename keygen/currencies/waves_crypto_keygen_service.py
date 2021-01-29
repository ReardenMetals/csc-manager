from keygen.crypto_coin import CryptoCoin
from keygen.crypto_keygen_service import CryptoKeygenService
import pywaves as pw

class WavesCryptoKeygenService(CryptoKeygenService):

    def generate(self):
        pw.setOffline()
        addr = pw.Address()
        return CryptoCoin(addr.address, addr.privateKey, addr.seed)

