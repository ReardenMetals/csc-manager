from keygen.crypto_coin import CryptoCoin
from keygen.crypto_coin_service import CoinService

from bip_utils import BitcoinConf, Bip44Coins, WifDecoder, Bip44, Base58Encoder, Bip39MnemonicGenerator, \
    Bip39SeedGenerator
from bip_utils.utils import CryptoUtils

import json
import subprocess


class BtcCoinService(CoinService):

    def generate(self):
        # Generate random mnemonic
        mnemonic = Bip39MnemonicGenerator.FromWordsNumber(12)

        # Generate seed from mnemonic
        seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

        # Generate BIP44 master keys
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN)

        address = bip_obj_mst.PublicKey().ToAddress()
        wif = bip_obj_mst.PrivateKey().ToWif()
        seed = mnemonic

        return CryptoCoin(address, wif, seed)

    def get_coin(self, private_key):
        config_alias = BitcoinConf
        coin_type = Bip44Coins.BITCOIN
        decodedWif = WifDecoder.Decode(wif_str=private_key, net_addr_ver=config_alias.WIF_NET_VER.Main())
        bip44_mst = Bip44.FromAddressPrivKey(decodedWif, coin_type)
        to_hex = bip44_mst.PublicKey().RawUncompressed().ToBytes()
        pub_key_bytes = b'\x04' + to_hex
        address = Base58Encoder.CheckEncode(config_alias.P2PKH_NET_VER.Main() + CryptoUtils.Hash160(pub_key_bytes))
        return CryptoCoin(address, private_key)

    # Deprecated
    def get_coin_sub_process(self, private_key):
        with open('config.json') as json_file:
            config_json = json.load(json_file)
            venv_btc = config_json['venv_27']
            btc_external_script = config_json['btc_external_script']
        p = subprocess.check_output([venv_btc, btc_external_script, str(private_key)])
        obj = json.loads(p)
        return CryptoCoin(obj["address"], obj["wif"], obj["seed"])
