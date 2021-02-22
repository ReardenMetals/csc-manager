from keygen.crypto_coin import CryptoCoin
from keygen.crypto_coin_service import CoinService
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes, WifDecoder
import json
import subprocess


class BnbCoinService(CoinService):

    def generate(self):
        # Generate random mnemonic
        mnemonic = Bip39MnemonicGenerator.FromWordsNumber(12)

        # Generate seed from mnemonic
        seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

        # Generate BIP44 master keys
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BINANCE_COIN)

        address = bip_obj_mst.PublicKey().ToAddress()
        wif = bip_obj_mst.PrivateKey().ToExtended()
        seed = mnemonic

        return CryptoCoin(address, wif, seed)

    def get_coin(self, private_key):
        addr = Bip44.FromExtendedKey(private_key, Bip44Coins.BINANCE_COIN)
        address = addr.PublicKey().ToAddress()
        return CryptoCoin(address, private_key)

    # Deprecated
    def generate_list_sub_process(self, count):
        with open('config.json') as json_file:
            config_json = json.load(json_file)
            venv_bnb = config_json['venv_bnb']
            bnb_external_script = config_json['bnb_external_script']
        p = subprocess.check_output([venv_bnb, bnb_external_script, str(count)])
        objList = json.loads(p)
        coins = [CryptoCoin(obj["address"], obj["wif"], obj["seed"]) for obj in objList]
        return coins
