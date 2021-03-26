import os


class CoinImageUtil:

    @staticmethod
    def get_path(a, *p):
        return os.path.join(a, *p)

    @staticmethod
    def get_coin_image_by_currency(currency: str):
        currency_lower = currency.lower()
        file_name = 'coin-{}.png'.format(currency_lower)
        return CoinImageUtil.get_path('resources', 'img', file_name)
