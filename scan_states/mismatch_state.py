from scan_states.scan_state import ScanState
from scan_states.states_enum import States


class MismatchState(ScanState):

    def __init__(self, context):
        super().__init__(context)

    def init_state(self):
        super().init_state()
        self.context.set_action_title("Mismatch")
        self.context.show_incorrect()
        self.context.play_error_song()
        self.context.start_async(self.delay_task())

    async def delay_task(self):
        await self.context.sleep(2000)
        self.change_state(States.SCAN_STICKER_STATE)
