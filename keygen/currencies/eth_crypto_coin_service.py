from keygen.crypto_coin import CryptoCoin
from keygen.crypto_coin_service import CoinService

# for ethereum wallets
from ecdsa import SigningKey, SECP256k1
import sha3
import codecs

import re


class EthCoinService(CoinService):

    def generate(self):
        keccak = sha3.keccak_256()
        priv = SigningKey.generate(curve=SECP256k1)
        pub = priv.get_verifying_key().to_string()
        keccak.update(pub)
        address = keccak.hexdigest()[24:]
        priv_hex = str(codecs.encode(priv.to_string(), 'hex'))[2:-1]
        return CryptoCoin("0x{}".format(address), priv_hex)

    def get_coin(self, private_key):
        keccak = sha3.keccak_256()
        decoded_private_key = codecs.decode(private_key, 'hex')
        priv = SigningKey.from_string(decoded_private_key, curve=SECP256k1)
        pub = priv.get_verifying_key().to_string()
        keccak.update(pub)
        address = keccak.hexdigest()[24:]
        priv_hex = codecs.encode(priv.to_string(), 'hex')
        return CryptoCoin("0x{}".format(address), priv_hex)

    def generate_asset_id(self, coin):
        return re.search('^0x(\\w{6}).+$', coin.address).group(1)
