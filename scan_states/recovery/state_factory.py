from scan_states.recovery.context import Context
from scan_states.recovery.apply_coin_state import ApplyCoinState
from scan_states.recovery.scan_coin_error_state import ScanCoinErrorState
from scan_states.recovery.scan_coin_state import ScanCoinState
from scan_states.recovery.states_enum import States


def get_state(state_name: States, context: Context):
    if state_name == States.SCAN_COIN_STATE:
        return ScanCoinState(context)
    if state_name == States.APPLY_COIN_STATE:
        return ApplyCoinState(context)
    if state_name == States.SCAN_COIN_ERROR_STATE:
        return ScanCoinErrorState(context)
