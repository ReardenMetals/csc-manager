from btc_crypto_keygen_service import BtcCryptoKeygenService


class CryptoKeygenFactory:
    def __init__(self):
        pass

    @staticmethod
    def get_crypto_keygen_service(currency):
        if currency == "BTC":
            return BtcCryptoKeygenService()
        if currency == "ETH":
            return  # TODO Include another services
