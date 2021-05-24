from scan_states.recovery.scan_state import ScanState
from scan_states.recovery.states_enum import States


class ApplyCoinState(ScanState):

    def __init__(self, context):
        super().__init__(context)

    def init_state(self):
        super().init_state()
        self.context.set_action_title("Apply Coin")
        self.context.show_correct()
        self.context.play_success_song()
        self.context.start_async(self.delay_task())

    async def delay_task(self):
        await self.context.sleep(1000)
        self.change_state(States.SCAN_COIN_STATE)
