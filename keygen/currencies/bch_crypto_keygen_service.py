from keygen.crypto_coin import CryptoCoin
from keygen.crypto_keygen_service import CryptoKeygenService
from pybitcoin import BitcoinPrivateKey
from cashaddress import convert

class BchCryptoKeygenService(CryptoKeygenService):

    def generate(self):
        private_key = BitcoinPrivateKey.from_passphrase()
        # seed = private_key.passphrase()
        # private_key._compressed = True
        wif = private_key.to_wif()
        address = convert.to_cash_address(private_key.public_key().address())
        return CryptoCoin(address.replace('bitcoincash:', ''), wif)

