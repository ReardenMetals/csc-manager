
from pywallet import wallet
from pywallet.network import DogecoinMainNet
from pywallet.utils.keys import PrivateKey

# w = wallet.create_wallet(network="doge", children=1)
# wif = w.get('wif')
# address = w.get('address')
#
# print(address)
# print(wif)

key = PrivateKey.from_wif("QRJCy2Xqi26TspR3gvwF2v5vBx31ZTtvDbZtpMv9PFQXdVwCjAjU", network=DogecoinMainNet)
address = key.get_public_key().to_address()
print(address)

# DRiR4oUA5c6euzPWzA6FeoFjeNEB58JATM
# QRJCy2Xqi26TspR3gvwF2v5vBx31ZTtvDbZtpMv9PFQXdVwCjAjU