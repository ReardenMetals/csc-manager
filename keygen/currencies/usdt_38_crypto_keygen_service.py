from keygen.crypto_coin import CryptoCoin
from keygen.crypto_keygen_service import CryptoKeygenService
import json
import subprocess

class NewUsdtCryptoKeygenService(CryptoKeygenService):

    def generate(self):
        return self.generateList(1)[0]

    def generateList(self, count):
        with open('config.json') as json_file:
            config_json = json.load(json_file)
            venv_usdt = config_json['venv_usdt']
            usd_external_script = config_json['usd_external_script']
        p = subprocess.check_output([venv_usdt, usd_external_script, str(count)])
        objList = json.loads(p)
        coins = [CryptoCoin(obj["address"], obj["wif"], obj["seed"]) for obj in objList]
        return coins
