from keygen.crypto_coin import CryptoCoin
from keygen.crypto_keygen_service import CryptoKeygenService
from pybitcoin import LitecoinPrivateKey

class LtcCryptoKeygenService(CryptoKeygenService):

    def generate(self):
        private_key = LitecoinPrivateKey.from_passphrase()
        # seed = private_key.passphrase()
        wif = private_key.to_wif()
        address = private_key.public_key().address()
        return CryptoCoin(address, wif)

