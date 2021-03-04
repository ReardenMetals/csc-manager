from scan_states.scan_state import ScanState
from scan_states.states_enum import States


class ScanCoinErrorState(ScanState):

    def __init__(self, context):
        super().__init__(context)

    def init_state(self):
        super().init_state()
        self.context.play_error_song()
        self.change_state(States.SCAN_COIN_STATE)
