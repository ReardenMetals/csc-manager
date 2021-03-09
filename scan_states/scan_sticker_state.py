from scan_states.scan_state import ScanState
from scan_states.states_enum import States


class ScanStickerState(ScanState):

    def __init__(self, context):
        super().__init__(context)
        self.sticker_processing = False

    def init_state(self):
        super().init_state()
        self.context.set_action_title("Scan Sticker")
        self.context.show_coin_info()

    def on_qr_code_scanned(self, qr_code_text):
        super().on_qr_code_scanned(qr_code_text)
        if qr_code_text != self.context.get_private_key():
            if not self.sticker_processing:
                self.sticker_processing = True
                self.on_address_scanned(qr_code_text)
        else:
            print("Sticker public key can be the same as private key")

    def on_address_scanned(self, address_text):
        print("Fetched address: ", self.context.get_fetched_address())
        print("Scanned address: ", address_text)
        if self.context.get_fetched_address() == address_text:
            print("fetched_address == address_text")
            self.change_state(States.APPLY_STICKER_STATE)
        else:
            print("fetched_address != address_text")
            self.change_state(States.MISMATCH_STATE)