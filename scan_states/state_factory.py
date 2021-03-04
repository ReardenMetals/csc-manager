from scan_states.apply_sticker_state import ApplyStickerState
from scan_states.context import Context
from scan_states.mismatch_state import MismatchState
from scan_states.scan_coin_error_state import ScanCoinErrorState
from scan_states.scan_coin_state import ScanCoinState
from scan_states.scan_sticker_state import ScanStickerState
from scan_states.states_enum import States


def get_state(state_name: States, context: Context):
    if state_name == States.APPLY_STICKER_STATE:
        return ApplyStickerState(context)
    if state_name == States.MISMATCH_STATE:
        return MismatchState(context)
    if state_name == States.SCAN_COIN_ERROR_STATE:
        return ScanCoinErrorState(context)
    if state_name == States.SCAN_COIN_STATE:
        return ScanCoinState(context)
    if state_name == States.SCAN_STICKER_STATE:
        return ScanStickerState(context)
