from keygen.crypto_keygen_factory import CryptoKeygenFactory

factory = CryptoKeygenFactory()

currencies = ["BTC", "BCH", "LTC", "DASH", "CLUB", "ETH", "XMR", "WAVES", "POTE"]

# for currency in currencies:
#     print("Currency " + currency)
#     print(factory.get_crypto_keygen_service(currency).generate())
#     print("End..."+currency)

coins = factory.get_crypto_keygen_service('ETH').generateList(3)
print(coins)
