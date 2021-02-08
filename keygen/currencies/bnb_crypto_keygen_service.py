from keygen.crypto_coin import CryptoCoin
from keygen.crypto_keygen_service import CryptoKeygenService
import json
import subprocess


class BnbCryptoKeygenService(CryptoKeygenService):

    def generate(self):
        return self.generateList(1)[0]

    def generateList(self, count):
        with open('config.json') as json_file:
            config_json = json.load(json_file)
            venv_bnb = config_json['venv_bnb']
            bnb_external_script = config_json['bnb_external_script']
        p = subprocess.check_output([venv_bnb, bnb_external_script, str(count)])
        objList = json.loads(p)
        coins = [CryptoCoin(obj["address"], obj["wif"], obj["seed"]) for obj in objList]
        return coins
