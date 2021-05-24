import json


# coin = tuple of (coin,asset_id)
def save_recovered_coins(coins):
    recovered_file_name, recovered_keys_file_name = load_file_config()

    print("Saving recovered public keys & asset IDs to file...\n")
    with open(recovered_file_name, 'w') as recovered_file:
        save_public_keys(coins, recovered_file)
        recovered_file.flush()
        recovered_file.close()
        print("Recovered public keys & asset IDs saved to file!\n")

    print("Saving recovered private keys to file...\n")
    with open(recovered_keys_file_name, 'w') as recovered_keys_file:
        save_private_keys(coins, recovered_keys_file)
        recovered_keys_file.flush()
        recovered_keys_file.close()
        print("Recovered private keys saved to file!\n")


def load_file_config():
    with open('config.json') as json_file:
        config_json = json.load(json_file)
        recovered_file_name = config_json['recovered_file_name']
        recovered_keys_file_name = config_json['recovered_keys_file_name']
        return recovered_file_name, recovered_keys_file_name


# coin = tuple of (coin,asset_id)
def save_public_keys(coins, file):
    for coin in coins:
        line = "{},{}".format(coin[0].address, coin[1])
        file.write("{}\n".format(line))
        print(line)
        print("Recovered public keys {}/{}\n".format(coins.index(coin) + 1, len(coins)))


# coin = tuple of (coin,asset_id)
def save_private_keys(coins, file):
    for coin in coins:
        line = "{}".format(coin[0].wif)
        file.write("{}\n".format(line))
        print(line)
        print("Recovered private keys {}/{}\n".format(coins.index(coin) + 1, len(coins)))
