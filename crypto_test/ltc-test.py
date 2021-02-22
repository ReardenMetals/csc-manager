
from pybitcoin import BitcoinPrivateKey
from cashaddress import convert
from pybitcoin import LitecoinPrivateKey


private_key = LitecoinPrivateKey(private_key='6vm5LgDCL9kfZGoc7MscpSd9xKWyf6Jj1YQLCDeNTNds8mfzrbV')
# wif = private_key.to_wif()
address = private_key.public_key().address()

# print(wif)
print(address)

# 6vm5LgDCL9kfZGoc7MscpSd9xKWyf6Jj1YQLCDeNTNds8mfzrbV
# LgJnMTxsR4tHqxT8Qd2cAeb2sX9PBEscyV