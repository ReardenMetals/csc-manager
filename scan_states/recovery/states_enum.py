from enum import Enum


class States(Enum):
    SCAN_COIN_STATE = 'ScanCoinState',
    APPLY_COIN_STATE = 'ApplyCoinState',
    SCAN_COIN_ERROR_STATE = 'ScanCoinErrorState'
