from scan_states.recovery.context import Context
from scan_states.recovery.states_enum import States


class ScanState:

    def __init__(self, context: Context):
        self.context = context

    def init_state(self):
        # print("Init new state:", self)
        pass

    def change_state(self, new_state: States):
        self.context.change_state(new_state)

    def on_qr_code_scanned(self, qr_code_text):
        print("ScanState: ", qr_code_text)
