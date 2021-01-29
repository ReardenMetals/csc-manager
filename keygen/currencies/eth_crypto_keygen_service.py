from keygen.crypto_coin import CryptoCoin
from keygen.crypto_keygen_service import CryptoKeygenService

#for ethereum wallets
from ecdsa import SigningKey, SECP256k1
import sha3
import codecs

class EthCryptoKeygenService(CryptoKeygenService):

    def generate(self):
        keccak = sha3.keccak_256()
        priv = SigningKey.generate(curve=SECP256k1)
        pub = priv.get_verifying_key().to_string()
        keccak.update(pub)
        address = keccak.hexdigest()[24:]
        priv_hex = codecs.encode(priv.to_string(), 'hex')
        return CryptoCoin("0x{}".format(address), priv_hex)
