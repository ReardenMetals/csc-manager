from keygen.crypto_coin import CryptoCoin
from keygen.crypto_check_service import CoinService
import json
import subprocess


class XmrCoinService(CoinService):

    def get_coin(self, private_key):
        with open('config.json') as json_file:
            config_json = json.load(json_file)
            venv_xmr = config_json['venv_27']
            xmr_external_script = config_json['xmr_external_script']
        p = subprocess.check_output([venv_xmr, xmr_external_script, str(private_key)])
        obj = json.loads(p)
        return CryptoCoin(obj["address"], obj["wif"], obj["seed"])
