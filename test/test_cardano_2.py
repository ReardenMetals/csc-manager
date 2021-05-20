from mnemonic import Mnemonic
from hashlib import blake2b, sha512
from base58 import b58decode
from pbkdf2 import PBKDF2
from chacha20poly1305 import ChaCha20Poly1305
from sys import argv
import cbor
import hmac
import ed25519
words = 'provide lumber used piece fossil crop defy tornado focus say kitchen gentle'
addr = 'DdzFFzCqrhsfE419Z4WHVTQVP4wnXGqx7pDVTLhNLaLxVxazViMiYhd1zr4bcRpqEHLbZ6DvaAdLro9JZq7q9oD6hopD1wzQu7yiQKxP'
entropy = Mnemonic('english').to_entropy(words)
cborEnt = cbor.dumps(bytes(entropy))
seed = blake2b(cborEnt, digest_size=32)
cborSeed = cbor.dumps(seed.digest())
buf = hmac.new(cborSeed, b'Root Seed Chain 5', sha512).digest()
buf_l, buf_r = buf[:32], buf[32:]
bip32 = ed25519.SigningKey(buf_l)
xpub = bip32.vk_s + buf_r
decodedAddr = b58decode(addr)
loadedAddr = cbor.loads(decodedAddr)
address = cbor.loads(loadedAddr[0].value)
# print(address)
addrAttributes = cbor.loads(address[1][1])
# print(addrAttributes)
nonce = b'serokellfore'
hdpass = PBKDF2(xpub, 'address-hashing', iterations=500, digestmodule=sha512).read(32)
cip = ChaCha20Poly1305(hdpass)

decryptedAttr = cip.decrypt(nonce, addrAttributes)
print(decryptedAttr)
c=cbor.loads(decryptedAttr)
# print(c)
# [2147483648, 2147483648]