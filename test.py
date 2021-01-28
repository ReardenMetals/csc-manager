from crypto_keygen_factory import CryptoKeygenFactory

factory = CryptoKeygenFactory()
service = factory.get_crypto_keygen_service("BTC")
crypto_coin = service.generate()
print(crypto_coin)
