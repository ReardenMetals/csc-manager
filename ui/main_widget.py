import tkinter
from tkinter import ttk

from ui.coin_checker_widget import CoinCheckerWidget
from ui.log_widget import LogWidget


class MainWidget:

    def __init__(self, frame, currencies=None, on_qr_code_scanned=None, on_currency_selected=None, on_refreshed=None):

        self.frame = frame

        self.tabControl = ttk.Notebook(frame)

        self.coin_checker_frame = tkinter.Frame(self.tabControl)

        self.coin_checker_widget = CoinCheckerWidget(self.coin_checker_frame,
                                                     currencies=currencies,
                                                     on_currency_selected=on_currency_selected,
                                                     on_qr_code_scanned=on_qr_code_scanned,
                                                     on_refreshed=on_refreshed)

        self.coin_checker_frame.pack()

        self.keygen_frame = tkinter.Frame(self.tabControl)
        self.update_frame = ttk.Frame(self.tabControl)

        self.tabControl.add(self.coin_checker_frame, text='Coin Checker')
        self.tabControl.add(self.keygen_frame, text='KeyGen')
        self.tabControl.add(self.update_frame, text='Update')

        self.tabControl.pack()

        # Log frame
        bottom_frame_width = 650
        log_frame = tkinter.Frame(self.frame, height=300, width=bottom_frame_width, borderwidth=3, bg='GRAY')

        self.log_widget = LogWidget(log_frame, frame_width=bottom_frame_width)
        log_frame.pack(fill=tkinter.BOTH, expand=True)



    def set_currency(self, currency):
        self.coin_checker_widget.set_currency(currency)

    def set_action_title(self, title):
        self.coin_checker_widget.set_action_title(title)

    def show_none(self):
        self.coin_checker_widget.show_none()

    def show_correct(self):
        self.coin_checker_widget.show_correct()

    def show_incorrect(self):
        self.coin_checker_widget.show_incorrect()

    def show_coin_details_info(self, private_key, snip, address):
        self.coin_checker_widget.show_coin_details_info(private_key, snip, address)

    def add_log(self, text):
        self.log_widget.add_log(text)
