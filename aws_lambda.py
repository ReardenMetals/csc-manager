import json
from keygen.crypto_coin_factory import CoinFactory


def lambda_handler(event, context):
    requestBody = json.loads(event["body"])
    blockchain = requestBody["blockchain"]
    quantity = requestBody["quantity"]

    coin = blockchain.upper()
    factory = CoinFactory()
    crypto_keygen_service = factory.get_coin_service(coin)

    coins = crypto_keygen_service.generate_list(quantity)

    res = [{"wif": coin.wif, "address": coin.address, "snip": crypto_keygen_service.generate_asset_id(coin)} for coin in
           coins]

    body = json.dumps({
        'data': res,
        'metadata': {
            'blockchain': blockchain,
            'quantity': quantity
        }
    })

    return {
        'statusCode': 200,
        'body': body
    }

# event = {"body": "{\"blockchain\":\"BTC\", \"quantity\": 10}"}
# res = lambda_handler(event, None)
# print(res)
