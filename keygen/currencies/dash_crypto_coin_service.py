from bip_utils.utils import CryptoUtils

from keygen.crypto_coin import CryptoCoin
from keygen.crypto_coin_service import CoinService
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes, WifDecoder, DashConf, \
    Base58Encoder

from keygen.wif_validator import is_compressed_wif


class DashCoinService(CoinService):

    def generate(self):
        # Generate random mnemonic
        mnemonic = Bip39MnemonicGenerator.FromWordsNumber(12)

        # Generate seed from mnemonic
        seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

        # Generate BIP44 master keys
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.DASH)

        address = bip_obj_mst.PublicKey().ToAddress()
        wif = bip_obj_mst.PrivateKey().ToWif()
        seed = mnemonic

        return CryptoCoin(address, wif, seed)

    def get_coin(self, private_key):
        if is_compressed_wif(private_key):
            return self.get_default_coin(private_key)
        else:
            return self.get_uncompressed_coin(private_key)

    @staticmethod
    def get_default_coin(private_key):
        decoded_wif = WifDecoder.Decode(wif_str=private_key,
                                        net_addr_ver=DashConf.WIF_NET_VER.Main())
        key_pair = Bip44.FromAddressPrivKey(decoded_wif, Bip44Coins.DASH)
        address = key_pair.PublicKey().ToAddress()
        return CryptoCoin(address, private_key)

    @staticmethod
    def get_uncompressed_coin(private_key):
        print("Warning Uncompressed key")
        config_alias = DashConf
        coin_type = Bip44Coins.DASH
        decoded_wif = WifDecoder.Decode(wif_str=private_key, net_addr_ver=config_alias.WIF_NET_VER.Main())
        bip44_mst = Bip44.FromAddressPrivKey(decoded_wif, coin_type)
        to_hex = bip44_mst.PublicKey().RawUncompressed().ToBytes()
        pub_key_bytes = b'\x04' + to_hex
        address = Base58Encoder.CheckEncode(config_alias.P2PKH_NET_VER.Main() + CryptoUtils.Hash160(pub_key_bytes))
        return CryptoCoin(address, private_key)
