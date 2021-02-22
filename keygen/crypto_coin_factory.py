from keygen.currencies.bnb_crypto_coin_service import BnbCoinService
from keygen.currencies.btc_crypto_coin_service import BtcCoinService
from keygen.currencies.bch_crypto_coin_service import BchCoinService
from keygen.currencies.eos_crypto_coin_service import EosCoinService
from keygen.currencies.ltc_crypto_coin_service import LtcCoinService
from keygen.currencies.club_crypto_coin_service import ClubCoinService
from keygen.currencies.dash_crypto_coin_service import DashCoinService
from keygen.currencies.eth_crypto_coin_service import EthCoinService
from keygen.currencies.usdt_crypto_coin_service import UsdtCoinService
from keygen.currencies.xmr_crypto_coin_service import XmrCoinService
from keygen.currencies.pote_crypto_coin_service import PoteCoinService
from keygen.currencies.waves_crypto_coin_service import WavesCoinService
from keygen.currencies.doge_crypto_coin_service import DogeCoinService
from keygen.currencies.xrp_crypto_coin_service import RippleCoinService


class CoinFactory:
    def __init__(self):
        pass

    @staticmethod
    def get_available_currencies():
        return ['BTC', 'BCH', 'LTC', 'CLUB', 'DASH', 'ETH', 'XMR', 'WAVES', 'POTE', 'DOGE', 'USDT', 'BNB', 'EOS', 'XRP']

    @staticmethod
    def get_coin_service(currency):
        if currency == "BTC":
            return BtcCoinService()
        if currency == "BCH":
            return BchCoinService()
        if currency == "LTC":
            return LtcCoinService()
        if currency == "CLUB":
            return ClubCoinService()
        if currency == "DASH":
            return DashCoinService()
        if currency == "ETH":
            return EthCoinService()
        if currency == "XMR":
            return XmrCoinService()
        if currency == "WAVES":
            return WavesCoinService()
        if currency == "POTE":
            return PoteCoinService()
        if currency == "DOGE":
            return DogeCoinService()
        if currency == "USDT":
            return UsdtCoinService()
        if currency == "BNB":
            return BnbCoinService()
        if currency == "EOS":
            return EosCoinService()
        if currency == "XRP":
            return RippleCoinService()
        raise Exception("Coin not supported")
