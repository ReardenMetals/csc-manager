from keygen.crypto_coin import CryptoCoin
from keygen.crypto_keygen_service import CryptoKeygenService
from pybitcoin import BitcoinPrivateKey

class PotCoinPublicKey(BitcoinPrivateKey):
    _pubkeyhash_version_byte = 0x37

class PoteCryptoKeygenService(CryptoKeygenService):

    def generate(self):
        private_key = PotCoinPublicKey.from_passphrase()
        # private_key._compressed = True
        wif = private_key.to_wif()
        address = private_key.public_key().address()
        return CryptoCoin(address, wif)

