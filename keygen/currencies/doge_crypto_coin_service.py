from keygen.crypto_coin import CryptoCoin
from keygen.crypto_coin_service import CoinService
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes, WifDecoder, \
    DogecoinConf


class DogeCoinService(CoinService):

    def generate(self):
        # Generate random mnemonic
        mnemonic = Bip39MnemonicGenerator.FromWordsNumber(12)

        # Generate seed from mnemonic
        seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

        # Generate BIP44 master keys
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.DOGECOIN)

        address = bip_obj_mst.PublicKey().ToAddress()
        wif = bip_obj_mst.PrivateKey().ToWif()
        seed = mnemonic

        return CryptoCoin(address, wif, seed)

    def get_coin(self, private_key):
        decodedWif = WifDecoder.Decode(wif_str=private_key, net_addr_ver = DogecoinConf.WIF_NET_VER.Main())
        keyPair = Bip44.FromAddressPrivKey(decodedWif, Bip44Coins.DOGECOIN)
        address = keyPair.PublicKey().ToAddress()
        return CryptoCoin(address, private_key)
