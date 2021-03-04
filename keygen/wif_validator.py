from bip_utils import Base58Decoder
from bip_utils.utils import KeyUtils


def is_compressed_wif(wif: str):
    key_bytes = Base58Decoder.CheckDecode(wif)
    key_bytes = key_bytes[1:]
    return not KeyUtils.IsPrivate(key_bytes)