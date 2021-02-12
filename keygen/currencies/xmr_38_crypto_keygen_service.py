from keygen.crypto_coin import CryptoCoin
from keygen.crypto_keygen_service import CryptoKeygenService

from monero.seed import Seed

class Xmr38CryptoKeygenService(CryptoKeygenService):

    def generate(self):
        s = Seed()

        seed = s.phrase
        addr = str(s.public_address())
        sk = s.secret_spend_key()

        return CryptoCoin(addr, sk, seed)

    def get_csv_header(self):
        return "Address,Secret View Key,Secret Spend Key,Secret Mnemonic\n"
