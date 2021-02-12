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
from keygen.currencies.bnb_38_crypto_keygen_service import NewBnbCryptoKeygenService
from keygen.currencies.btc_38_crypto_keygen_service import NewBtcCryptoKeygenService
from keygen.currencies.bch_38_crypto_keygen_service import NewBchCryptoKeygenService
from keygen.currencies.club_38_crypto_keygen_service import NewClubCryptoKeygenService
from keygen.currencies.doge_38_crypto_keygen_service import NewDogeCryptoKeygenService
from keygen.currencies.eos_38_crypto_keygen_service import NewEosCryptoKeygenService
from keygen.currencies.ltc_38_crypto_keygen_service import NewLtcCryptoKeygenService
from keygen.currencies.dash_38_crypto_keygen_service import NewDashCryptoKeygenService
from keygen.currencies.eth_38_crypto_keygen_service import NewEthCryptoKeygenService
from keygen.currencies.pote_38_crypto_keygen_service import NewPoteCryptoKeygenService
from keygen.currencies.usdt_38_crypto_keygen_service import NewUsdtCryptoKeygenService
from keygen.currencies.waves_38_crypto_keygen_service import NewWavesCryptoKeygenService
from keygen.currencies.xmr_38_crypto_keygen_service import NewXmrCryptoKeygenService


class CryptoKeygenFactory:
    def __init__(self):
        pass

    @staticmethod
    def get_crypto_keygen_service(currency):
        if currency == "BTC":
            return NewBtcCryptoKeygenService()
        if currency == "BCH":
            return NewBchCryptoKeygenService()
        if currency == "LTC":
            return NewLtcCryptoKeygenService()
        if currency == "DASH":
            return NewDashCryptoKeygenService()
        if currency == "CLUB": #Python2.7 version
            return NewClubCryptoKeygenService()
        if currency == "ETH":
            return NewEthCryptoKeygenService()
        if currency == "XMR":
            return NewXmrCryptoKeygenService()
        if currency == "WAVES": #Python2.7 low priority
            return NewWavesCryptoKeygenService()
        if currency == "POTE": #Python2.7
            return NewPoteCryptoKeygenService()
        if currency == "USDT":
            return NewUsdtCryptoKeygenService()
        if currency == "BNB":
            return NewBnbCryptoKeygenService()
        if currency == "EOS":
            return NewEosCryptoKeygenService()
        if currency == "DOGE":
            return NewDogeCryptoKeygenService()
        raise Exception("Coin not supported")