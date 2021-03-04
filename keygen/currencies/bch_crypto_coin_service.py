from keygen.crypto_coin_service import CoinService
from bip_utils.utils import CryptoUtils
from cashaddress import convert
from keygen.crypto_coin import CryptoCoin
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, BitcoinConf, Bip44Coins, WifDecoder, Bip44, \
    Base58Encoder, BitcoinCashConf

from keygen.wif_validator import is_compressed_wif


class BchCoinService(CoinService):

    def generate(self):
        # Generate random mnemonic
        mnemonic = Bip39MnemonicGenerator.FromWordsNumber(12)

        # Generate seed from mnemonic
        seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

        # Generate BIP44 master keys
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN_CASH)

        address = bip_obj_mst.PublicKey().ToAddress().replace('bitcoincash:', '')
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
        decoded_wif = WifDecoder.Decode(wif_str=private_key, net_addr_ver=BitcoinCashConf.WIF_NET_VER.Main())
        key_pair = Bip44.FromAddressPrivKey(decoded_wif, Bip44Coins.BITCOIN_CASH)
        address = key_pair.PublicKey().ToAddress().replace('bitcoincash:', '')
        return CryptoCoin(address, private_key)

    @staticmethod
    def get_uncompressed_coin(private_key):
        print("Warning Uncompressed key")
        config_alias = BitcoinConf
        coin_type = Bip44Coins.BITCOIN
        decodedWif = WifDecoder.Decode(wif_str=private_key, net_addr_ver=config_alias.WIF_NET_VER.Main())
        bip44_mst = Bip44.FromAddressPrivKey(decodedWif, coin_type)
        to_hex = bip44_mst.PublicKey().RawUncompressed().ToBytes()
        pub_key_bytes = b'\x04' + to_hex
        legacy_address = Base58Encoder.CheckEncode(
            config_alias.P2PKH_NET_VER.Main() + CryptoUtils.Hash160(pub_key_bytes))
        address = convert.to_cash_address(legacy_address).replace('bitcoincash:', '')
        return CryptoCoin(address, private_key)


