# from keygen.currencies.bch_crypto_keygen_service import BchCryptoKeygenService
# from keygen.currencies.btc_crypto_keygen_service import BtcCryptoKeygenService
# from keygen.currencies.club_crypto_keygen_service import ClubCryptoKeygenService
# from keygen.currencies.dash_crypto_keygen_service import DashCryptoKeygenService
# from keygen.currencies.doge_crypto_keygen_service import DogeCryptoKeygenService
# from keygen.currencies.eth_crypto_keygen_service import EthCryptoKeygenService
# from keygen.currencies.ltc_crypto_keygen_service import LtcCryptoKeygenService
# from keygen.currencies.pote_crypto_keygen_service import PoteCryptoKeygenService
# from keygen.currencies.usdt_crypto_keygen_service import UsdtCryptoKeygenService
# from keygen.currencies.waves_crypto_keygen_service import WavesCryptoKeygenService
# from keygen.currencies.xmr_crypto_keygen_service import XmrCryptoKeygenService
# from keygen.currencies.bnb_crypto_keygen_service import BnbCryptoKeygenService
# from keygen.currencies.eos_crypto_keygen_service import EosCryptoKeygenService
from keygen.currencies.bnb_38_crypto_keygen_service import Bnb38CryptoKeygenService
from keygen.currencies.btc_38_crypto_keygen_service import Btc38CryptoKeygenService
from keygen.currencies.bch_38_crypto_keygen_service import Bch38CryptoKeygenService
from keygen.currencies.club_38_crypto_keygen_service import Club38CryptoKeygenService
from keygen.currencies.doge_38_crypto_keygen_service import Doge38CryptoKeygenService
from keygen.currencies.eos_38_crypto_keygen_service import Eos38CryptoKeygenService
from keygen.currencies.ltc_38_crypto_keygen_service import Ltc38CryptoKeygenService
from keygen.currencies.dash_38_crypto_keygen_service import Dash38CryptoKeygenService
from keygen.currencies.eth_38_crypto_keygen_service import Eth38CryptoKeygenService
from keygen.currencies.pote_38_crypto_keygen_service import Pote38CryptoKeygenService
from keygen.currencies.usdt_38_crypto_keygen_service import Usdt38CryptoKeygenService
from keygen.currencies.waves_38_crypto_keygen_service import Waves38CryptoKeygenService
from keygen.currencies.xmr_38_crypto_keygen_service import Xmr38CryptoKeygenService


class CryptoKeygenFactory:
    def __init__(self):
        pass

    @staticmethod
    def get_crypto_keygen_service(currency):
        if currency == "BTC":
            return Btc38CryptoKeygenService()
        if currency == "BCH":
            return Bch38CryptoKeygenService()
        if currency == "LTC":
            return Ltc38CryptoKeygenService()
        if currency == "DASH":
            return Dash38CryptoKeygenService()
        if currency == "CLUB":  #FIXME migrate from Python2.7 version
            return Club38CryptoKeygenService()
        if currency == "ETH":
            return Eth38CryptoKeygenService()
        if currency == "XMR":
            return Xmr38CryptoKeygenService()
        if currency == "WAVES":  #FIXME migrate from Python2.7 low priority
            return Waves38CryptoKeygenService()
        if currency == "POTE":  #FIXME migrate from Python2.7
            return Pote38CryptoKeygenService()
        if currency == "USDT": #FIXME migrate from Python3.6
            return Usdt38CryptoKeygenService()
        if currency == "BNB":
            return Bnb38CryptoKeygenService()
        if currency == "EOS":
            return Eos38CryptoKeygenService()
        if currency == "DOGE":
            return Doge38CryptoKeygenService()
        raise Exception("Coin not supported")