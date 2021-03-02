from logger import logger
from scan_states.context import Context
from scan_states.states_enum import States


class ScanState:

    def __init__(self, context: Context):
        self.context = context

    def init_state(self):
        logger.log("Init new state:", self)

    def change_state(self, new_state: States):
        self.context.change_state(new_state)

    def on_qr_code_scanned(self, qr_code_text):
        logger.log("ScanState: ", qr_code_text)