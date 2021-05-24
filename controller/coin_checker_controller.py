import asynctkinter as at
import pygame

from keygen.crypto_coin_factory import CoinFactory
from scan_states.context import Context
from scan_states.state_factory import get_state
from scan_states.states_enum import States


class CoinCheckerController(Context):
    def __init__(self, root, window):
        super().__init__()
        self.root = root
        self.window = window

        self.state = None
        self.coin_service = None
        self.currency = None

        self.fetched_address = None
        self.private_key = None
        self.snip = None

    def init(self):
        currencies = CoinFactory.get_available_currencies()
        self.currency = currencies[0]

        self.select_currency(self.currency)

    def on_currency_selected(self, currency):
        self.select_currency(currency)

    def on_refreshed(self):
        self.change_state(States.SCAN_COIN_STATE)

    def select_currency(self, currency):
        self.currency = currency
        self.coin_service = CoinFactory.get_coin_service(self.currency)
        self.change_state(States.SCAN_COIN_STATE)
        self.root.set_currency(currency)
        print("Selected currency: ", self.currency)

    def on_qr_code_scanned(self, qr_code_text):
        self.state.on_qr_code_scanned(qr_code_text)

    def clear_data(self):
        self.fetched_address = None
        self.private_key = None
        self.snip = None

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

    def set_fetched_snip(self, snip):
        self.snip = snip

    def load_address_and_id(self, private_key):
        return self.coin_service.get_address_and_id(private_key)

    def set_action_title(self, title: str):
        self.root.set_action_title(title)

    def show_none(self):
        self.root.show_none()

    def show_correct(self):
        self.root.show_correct()

    def show_incorrect(self):
        self.root.show_incorrect()

    def show_coin_info(self):
        private_key = self.private_key
        snip = self.snip
        address = self.fetched_address
        self.root.show_coin_details_info(private_key=private_key, snip=snip, address=address)

    def show_error(self):
        self.root.show_coin_details_info('error', 'error', 'error')

    def show_coin_private_key(self):
        private_key = self.private_key
        self.root.show_coin_details_info(private_key, "...", "...")

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

    @staticmethod
    def _play_song(file_name: str):
        music = pygame.mixer.music
        music.load(file_name)
        music.play()
