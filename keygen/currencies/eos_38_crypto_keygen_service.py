from keygen.crypto_coin import CryptoCoin
from keygen.crypto_keygen_service import CryptoKeygenService

from aioeos.keys import EosKey


class Eos38CryptoKeygenService(CryptoKeygenService):

    def generate(self):
        eos = EosKey()
        address = eos.to_public()
        wif = eos.to_wif()
        seed = ''
        return CryptoCoin(address, wif, seed)