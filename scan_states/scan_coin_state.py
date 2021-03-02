from scan_states.context import Context
from scan_states.scan_state import ScanState
from scan_states.states_enum import States
from logger import logger

class ScanCoinState(ScanState):

    def __init__(self, context: Context):
        super().__init__(context)
        self.private_key_text = None
        self.coin_processing = False

    def init_state(self):
        super().init_state()
        self.context.set_action_title("Scan Coin")
        self.context.show_none()
        self.context.set_fetched_address(None)
        self.context.set_coin_private_key(None)

    def on_qr_code_scanned(self, qr_code_text):
        super().on_qr_code_scanned(qr_code_text)
        if not self.coin_processing:
            self.coin_processing = True
            self.on_private_key_scanned(qr_code_text)

    def on_private_key_scanned(self, private_key_text):
        if private_key_text != self.private_key_text:
            logger.log("Start processing: get_address_and_id")
            self.private_key_text = private_key_text
            logger.log('private_key:', self.private_key_text)
            private_key = self.private_key_text
            self.context.show_coin_private_key(private_key)
            self.context.start_async(self.load_address_from_private_async(private_key))

    async def load_address_from_private_async(self, private_key):
        address, asset_id, error = await self.context.run_in_thread(lambda: self.load_address_and_id(private_key))
        if error is None:
            logger.log('address, asset_id')
            logger.log(address, asset_id)
            if address is not None and asset_id is not None:
                self.context.show_coin_details_info(private_key, asset_id, address)
                self.context.play_success_song()
                self.change_state(States.SCAN_STICKER_STATE)
        else:
            self.context.show_coin_details_info('error', 'error', 'error')
            self.change_state(States.SCAN_COIN_ERROR_STATE)

    def load_address_and_id(self, private_key):
        try:
            address, asset_id = self.context.load_address_and_id(private_key)
            error = None
            return address, asset_id, error
        except Exception:
            address = None
            asset_id = None
            error = "Error loading address"
            logger.log(error)
            return address, asset_id, error