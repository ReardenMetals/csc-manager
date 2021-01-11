from sys import argv, exit
from pybitcoin import BitcoinPrivateKey, LitecoinPrivateKey
# import pywaves as pw
from cashaddress import convert

#for ethereum wallets
from ecdsa import SigningKey, SECP256k1
import sha3
import codecs
import json


# for monero wallet
from moneropy import account

class DashPublicKey(BitcoinPrivateKey):
    _pubkeyhash_version_byte = 0x4c


class ClubCoinPublicKey(BitcoinPrivateKey):
    _pubkeyhash_version_byte = 0x1c


class PotCoinPublicKey(BitcoinPrivateKey):
    _pubkeyhash_version_byte = 0x37


class CryptoCoin:
    address = ''
    wif = ''
    seed = ''

    def __init__(self, address, wif, seed=''):
        self.address = address
        self.wif = wif
        self.seed = seed

    def __repr__(self):
        return "address='{}', wif='{}', seed='{}'".format(self.address, self.wif, self.seed)


def GenerateBTC():
    private_key = BitcoinPrivateKey.from_passphrase()
    wif = private_key.to_wif()
    seed = private_key.passphrase()
    address = private_key.public_key().address()
    coin = CryptoCoin(address, wif, seed)
    # line = "{},{},{}\n".format(coin.wif, coin.address, coin.seed)
    return coin


def FormatBTC(coin):
    line = "{},{},{}\n".format(coin.wif, coin.address, coin.seed)
    return line


def GenerateBCH():
    private_key = BitcoinPrivateKey.from_passphrase()
    # seed = private_key.passphrase()
    # private_key._compressed = True
    wif = private_key.to_wif()
    address = convert.to_cash_address(private_key.public_key().address())
    coin = CryptoCoin(address.replace('bitcoincash:', ''), wif)
    return coin


def FormatBCH(coin):
    line = "{},{}\n".format(coin.wif, coin.address)
    return line


def GenerateLTC():
    private_key = LitecoinPrivateKey.from_passphrase()
    # seed = private_key.passphrase()
    wif = private_key.to_wif()
    address = private_key.public_key().address()
    coin = CryptoCoin(address, wif)
    return coin


def FormatLTC(coin):
    line = "{},{}\n".format(coin.wif, coin.address)
    return line


def GenerateDASH():
    private_key = DashPublicKey.from_passphrase()
    # private_key._compressed = True
    wif = private_key.to_wif()
    address = private_key.public_key().address()
    coin = CryptoCoin(address, wif)
    return coin


def FormatDASH(coin):
    line = "{},{}\n".format(coin.wif, coin.address)
    return line


def GenerateCLUB():
    private_key = ClubCoinPublicKey.from_passphrase()
    # private_key._compressed = True
    wif = private_key.to_wif()
    address = private_key.public_key().address()
    coin = CryptoCoin(address, wif)
    return coin


def FormatCLUB(coin):
    line = "{},{}\n".format(coin.wif, coin.address)
    return line


def GeneratePOTE():
    private_key = PotCoinPublicKey.from_passphrase()
    # private_key._compressed = True
    wif = private_key.to_wif()
    address = private_key.public_key().address()
    coin = CryptoCoin(address, wif)
    return coin


def FormatPOTE(coin):
    line = "{},{}\n".format(coin.wif, coin.address)
    return line


def GenerateETH():
    keccak = sha3.keccak_256()

    priv = SigningKey.generate(curve=SECP256k1)
    pub = priv.get_verifying_key().to_string()
    keccak.update(pub)
    address = keccak.hexdigest()[24:]
    priv_hex = codecs.encode(priv.to_string(), 'hex')
    coin = CryptoCoin("0x{}".format(address), priv_hex)
    # line = "{},0x{}\n".format(priv_hex, address)
    return coin


def FormatETH(coin):
    line = "{},{}\n".format(coin.wif, coin.address)
    return line


# TODO Add this coins
def GenerateXMR():
    seed, sk, vk, addr = account.gen_new_wallet()
    # line = "{},{},{},{}\n".format(addr,vk,sk,seed)
    coin = CryptoCoin(addr, sk, seed)
    return coin


def FormatXMR(coin):
    line = "{},{}\n".format(coin.wif, coin.address)
    return line
#
# def GenerateWaves():
#     addr = pw.Address()
#     line = "{},{},{},{}\n".format(addr.address, addr.publicKey, addr.privateKey, addr.seed)
#     return line

def toNumber(input):
    try:
        return int(input)
    except ValueError:
        print "Please input valid integer! {}".format(input)
        return None


def saveCoinsList(coin, coin_list=[], filename='address.csv'):
    options = {
        "BTC": FormatBTC,
        "BCH": FormatBCH,
        "LTC": FormatLTC,
        "DASH": FormatDASH,
        'CLUB': FormatCLUB,
        'ETH': FormatETH,
        'XMR': FormatXMR,
        # 'WAVES': FormatWaves, #TODO
        'POTE': FormatPOTE,
    }

    with open(filename, 'w') as file:
        if coin == "XMR":
            file.write("Address,Secret View Key,Secret Spend Key,Secret Mnemonic\n")
        elif coin == "WAVES":
            file.write("Address,Public Key,Private Key,Seed\n")
        elif coin == "BTC":
            file.write("WIF,Address,Seed\n")
        else:
            file.write("WIF,Address\n")
        for coin_item in coin_list:
            line = options[coin](coin_item)
            file.write(line)
            print "{}/{}".format(coin_list.index(coin_item), len(coin_list))
        file.flush()
        file.close()
        print "Done!"


def GenerateAssetIdFromDefault(coin_item):
    coin_address = coin_item.address
    return coin_address[1:7]

def GenerateAssetIdFromETH(coin_item):
    coin_address = coin_item.address
    return coin_address[2:8]


def GenerateAssetId(coin):
    options = {
        "BTC": GenerateAssetIdFromDefault,
        "ETH": GenerateAssetIdFromETH,
        "BCH": GenerateAssetIdFromDefault,
        "LTC": GenerateAssetIdFromDefault,
        "DASH": GenerateAssetIdFromDefault,
        'CLUB': GenerateAssetIdFromDefault,
        'XMR': GenerateAssetIdFromDefault,
        # 'WAVES': GenerateAssetIdFromDefault,
        'POTE': GenerateAssetIdFromDefault,
    }
    return options[coin]


def saveAssetIds(coin, coin_list=[], filename='assetid.txt'):
    with open(filename, 'w') as file:
        for coin_item in coin_list:
            line = "{}\n".format(GenerateAssetId(coin)(coin_item))
            file.write(line)
            print "Asset IDs {}/{}".format(coin_list.index(coin_item), len(coin_list))
        file.flush()
        file.close()
        print "Done!"


def savePrivateKeys(coin, coin_list=[], filename='private.txt'):
    with open(filename, 'w') as file:
        for coin_item in coin_list:
            line = "{}\n".format(coin_item.wif)
            file.write(line)
            print "PrivateKeys {}/{}".format(coin_list.index(coin_item), len(coin_list))
        file.flush()
        file.close()
        print "Done!"


def savePublicKeys(coin, coin_list=[], filename='public.txt'):
    with open(filename, 'w') as file:
        for coin_item in coin_list:
            line = "{},{}\n".format(coin_item.address, GenerateAssetId(coin)(coin_item))
            file.write(line)
            print "PublicKeys {}/{}".format(coin_list.index(coin_item), len(coin_list))
        file.flush()
        file.close()
        print "Done!"

def saveSequenseCoinId(lazer_type, coin_list=[], filename = 'sequence.txt'):
    with open(filename, 'w') as file:
        for coin_item in coin_list:
            line = "{}{}\n".format(lazer_type,coin_list.index(coin_item).__format__('04'))
            file.write(line)
            print "CoinId Lazer Type {}, Number {}".format(lazer_type,coin_list.index(coin_item).__format__('04'))
        file.flush()
        file.close()
        print "Done!"

def default_input( message, defaultVal ):
    if defaultVal:
        return raw_input( "%s [%s] : " % (message,defaultVal) ) or defaultVal
    else:
        return raw_input( "%s " % (message) )


def init():
    with open('config.json') as json_file:
        config_json = json.load(json_file)
        base_file_name = config_json['base_file_name']
        asset_id_file_name = config_json['asset_id_file_name']
        private_file_name = config_json['private_file_name']
        public_file_name = config_json['public_file_name']
        sequence_file_name = config_json['sequence_file_name']

    max_iterator_count = int(default_input("How many codes you want? ","10"))
    coin = default_input("What crypto you making (BTC, ETH,)? ","BTC").upper()
    lazer_type = default_input("What laser is this (A, B, C)? ", "A").upper()

    options = {
        "BTC": GenerateBTC,
        "BCH": GenerateBCH,
        "LTC": GenerateLTC,
        "DASH": GenerateDASH,
        'CLUB': GenerateCLUB,
        'ETH': GenerateETH,
        'XMR': GenerateXMR,
        # 'WAVES': GenerateWaves,
        'POTE': GeneratePOTE,
    }
    coins = list(options.keys())

    if coin in options:
        print "Number of address: {} \nOutput:  {}\nCoin: {} ".format(max_iterator_count, base_file_name, coin)
        coin_list = []
        if (max_iterator_count > 0):
            for i in range(max_iterator_count):
                coin_item = options[coin]()
                coin_list.append(coin_item)
            saveCoinsList(coin, coin_list, base_file_name)
            saveAssetIds(coin, coin_list, asset_id_file_name)
            savePrivateKeys(coin, coin_list, private_file_name)
            savePublicKeys(coin, coin_list, public_file_name)
            saveSequenseCoinId(lazer_type,coin_list, sequence_file_name)
        else:
            print "Iterator count should be > 0"
    else:
        print "{} is not supported yet, Supported coins are {}".format(coin, ', '.join(coins))
        print "Usage python script.py <number_of_wallets> <file_name.csv> <coin>"
        print "Usage python script.py 10 wallets.csv BTC"


if __name__ == "__main__":
    init()
