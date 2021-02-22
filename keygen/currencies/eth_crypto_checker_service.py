from keygen.crypto_coin import CryptoCoin
from keygen.crypto_check_service import CoinService
import json
import subprocess

class EthCoinService(CoinService):

    def get_coin(self, private_key):
        with open('config.json') as json_file:
            config_json = json.load(json_file)
            venv_eth = config_json['venv_27']
            eth_external_script = config_json['eth_external_script']
        p = subprocess.check_output([venv_eth, eth_external_script, str(private_key)])
        obj = json.loads(p)
        return CryptoCoin(obj["address"], obj["wif"], obj["seed"])

    def generate_asset_id(self, coin):
        coin_address = coin.address
        return coin_address[2:8]
