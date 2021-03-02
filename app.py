from keygen.crypto_coin_factory import CoinFactory
from logger import logger
from scan_states.context import Context
from scan_states.state_factory import get_state
from scan_states.states_enum import States
from ui.main_widget import MainWidget
import asynctkinter as at
import pygame


class App(Context):

    def __init__(self, window_title, window):
        super().__init__()

        self.window = window
        # self.window.resizable(False, False)
        self.window.title(window_title)
        logger.set_appender(self)

        currencies = CoinFactory.get_available_currencies()
        self.currency = currencies[0]
        self.main_widget = MainWidget(self.window,
                                      currencies=currencies,
                                      on_currency_selected=self.on_currency_selected,
                                      on_qr_code_scanned=self.on_qr_code_scanned,
                                      on_refreshed=self.on_refreshed)

        self.state = None
        self.fetched_address = None
        self.private_key = None
        self.coin_service = None

        self.select_currency(self.currency)

        pygame.mixer.init()

    def on_currency_selected(self, currency):
        self.select_currency(currency)

    def on_refreshed(self):
        self.change_state(States.SCAN_COIN_STATE)

    def select_currency(self, currency):
        self.currency = currency
        self.coin_service = CoinFactory.get_coin_service(self.currency)
        self.change_state(States.SCAN_COIN_STATE)
        self.main_widget.set_currency(currency)
        print("Selected currency: ", self.currency)

    def on_qr_code_scanned(self, qr_code_text):
        self.state.on_qr_code_scanned(qr_code_text)

    def change_state(self, new_state: States):
        print("New state:", new_state)
        self.state = get_state(new_state, self)
        self.state.init_state()

    def get_private_key(self):
        return self.private_key

    def set_coin_private_key(self, private_key):
        self.private_key = private_key

    def get_fetched_address(self):
        return self.fetched_address

    def set_fetched_address(self, fetched_address):
        self.fetched_address = fetched_address

    def load_address_and_id(self, private_key):
        return self.coin_service.get_address_and_id(private_key)

    def set_action_title(self, title: str):
        self.main_widget.set_action_title(title)

    def show_none(self):
        self.main_widget.show_none()

    def show_correct(self):
        self.main_widget.show_correct()

    def show_incorrect(self):
        self.main_widget.show_incorrect()

    def show_coin_details_info(self, private_key, snip, address):
        self.main_widget.show_coin_details_info(private_key, snip, address)
        self.fetched_address = address

    def show_coin_private_key(self, private_key):
        self.set_coin_private_key(private_key)
        self.main_widget.show_coin_details_info(private_key, "...", "...")

    def play_success_song(self):
        self._play_song("./resources/audio/definite.mp3")

    def play_error_song(self):
        self._play_song("./resources/audio/no-trespassing.mp3")

    def start_async(self, task):
        at.start(task)

    def run_in_thread(self, func):
        return at.run_in_thread(func, after=self.window.after)

    def sleep(self, milliseconds):
        return at.sleep(milliseconds, after=self.window.after)

    def log(self, *args):
        self.main_widget.add_log(' '.join(map(str, *args)))

    @staticmethod
    def _play_song(file_name: str):
        music = pygame.mixer.music
        music.load(file_name)
        music.play()
