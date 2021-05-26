from scan_states.recovery.scan_state import ScanState
from scan_states.recovery.states_enum import States


class ScanCoinErrorState(ScanState):

    def __init__(self, context):
        super().__init__(context)

    def init_state(self):
        super().init_state()
        self.context.set_action_title("Scan Error")
        self.context.show_incorrect()
        self.context.play_error_song()
        self.context.start_async(self.delay_task())

    async def delay_task(self):
        await self.context.sleep(1000)
        self.change_state(States.SCAN_COIN_STATE)