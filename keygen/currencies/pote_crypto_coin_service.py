from keygen.crypto_coin import CryptoCoin
from keygen.crypto_coin_service import CoinService
import json
import subprocess


# FIXME implement python3.8 generate!
class PoteCoinService(CoinService):

    def generate(self):
        return self.generateList(1)[0]

    def generateList(self, count):
        with open('config.json') as json_file:
            config_json = json.load(json_file)
            venv_eos = config_json['venv_27']
            eos_external_script = config_json['pote_external_script']
        p = subprocess.check_output([venv_eos, eos_external_script, str(count)])
        objList = json.loads(p)
        coins = [CryptoCoin(obj["address"], obj["wif"], obj["seed"]) for obj in objList]
        return coins

    def get_coin(self, private_key):
        with open('config.json') as json_file:
            config_json = json.load(json_file)
            venv_pote = config_json['venv_27']
            pote_external_script = config_json['pote_external_script']
        p = subprocess.check_output([venv_pote, pote_external_script, str(private_key)])
        obj = json.loads(p)
        return CryptoCoin(obj["address"], obj["wif"], obj["seed"])
