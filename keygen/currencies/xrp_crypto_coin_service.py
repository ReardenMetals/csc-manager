from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, WifDecoder, \
    RippleConf

from keygen.crypto_coin import CryptoCoin
from keygen.crypto_coin_service import CoinService


class RippleCoinService(CoinService):

    def generate(self):
        # Generate random mnemonic
        mnemonic = Bip39MnemonicGenerator.FromWordsNumber(12)

        # Generate seed from mnemonic
        seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

        # Generate BIP44 master keys
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.RIPPLE)

        address = bip_obj_mst.PublicKey().ToAddress()
        key = bip_obj_mst.PrivateKey()
        wif = key.ToExtended()
        seed = mnemonic

        return CryptoCoin(address, wif, seed)

    def get_coin(self, private_key):
        key_pair = Bip44.FromExtendedKey(private_key, Bip44Coins.RIPPLE)
        address = key_pair.PublicKey().ToAddress()
        return CryptoCoin(address, private_key)
