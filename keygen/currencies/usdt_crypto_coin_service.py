from pywallet.utils import Wallet
from pywallet.utils.keys import PrivateKey

from keygen.crypto_coin import CryptoCoin
from keygen.crypto_coin_service import CoinService

from pywallet import wallet


class UsdtCoinService(CoinService):

    def generate(self):
        seed = wallet.generate_mnemonic()
        w = wallet.create_wallet(network="omni", seed=seed, children=1)
        wif = w.get('wif').decode("utf-8")
        address = w.get('address')
        seed = w.get('seed')
        return CryptoCoin(address, wif, seed)

    def get_coin(self, private_key):
        wif = private_key
        key = PrivateKey.from_wif(wif=private_key, network=Wallet.get_network('OMNI'))
        address = key.get_public_key().to_address()
        return CryptoCoin(address, wif, '')
