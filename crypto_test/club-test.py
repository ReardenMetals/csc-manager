
from pybitcoin import BitcoinPrivateKey

class ClubCoinPublicKey(BitcoinPrivateKey):
    _pubkeyhash_version_byte = 0x1c
    _wif_version_byte = 0x99

private_key = ClubCoinPublicKey(private_key='69AKnf5dW4McVLRNt6ZHUEaVkubgBbtq5mFjh7YAMwVCoaNY9F3')
# wif = private_key.to_wif()
address = private_key.public_key().address()

print(address)
# print(wif)

# CcDxzPk2vJ7gaS3f9ps7Ttw625BHU4e2oy
# 69AKnf5dW4McVLRNt6ZHUEaVkubgBbtq5mFjh7YAMwVCoaNY9F3