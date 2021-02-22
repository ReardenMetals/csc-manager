from keygen.crypto_coin import CryptoCoin
from keygen.crypto_check_service import CoinService
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes, WifDecoder, \
    DogecoinConf


class DogeCoinService(CoinService):

    def get_coin(self, private_key):
        decodedWif = WifDecoder.Decode(wif_str=private_key, net_addr_ver = DogecoinConf.WIF_NET_VER.Main())
        keyPair = Bip44.FromAddressPrivKey(decodedWif, Bip44Coins.DOGECOIN)
        address = keyPair.PublicKey().ToAddress()
        return CryptoCoin(address, private_key)
