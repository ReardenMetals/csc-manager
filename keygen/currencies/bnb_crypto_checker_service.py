from keygen.crypto_coin import CryptoCoin
from keygen.crypto_check_service import CoinService
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes, WifDecoder


class BnbCoinService(CoinService):

    def get_coin(self, private_key):
        addr = Bip44.FromExtendedKey(private_key, Bip44Coins.BINANCE_COIN)
        address = addr.PublicKey().ToAddress()
        return CryptoCoin(address, private_key)
