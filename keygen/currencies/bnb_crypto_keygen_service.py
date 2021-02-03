from keygen.crypto_coin import CryptoCoin
from keygen.crypto_keygen_service import CryptoKeygenService
import json
import subprocess


class BnbCryptoKeygenService(CryptoKeygenService):

    def generate(self):
        with open('config.json') as json_file:
            config_json = json.load(json_file)
            venv_bnb = config_json['venv_bnb']
            bnb_external_script = config_json['bnb_external_script']
        p = subprocess.check_output([venv_bnb, bnb_external_script])
        obj = json.loads(p)
        coin = CryptoCoin(obj["address"], obj["wif"], obj["seed"])
        return coin
