#for ethereum wallets
from ecdsa import SigningKey, SECP256k1
import sha3
import codecs

# keccak = sha3.keccak_256()
# priv = SigningKey.generate(curve=SECP256k1)
# pub = priv.get_verifying_key().to_string()
# keccak.update(pub)
# address = keccak.hexdigest()[24:]
# priv_hex = codecs.encode(priv.to_string(), 'hex')
# addr=("0x{}".format(address))

keccak = sha3.keccak_256()
decoded_private_key = codecs.decode('813c58c6edc5f2689d54ca06efddbfb56feae888abfe30ce8e293224919ec818', 'hex')
priv = SigningKey.from_string(decoded_private_key, curve=SECP256k1)
pub = priv.get_verifying_key().to_string()
keccak.update(pub)
address = keccak.hexdigest()[24:]
priv_hex = codecs.encode(priv.to_string(), 'hex')
addr=("0x{}".format(address))

print(addr)
# print(priv_hex)

# 0x96fe96e97a107fff1f4c619ad1d5c0d568219f53
# 813c58c6edc5f2689d54ca06efddbfb56feae888abfe30ce8e293224919ec818