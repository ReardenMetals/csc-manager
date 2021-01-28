from crypto_coin import CryptoCoin
from crypto_keygen_service import CryptoKeygenService
from pybitcoin import BitcoinPrivateKey


class BtcCryptoKeygenService(CryptoKeygenService):

    def generate(self):
        private_key = BitcoinPrivateKey.from_passphrase()
        wif = private_key.to_wif()
        seed = private_key.passphrase()
        address = private_key.public_key().address()
        coin = CryptoCoin(address, wif, seed)
        return coin
