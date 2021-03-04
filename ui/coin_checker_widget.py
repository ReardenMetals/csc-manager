import tkinter
from tkinter import ttk

from ui.footer_widget import FooterWidget
from ui.header_widget import HeaderWidget

class CoinCheckerWidget:
    def __init__(self, coin_checker_frame, currencies=None, on_qr_code_scanned=None, on_currency_selected=None, on_refreshed=None):

        self.coin_checker_frame = coin_checker_frame

        top_frame = tkinter.Frame(self.coin_checker_frame, borderwidth=3)

        self.currencies = currencies

        self.header_widget = HeaderWidget(top_frame,
                                          currencies=self.currencies,
                                          on_currency_selected=on_currency_selected,
                                          on_refreshed=on_refreshed)
        top_frame.pack(fill=tkinter.X)

        bottom_frame_width = 650
        bottom_frame_height = 350

        bottom_frame = tkinter.Frame(self.coin_checker_frame, height=bottom_frame_height, width=bottom_frame_width,
                                     borderwidth=3)
        self.footer_widget = FooterWidget(bottom_frame, frame_width=bottom_frame_width,
                                          frame_height=bottom_frame_height, on_qr_code_scanned=on_qr_code_scanned)
        bottom_frame.pack(fill=tkinter.BOTH, expand=True)

    def set_currency(self, currency):
        self.footer_widget.set_currency(currency)

    def set_action_title(self, title):
        self.footer_widget.set_action_title(title)

    def show_none(self):
        self.footer_widget.show_none()

    def show_correct(self):
        self.footer_widget.show_correct()

    def show_incorrect(self):
        self.footer_widget.show_incorrect()

    def show_coin_details_info(self, private_key, snip, address):
        self.footer_widget.show_coin_details_info(private_key, snip, address)