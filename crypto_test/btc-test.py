
from pybitcoin import BitcoinPrivateKey


private_key = BitcoinPrivateKey(private_key='5Ke8bzyw8g1H172bCU4jCXQpvVRD3eSFCmsxR81RYJZpTM7xL9X')
address = private_key.public_key().address()
print(address)

# 5Ke8bzyw8g1H172bCU4jCXQpvVRD3eSFCmsxR81RYJZpTM7xL9X
# 1GDLTzQDLJJLnihqVgcjwuTaSCwx8W4P2B