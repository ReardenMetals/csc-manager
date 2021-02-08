from keygen.currencies.bch_crypto_keygen_service import BchCryptoKeygenService
from keygen.currencies.btc_crypto_keygen_service import BtcCryptoKeygenService
from keygen.currencies.club_crypto_keygen_service import ClubCryptoKeygenService
from keygen.currencies.dash_crypto_keygen_service import DashCryptoKeygenService
from keygen.currencies.eth_crypto_keygen_service import EthCryptoKeygenService
from keygen.currencies.ltc_crypto_keygen_service import LtcCryptoKeygenService
from keygen.currencies.pote_crypto_keygen_service import PoteCryptoKeygenService
from keygen.currencies.usdt_crypto_keygen_service import UsdtCryptoKeygenService
from keygen.currencies.waves_crypto_keygen_service import WavesCryptoKeygenService
from keygen.currencies.xmr_crypto_keygen_service import XmrCryptoKeygenService
from keygen.currencies.bnb_crypto_keygen_service import BnbCryptoKeygenService
from keygen.currencies.eos_crypto_keygen_service import EosCryptoKeygenService




class CryptoKeygenFactory:
    def __init__(self):
        pass

    @staticmethod
    def get_crypto_keygen_service(currency):
        if currency == "BTC":
            return BtcCryptoKeygenService()
        if currency == "BCH":
            return BchCryptoKeygenService()
        if currency == "LTC":
            return LtcCryptoKeygenService()
        if currency == "DASH":
            return DashCryptoKeygenService()
        if currency == "CLUB":
            return ClubCryptoKeygenService()
        if currency == "ETH":
            return EthCryptoKeygenService()
        if currency == "XMR":
            return XmrCryptoKeygenService()
        if currency == "WAVES":
            return WavesCryptoKeygenService()
        if currency == "POTE":
            return PoteCryptoKeygenService()
        if currency == "USDT":
            return UsdtCryptoKeygenService()
        if currency == "BNB":
            return BnbCryptoKeygenService()
        if currency == "EOS":
            return EosCryptoKeygenService()
        raise Exception("Coin not supported")