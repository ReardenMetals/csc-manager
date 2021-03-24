from scan_states.states_enum import States


class Context:
    def __init__(self):
        pass

    def clear_data(self):
        pass

    def change_state(self, new_state: States):
        pass

    def get_fetched_address(self):
        pass

    def get_private_key(self):
        pass

    def set_coin_private_key(self, private_key):
        pass

    def set_fetched_snip(self, snip):
        pass

    def set_fetched_address(self, fetched_address):
        pass

    def load_address_and_id(self, private_key):
        pass

    def set_action_title(self, title: str):
        pass

    def show_none(self):
        pass

    def show_correct(self):
        pass

    def show_incorrect(self):
        pass

    def show_coin_info(self):
        pass

    def show_error(self):
        pass

    def show_coin_private_key(self):
        pass

    def play_success_song(self):
        pass

    def play_error_song(self):
        pass

    def start_async(self, task):
        pass

    def run_in_thread(self, func):
        pass

    def sleep(self, milliseconds):
        pass
