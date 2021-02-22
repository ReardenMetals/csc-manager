from bip_utils import BitcoinConf, Bip44Coins, WifDecoder, Bip44, Base58Encoder
from bip_utils.utils import CryptoUtils

from keygen.crypto_coin import CryptoCoin
from keygen.crypto_check_service import CoinService
import json
import subprocess


class BtcCoinService(CoinService):

    def get_coin(self, private_key):
        config_alias = BitcoinConf
        coin_type = Bip44Coins.BITCOIN
        decodedWif = WifDecoder.Decode(wif_str=private_key, net_addr_ver=config_alias.WIF_NET_VER.Main())
        bip44_mst = Bip44.FromAddressPrivKey(decodedWif, coin_type)
        to_hex = bip44_mst.PublicKey().RawUncompressed().ToBytes()
        pub_key_bytes = b'\x04' + to_hex
        address = Base58Encoder.CheckEncode(config_alias.P2PKH_NET_VER.Main() + CryptoUtils.Hash160(pub_key_bytes))
        return CryptoCoin(address, private_key)

    def get_coin_sub_process(self, private_key):
        with open('config.json') as json_file:
            config_json = json.load(json_file)
            venv_btc = config_json['venv_27']
            btc_external_script = config_json['btc_external_script']
        p = subprocess.check_output([venv_btc, btc_external_script, str(private_key)])
        obj = json.loads(p)
        return CryptoCoin(obj["address"], obj["wif"], obj["seed"])
