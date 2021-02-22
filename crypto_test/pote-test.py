from pybitcoin import BitcoinPrivateKey

class PotCoinPublicKey(BitcoinPrivateKey):
    _pubkeyhash_version_byte = 0x37

private_key = PotCoinPublicKey(private_key='79pHKdz8jC6m9WkBRpira7yMCdpDLZKmKxStsAcMi1XDrja45kQ')
wif = private_key.to_wif()
address = private_key.public_key().address()

print(address)
# print(wif)

# PDyWMDMbqBeyKYAtUon5UnB3MH5qmjLaFc
# 79pHKdz8jC6m9WkBRpira7yMCdpDLZKmKxStsAcMi1XDrja45kQ