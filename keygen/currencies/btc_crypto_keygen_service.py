from keygen.crypto_coin import CryptoCoin
from keygen.crypto_keygen_service import CryptoKeygenService
from pybitcoin import BitcoinPrivateKey


class BtcCryptoKeygenService(CryptoKeygenService):

    def generate(self):
        private_key = BitcoinPrivateKey.from_passphrase()
        wif = private_key.to_wif()
        seed = private_key.passphrase()
        address = private_key.public_key().address()
        return CryptoCoin(address, wif, seed)

    def format(self, coin):
        return "{},{},{}\n".format(coin.wif, coin.address, coin.seed)

    def get_csv_header(self):
        return "WIF,Address,Seed\n"
