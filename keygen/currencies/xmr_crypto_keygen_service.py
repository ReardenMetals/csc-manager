from keygen.crypto_coin import CryptoCoin
from keygen.crypto_keygen_service import CryptoKeygenService
# for monero wallet
from moneropy import account

class XmrCryptoKeygenService(CryptoKeygenService):

    def generate(self):
        seed, sk, vk, addr = account.gen_new_wallet()
        # line = "{},{},{},{}\n".format(addr,vk,sk,seed)
        return CryptoCoin(addr, sk, seed)

    def get_csv_header(self):
        return "Address,Secret View Key,Secret Spend Key,Secret Mnemonic\n"
