from keygen.crypto_coin_factory import CoinFactory

import pygame

class RecoveryController:
    def __init__(self, root, window):
        self.root = root
        self.window = window

    def init(self):
        currencies = CoinFactory.get_available_currencies()
        self.currency = currencies[0]

        self.select_currency(self.currency)


    def on_currency_selected(self, currency):
        print("on_currency_selected")
        # self.select_currency(currency)

    def on_refreshed(self):
        print("on_refreshed")
        # self.change_state(States.SCAN_COIN_STATE)

    def select_currency(self, currency):
        self.currency = currency
        self.coin_service = CoinFactory.get_coin_service(self.currency)
        # self.root.set_currency(currency)
        print("Selected currency: ", self.currency)

    def on_qr_code_scanned(self, qr_code_text):
        # self.state.on_qr_code_scanned(qr_code_text)
        print("on_qr_code_scanned")