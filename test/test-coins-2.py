from keygen.crypto_coin_factory import CoinFactory


def test_coin(currency, private_key, address):
    service = CoinFactory.get_coin_service(currency)
    gen_address = service.get_address(private_key)
    assert gen_address == address


def test(currency, private_key, address, title):
    print("Checking {}, {}...".format(title, private_key))
    test_coin(currency, private_key, address)
    print(currency + " Success")

# 1. ETH
test('ETH', 'bb0d723177603b46d3ba5b4aad018b83bd3cf7afc128274948655f2036549858',
     '0xd3af1fdfae6a9871c06b90e23193b3785bd2390a', 'ETH')

test('ETH', 'c2afb46249f70cd011cf594e29af09cebd3fa2570774d80d54447f7440031921',
     '0x6f2a619733dcc8ee9c53766bd906b5985ab274e2', 'ETH (OLD)')

# 2. BTC
test('BTC', 'L4MdVAQgrbmZham4zFzam2zh3U68gqGdE7pQ1JKvrfQzrJPBoEdc',
     '1QHYPXFHJ5zCaQS5HcwNFzPNpDJXnCoXzo', 'BTC')

test('BTC', '5JQcan7Ry4mwGEZThCRW2oZJa9QbAMyahg9pR3LJwDhws85NW2r',
     '1GXXecdih6PSjuSZ14oMQGPHdtLQFYyGTD', 'BTC(OLD)')

# 3. BCH
test('BCH', 'KwLq3AMz5rdpALCFyHqfLe8TVHQCh1pHBhoS9yGuneYF8PmpgXEQ',
     'qzyvlkdgscpcpaspdknzscs9dl7phkgpjgkah386nq', 'BCH')

test('BCH', '5KMm8HtE8Q6x1P5AuTw7zfDTWWV1wcTp73ntYCWwj6dvBNenvth',
     'qre49ddrwdgqyjtpv2dahgn7gamwaxjeq54nvjgpwd', 'BCH(OLD)')

# 4. LTC
test('LTC', 'TAwDFcbahqX9RVVz9aT37jscCNitYp3oZM4SkxBhAmNjSZ9RhDrc',
     'LbW51HQNTKmkXKv5jKyU2pfvWSVUeQxA4X', 'LTC')

test('LTC', '6vzYB89RnDcYJBrfY6ansERJ2K5f44jkn2UuqXs3wd229W1U4tB',
     'LgU4TSGEkd8PzRiC343pqAPM9M1X9kcFhD', 'LTC (OLD)')

# 5. DASH
test('DASH', 'XH7URm12Kksn2dkECSHoExCA5Bnvj3XwbJTdhVVBFnugb4hKHBN2',
     'Xjtu6nYbd7ki9NBVB1LXFvDWCPTsAvyPmb', 'DASH')

test('DASH', '7rK9xTSzzgAt1N3XWAm8Erc7CJhxc6yyciteLZFU9pVaXozGbNZ',
     'Xy79yMGZkeDkqq5GcLhK32zGnomQUXZ4uF', 'DASH(OLD)')

# 6. CLUB
test('CLUB', 'Peqh7Nd6w5ws3cMZR7Eg6zi7JnwC3feNyVpUBjN8RrCY2RsCQwNQ',
     'CKFBatXTmCsvf9cGGmGe9VEZLK582nqUpg', 'CLUB')

test('CLUB', '68zhBVWaPD2uwqp2rdyW2QcfY1QkHZQyPMJv4uitPmQbiBeGnRa',
     'Cea1j3EnVM2VZgjrCxbbEczzRDTo6Rrtm6', 'CLUB(OLD)')

# 7. BSV
test('BSV', 'L4NpF6jfGEtSJ5YCsTQHgkC9zEzAqm913Qxr9Yc2QqsYyt2Gkj7Z',
     '1PpyrNBE5hRmDK9MWyFZr2sPfT4iRUUYF', 'BSV')

# 8. DOGE
test('DOGE', 'QXArcQ4YdLcxfBkEMucxq1BCfJWUodS7VvNzsEgSSdAt8ioRriey',
     'DLH5B4bx4zJ7ZQvphYi5nVJq6fVTPZoT9g', 'DOGE')

# 9. XRP
test('XRP', 'xprv9s21ZrQH143K2fNZPozW3tM4yVkkjmwbTzZ65KEfARmiprnNiqm3iQQYU3tPBnSLjJPUdfZR8E7QSz6gmNmZUs8A3KFnZspCD6R2cu6MS1B',
     'r4Cb1wsjEiP8j54LMhE48JUSZywTWEGh1J', 'XRP')

# 10. BNB
test('BNB', 'xprv9s21ZrQH143K2PyH8Tsd3wwiJ5qkjRMzHAf9qdRxVeGhi6yS7pwkcHoZajTX7qk38zSSwP2eUvtAd1quhzYccFqneFMXEAsTSWTHJy958mP',
     'bnb1f9akltnuwxgs9s9404k5u2frk95wpmy37cvcqq', 'BNB')

# 11. XMR
test('XMR', '876604d806600496bc05b8b594c9eee5bdfdc97bc8e599096d7bf73be982b20f',
     '4AYVcwKNaXAJMNeGYVSQ4JD1ovp3i5K7dSbJ2PpYk6KDDxoHc8bwUgqBoA7ZAw8UfLRdhJYmBitjMeBoNscH21XjJyRvBqm', 'XMR')

# 12. EOS
test('EOS', '5JbaS3Aec97j5G3NHxspfc6xNMT3qEEGpZNbB3GQH3SnNpsGPb5',
     'EOS8MWYCQXbs61djAneDLpQHjXe14WMJX9q2eGACoHx9BFLwTz7N5', 'EOS')

# 13. POTE
test('POTE', 'U9ZdLDCXhaY5NDkqKuxJwfZUXixKQExgor8MtqGwrzfjx4UoTtQ3',
     'PRYU7GUm9BYVya4WgH8iXUCBdwk3dKmKEJ', 'POTE')

test('POTE', '79mUxQE976DM88ZtUgpFcGMUQEyF3wrSnnSprQjtAk4nQRyQQLf',
     'PMT9ZBoJ8D7gq9AhVmRij2X6VtKMXZCCcW', 'POTE(OLD)')

# 14. WAVES
test('WAVES', 'ZUpu5qYspCb6MdafPV2MD3pCr5vDsTCuFLnuSVgvVqB',
     '3PHPEeAGmYhvE1dHYmBzor8WDHaJiWZZxtc', 'WAVES')

# 15. USDT
test('USDT', 'L4vzeLtADeQMYH8zV1UmqxXHHFJimgvwuGc4Eft6WbznTDLmFCJN',
     '32s399kQ4mQTQ815PhcUkwuUsPqhL5sbyg', 'USDT')

# TODO Add cardano tests

print("Final success")
