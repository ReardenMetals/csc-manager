from pybitcoin import BitcoinPrivateKey
from cashaddress import convert

private_key = BitcoinPrivateKey(private_key='5Ke8bzyw8g1H172bCU4jCXQpvVRD3eSFCmsxR81RYJZpTM7xL9X')
address = convert.to_cash_address(private_key.public_key().address()).replace('bitcoincash:', '')
print(address)

# 5Ke8bzyw8g1H172bCU4jCXQpvVRD3eSFCmsxR81RYJZpTM7xL9X
# qznd7gyv3l8ay02skgnperj7rnas4qawgcc90mee7w