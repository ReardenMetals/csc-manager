from keygen.crypto_coin_factory import CoinFactory
import json
import asynctkinter as at


class KeygenController:
    def __init__(self, root, window):
        self.root = root
        self.window = window

    def generate_keys(self, count, coin, laser):
        self.start_async(self.generate_keys_async(count, coin, laser))

    async def generate_keys_async(self, count, coin, laser):
        await self.run_in_thread(lambda: generate_keys(count, coin, laser))
        print("self.root.show_success()")
        self.root.show_success()

    def start_async(self, task):
        at.start(task)

    def run_in_thread(self, func):
        return at.run_in_thread(func, after=self.window.after)


def generate_keys(count, coin, laser):
    with open('config.json') as json_file:
        config_json = json.load(json_file)
        base_file_name = config_json['base_file_name']
        asset_id_file_name = config_json['asset_id_file_name']
        private_file_name = config_json['private_file_name']
        public_file_name = config_json['public_file_name']
        sequence_file_name = config_json['sequence_file_name']

    max_iterator_count = int(count)

    try:
        factory = CoinFactory()
        crypto_keygen_service = factory.get_coin_service(coin)

        if max_iterator_count > 0:
            coin_list = crypto_keygen_service.generate_list(max_iterator_count)
            save_coins_list(crypto_keygen_service, coin_list, base_file_name)
            save_asset_ids(crypto_keygen_service, coin_list, asset_id_file_name)
            save_private_keys(crypto_keygen_service, coin_list, private_file_name)
            save_public_keys(crypto_keygen_service, coin_list, public_file_name)
            save_sequense_coin_id(laser, coin_list, sequence_file_name)
        else:
            print("Iterator count should be > 0")
    except Exception as e:
        print(e)


def save_coins_list(crypto_keygen_service, coin_list=[], filename='address.csv'):
    with open(filename, 'w') as file:
        file.write(crypto_keygen_service.get_csv_header())
        for crypto_keygen_service in coin_list:
            line = "{},{},{}\n".format(crypto_keygen_service.address, crypto_keygen_service.wif,
                                       crypto_keygen_service.seed)
            print("Address.csv {}/{}".format(coin_list.index(crypto_keygen_service), len(coin_list)))
            file.write(line)
        file.flush()
        file.close()
        print("Done!")


def save_asset_ids(crypto_keygen_service, coin_list=[], filename='assetid.txt'):
    with open(filename, 'w') as file:
        for coin in coin_list:
            asset = crypto_keygen_service.generate_asset_id(coin)
            line = "{}\n".format(asset)
            file.write(line)
            print("Asset IDs {}/{}".format(coin_list.index(coin), len(coin_list)))
        file.flush()
        file.close()
        print("Done!")


def save_private_keys(crypto_keygen_service, coin_list=[], filename='private.txt'):
    with open(filename, 'w') as file:
        for coin in coin_list:
            line = "{}\n".format(coin.wif)
            file.write(line)
            print("PrivateKeys {}/{}".format(coin_list.index(coin), len(coin_list)))
        file.flush()
        file.close()
        print("Done!")


def save_public_keys(crypto_keygen_service, coin_list=[], filename='public.txt'):
    with open(filename, 'w') as file:
        for coin in coin_list:
            line = "{},{}\n".format(coin.address, crypto_keygen_service.generate_asset_id(coin))
            file.write(line)
            print("PublicKeys {}/{}".format(coin_list.index(coin), len(coin_list)))
        file.flush()
        file.close()
        print("Done!")


def save_sequense_coin_id(lazer_type, coin_list=[], filename='sequence.txt'):
    with open(filename, 'w') as file:
        for coin_item in coin_list:
            line = "{}{}\n".format(lazer_type, coin_list.index(coin_item).__format__('04'))
            file.write(line)
            print("CoinId Laser Type {}, Number {}".format(lazer_type, coin_list.index(coin_item).__format__('04')))
        file.flush()
        file.close()
        print("Done!")
