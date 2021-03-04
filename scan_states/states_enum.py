from enum import Enum


class States(Enum):
    APPLY_STICKER_STATE = 'ApplyStickerState',
    MISMATCH_STATE = 'MismatchState',
    SCAN_COIN_ERROR_STATE = 'ScanCoinErrorState',
    SCAN_COIN_STATE = 'ScanCoinState',
    SCAN_STICKER_STATE = 'ScanStickerState'
