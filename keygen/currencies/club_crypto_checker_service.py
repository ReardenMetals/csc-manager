from keygen.crypto_coin import CryptoCoin
from keygen.crypto_check_service import CoinService
import json
import subprocess


class ClubCoinService(CoinService):

    def get_coin(self, private_key):
        with open('config.json') as json_file:
            config_json = json.load(json_file)
            venv_usdt = config_json['venv_27']
            usd_external_script = config_json['club_external_script']
        p = subprocess.check_output([venv_usdt, usd_external_script, str(private_key)])
        obj = json.loads(p)
        return CryptoCoin(obj["address"], obj["wif"], obj["seed"])

