from keygen.crypto_coin import CryptoCoin
from keygen.crypto_coin_service import CoinService
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes, WifDecoder, \
    LitecoinConf
import json
import subprocess


class LtcCoinService(CoinService):

    def generate(self):
        # Generate random mnemonic
        mnemonic = Bip39MnemonicGenerator.FromWordsNumber(12)

        # Generate seed from mnemonic
        seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

        # Generate BIP44 master keys
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.LITECOIN)

        address = bip_obj_mst.PublicKey().ToAddress()
        wif = bip_obj_mst.PrivateKey().ToWif()
        seed = mnemonic

        return CryptoCoin(address, wif, seed)

    def get_coin(self, private_key):
        decoded_wif = WifDecoder.Decode(wif_str=private_key,
                                        net_addr_ver=LitecoinConf.WIF_NET_VER.Main())
        key_pair = Bip44.FromAddressPrivKey(decoded_wif, Bip44Coins.LITECOIN)
        address = key_pair.PublicKey().ToAddress()
        return CryptoCoin(address, private_key)

    # Deprecated
    def get_coin_subprocess(self, private_key):
        with open('config.json') as json_file:
            config_json = json.load(json_file)
            venv_ltc = config_json['venv_27']
            ltc_external_script = config_json['ltc_external_script']
        p = subprocess.check_output([venv_ltc, ltc_external_script, str(private_key)])
        obj = json.loads(p)
        return CryptoCoin(obj["address"], obj["wif"], obj["seed"])
