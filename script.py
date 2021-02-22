from keygen.crypto_coin_factory import CoinFactory
import json


def saveCoinsList(crypto_keygen_service, coin_list=[], filename='address.csv'):
    with open(filename, 'w') as file:
        file.write(crypto_keygen_service.get_csv_header())
        for crypto_keygen_service in coin_list:
            line = "{},{},{}\n".format(crypto_keygen_service.address, crypto_keygen_service.wif, crypto_keygen_service.seed)
            print ("Address.csv {}/{}".format(coin_list.index(crypto_keygen_service), len(coin_list)))
            file.write(line)
        file.flush()
        file.close()
        print ("Done!")


def saveAssetIds(crypto_keygen_service, coin_list=[], filename='assetid.txt'):
    with open(filename, 'w') as file:
        for coin in coin_list:
            aset = crypto_keygen_service.generate_asset_id(coin)
            line = "{}\n".format(aset)
            file.write(line)
            print ("Asset IDs {}/{}".format(coin_list.index(coin), len(coin_list)))
        file.flush()
        file.close()
        print ("Done!")


def savePrivateKeys(crypto_keygen_service, coin_list=[], filename='private.txt'):
    with open(filename, 'w') as file:
        for coin in coin_list:
            line = "{}\n".format(coin.wif)
            file.write(line)
            print ("PrivateKeys {}/{}".format(coin_list.index(coin), len(coin_list)))
        file.flush()
        file.close()
        print ("Done!")


def savePublicKeys(crypto_keygen_service, coin_list=[], filename='public.txt'):
    with open(filename, 'w') as file:
        for coin in coin_list:
            line = "{},{}\n".format(coin.address, crypto_keygen_service.generate_asset_id(coin))
            file.write(line)
            print ("PublicKeys {}/{}".format(coin_list.index(coin), len(coin_list)))
        file.flush()
        file.close()
        print ("Done!")


def saveSequenseCoinId(lazer_type, coin_list=[], filename='sequence.txt'):
    with open(filename, 'w') as file:
        for coin_item in coin_list:
            line = "{}{}\n".format(lazer_type, coin_list.index(coin_item).__format__('04'))
            file.write(line)
            print ("CoinId Lazer Type {}, Number {}".format(lazer_type, coin_list.index(coin_item).__format__('04')))
        file.flush()
        file.close()
        print ("Done!")


def default_input(message, defaultVal):
    if defaultVal:
        return input("%s [%s] : " % (message, defaultVal)) or defaultVal
    else:
        return input("%s " % (message))


def init():
    with open('config.json') as json_file:
        config_json = json.load(json_file)
        base_file_name = config_json['base_file_name']
        asset_id_file_name = config_json['asset_id_file_name']
        private_file_name = config_json['private_file_name']
        public_file_name = config_json['public_file_name']
        sequence_file_name = config_json['sequence_file_name']

    max_iterator_count = int(default_input("How many codes you want? ", "10"))
    coin = default_input("What crypto you making (BTC, ETH, ...)? ", "BTC").upper()
    lazer_type = default_input("What laser is this (A, B, C)? ", "A").upper()

    try:
        factory = CoinFactory()
        crypto_keygen_service = factory.get_coin_service(coin)

        if max_iterator_count > 0:
            coin_list = crypto_keygen_service.generate_list(max_iterator_count)
            saveCoinsList(crypto_keygen_service, coin_list, base_file_name)
            saveAssetIds(crypto_keygen_service, coin_list, asset_id_file_name)
            savePrivateKeys(crypto_keygen_service, coin_list, private_file_name)
            savePublicKeys(crypto_keygen_service, coin_list, public_file_name)
            saveSequenseCoinId(lazer_type, coin_list, sequence_file_name)
        else:
            print("Iterator count should be > 0")
    except Exception as e:
        print(e)
        # print "{} is not supported yet".format(coin)
        # print "Usage python script.py <number_of_wallets> <file_name.csv> <coin>"
        # print "Usage python script.py 10 wallets.csv BTC"


if __name__ == "__main__":
    init()
