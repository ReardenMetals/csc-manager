import tkinter

from controller.recovery_controller import RecoveryController
from keygen.crypto_coin_factory import CoinFactory
from ui.recovery.header_widget import HeaderWidget
from ui.recovery.footer_widget import FooterWidget

from tkinter import messagebox


class RecoveryWidget:
    def __init__(self, recovery_frame):
        self.recovery_frame = recovery_frame
        top_frame = tkinter.Frame(self.recovery_frame, borderwidth=3)

        currencies = CoinFactory.get_available_currencies()
        self.currencies = currencies

        self.recovery_controller = RecoveryController(self, recovery_frame)

        self.header_widget = HeaderWidget(top_frame,
                                          currencies=self.currencies,
                                          on_currency_selected=self.recovery_controller.on_currency_selected,
                                          on_refreshed=self.recovery_controller.on_refreshed,
                                          on_saved=self.recovery_controller.on_saved)

        top_frame.pack(fill=tkinter.X)

        bottom_frame_width = 650
        bottom_frame_height = 350

        bottom_frame = tkinter.Frame(self.recovery_frame, height=bottom_frame_height, width=bottom_frame_width,
                                     borderwidth=3)

        self.footer_widget = FooterWidget(bottom_frame, frame_width=bottom_frame_width,
                                          frame_height=bottom_frame_height,
                                          on_qr_code_scanned=self.recovery_controller.on_qr_code_scanned)
        bottom_frame.pack(fill=tkinter.BOTH, expand=True)

        self.recovery_controller.init()
        recovery_frame.out_callback = self.release_camera
        recovery_frame.in_callback = self.init_camera

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

    def init_camera(self):
        print("init recovery camera")
        self.footer_widget.camera_widget.resume()

    def release_camera(self):
        print("release recovery camera")
        self.footer_widget.camera_widget.pause()

    @staticmethod
    def show_success():
        messagebox.showinfo("Recovery success", "Crypto coins recovered in to files!")

    def set_scanned_count(self, count):
        self.header_widget.set_scanned_count(count=count)
