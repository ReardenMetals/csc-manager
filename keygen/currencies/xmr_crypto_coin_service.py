from keygen.crypto_coin import CryptoCoin
from keygen.crypto_coin_service import CoinService

from monero.seed import Seed


class XmrCoinService(CoinService):

    def generate(self):
        s = Seed()

        seed = s.phrase
        addr = str(s.public_address())
        sk = s.secret_spend_key()

        return CryptoCoin(addr, seed, seed)

    def get_coin(self, private_key):
        s = Seed(phrase_or_hex=private_key)

        seed = s.phrase
        addr = str(s.public_address())
        sk = s.secret_spend_key()

        return CryptoCoin(addr, sk, seed)

    def get_csv_header(self):
        return "Address,Secret Mnemonic\n"

    def format(self, coin):
        return "{},{}\n".format(coin.address, coin.wif)
