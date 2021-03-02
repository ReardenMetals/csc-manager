from bip_utils.utils import CryptoUtils

from keygen.crypto_coin import CryptoCoin
from keygen.crypto_coin_service import CoinService

from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes, WifDecoder, DashConf, \
    Base58Encoder, NetVersions, WifEncoder

from keygen.wif_validator import is_compressed_wif

CLUB_P2PKH_NET_VER = NetVersions(b"\x1c")
CLUB_WIF_NET_VER = NetVersions(b"\x99")


class ClubCoinService(CoinService):

    def generate(self):

        # Generate random mnemonic
        mnemonic = Bip39MnemonicGenerator.FromWordsNumber(12)

        # Generate seed from mnemonic
        seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

        # Generate BIP44 master keys
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN)

        wif = WifEncoder.Encode(bip_obj_mst.PrivateKey().Raw().ToBytes(), True, CLUB_WIF_NET_VER.Main())

        pub_key_bytes = bip_obj_mst.PublicKey().RawCompressed().ToBytes()
        address = Base58Encoder.CheckEncode(CLUB_P2PKH_NET_VER.Main() + CryptoUtils.Hash160(pub_key_bytes))

        seed = mnemonic

        return CryptoCoin(address, wif, seed)

    def get_coin(self, private_key):
        if is_compressed_wif(private_key):
            return self.get_default_coin(private_key)
        else:
            return self.get_uncompressed_coin(private_key)

    @staticmethod
    def get_default_coin(private_key):
        decoded_wif = WifDecoder.Decode(wif_str=private_key, net_addr_ver=CLUB_WIF_NET_VER.Main())
        bip44_mst = Bip44.FromAddressPrivKey(decoded_wif, Bip44Coins.BITCOIN)
        pub_key_bytes = bip44_mst.PublicKey().RawCompressed().ToBytes()
        address = Base58Encoder.CheckEncode(CLUB_P2PKH_NET_VER.Main() + CryptoUtils.Hash160(pub_key_bytes))
        return CryptoCoin(address, private_key)

    @staticmethod
    def get_uncompressed_coin(private_key):
        print("Warning Uncompressed key")
        decoded_wif = WifDecoder.Decode(wif_str=private_key, net_addr_ver=CLUB_WIF_NET_VER.Main())
        bip44_mst = Bip44.FromAddressPrivKey(decoded_wif, Bip44Coins.BITCOIN)
        to_hex = bip44_mst.PublicKey().RawUncompressed().ToBytes()
        pub_key_bytes = b'\x04' + to_hex
        address = Base58Encoder.CheckEncode(CLUB_P2PKH_NET_VER.Main() + CryptoUtils.Hash160(pub_key_bytes))
        return CryptoCoin(address, private_key)
