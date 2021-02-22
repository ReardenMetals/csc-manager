
from pybitcoin import BitcoinPrivateKey

class DashPublicKey(BitcoinPrivateKey):
    _pubkeyhash_version_byte = 0x4c

private_key = DashPublicKey(private_key='7rDNFgN32tLmknEC3mpm54VqdworVXrTEbyobbcg1mkvMmPZPdj')
# wif = private_key.to_wif()
address = private_key.public_key().address()

print(address)
# print(wif)

# XdRsX38wgENu6FrGx3wx6qnSTz7XVwANZx
# 7rDNFgN32tLmknEC3mpm54VqdworVXrTEbyobbcg1mkvMmPZPdj