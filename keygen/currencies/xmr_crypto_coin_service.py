from keygen.crypto_coin import CryptoCoin
from keygen.crypto_coin_service import CoinService
import json
import subprocess

from monero.seed import Seed


class XmrCoinService(CoinService):

    def generate(self):
        s = Seed()

        seed = s.phrase
        addr = str(s.public_address())
        sk = s.secret_spend_key()

        return CryptoCoin(addr, sk, seed)

    def get_coin(self, private_key):
        with open('config.json') as json_file:
            config_json = json.load(json_file)
            venv_xmr = config_json['venv_27']
            xmr_external_script = config_json['xmr_external_script']
        p = subprocess.check_output([venv_xmr, xmr_external_script, str(private_key)])
        obj = json.loads(p)
        return CryptoCoin(obj["address"], obj["wif"], obj["seed"])

    def get_csv_header(self):
        return "Address,Secret View Key,Secret Spend Key,Secret Mnemonic\n"
