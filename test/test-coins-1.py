from keygen.crypto_coin_factory import CoinFactory


def test_coin(currency, private_key, address):
    service = CoinFactory.get_coin_service(currency)
    gen_address = service.get_address(private_key)
    assert gen_address == address


print("Checking BTC...")
test_coin("BTC", "5Ke8bzyw8g1H172bCU4jCXQpvVRD3eSFCmsxR81RYJZpTM7xL9X", "1GDLTzQDLJJLnihqVgcjwuTaSCwx8W4P2B")
print("Checking BCH...")
test_coin("BCH", "5Ke8bzyw8g1H172bCU4jCXQpvVRD3eSFCmsxR81RYJZpTM7xL9X", "qznd7gyv3l8ay02skgnperj7rnas4qawgcc90mee7w")
print("Checking LTC...")
test_coin("LTC", "6vm5LgDCL9kfZGoc7MscpSd9xKWyf6Jj1YQLCDeNTNds8mfzrbV", "LgJnMTxsR4tHqxT8Qd2cAeb2sX9PBEscyV")
print("Checking DASH...")
test_coin("DASH", "7rDNFgN32tLmknEC3mpm54VqdworVXrTEbyobbcg1mkvMmPZPdj", "XdRsX38wgENu6FrGx3wx6qnSTz7XVwANZx")
print("Checking CLUB...")
test_coin("CLUB", "69AKnf5dW4McVLRNt6ZHUEaVkubgBbtq5mFjh7YAMwVCoaNY9F3", "CcDxzPk2vJ7gaS3f9ps7Ttw625BHU4e2oy")
print("Checking ETH...")
test_coin("ETH", "813c58c6edc5f2689d54ca06efddbfb56feae888abfe30ce8e293224919ec818",
          "0x96fe96e97a107fff1f4c619ad1d5c0d568219f53")
print("Checking XMR...")
test_coin("XMR", "e22b4f6e0d81cd7b71f5d2bcf4191c8ed893c0adac59c9f2bf22c27cece1f90d",
          "476vPMXFMjJKMrzTtBDCtfNYxVbX1HnqxTaYmoJ8sz9oZLFAbKastHXMVX5BckcdK9fawU4NgooPsYjWngfKFrq4FLMRNiU")
print("Checking WAVES...")
test_coin("WAVES", "7UexcdyEMBtH2Yqzq1WeKXFEdxoVqDK4b6Wo9D32pPxN", "3PPQVUhBtU3xL2779cJ1XPL5Rw4bWLtouuc")
print("Checking POTE...")
test_coin("POTE", "79pHKdz8jC6m9WkBRpira7yMCdpDLZKmKxStsAcMi1XDrja45kQ", "PDyWMDMbqBeyKYAtUon5UnB3MH5qmjLaFc")
print("Checking USDT...")
test_coin("USDT", "Ky1hSHk9RZUBmJU8Nj614Ra81y3xQpmqVohv1NCTQQhD8WzRyTCh", "3Qb5HTPwtCaCT4Zcct3X1tsWeYiHPt3d2J")
print("Checking BNB...")
test_coin("BNB",
          "aa541689331812de852348b0fae3a896bf82ddd709dc75896df345e16c409c8b",
          "bnb1upfqv7y0hdzvlrznwt83jklsl49lewcclhg9zu")
print("Checking EOS...")
test_coin("EOS", "5JyZpiLFnCy7JGn4TEKEFSU6pRwne3vgciJbUq5pT2wzM4bvrBB",
          "EOS6ZsC7LhKtAew7srZ6wUDk2HgzRtDscZVHTAbZiMyDCwdUbXKjq")
print("Checking DOGE...")
test_coin("DOGE", "QTtBXsAXSG8miomDVfmvYZVr4AHH9kpkrthAjviZzgxbzkc87eb6", "DST5AnAAqdjM1HQX9vLmHdwKjUpWYQQnaX")

print("Final success")
