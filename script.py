from sys import argv, exit
from pybitcoin import BitcoinPrivateKey, LitecoinPrivateKey
# import pywaves as pw
from cashaddress import convert

# for ethereum wallets
from ecdsa import SigningKey, SECP256k1
import sha3
import codecs


# for monero wallet
#from moneropy import account

class DashPublicKey(BitcoinPrivateKey):
    _pubkeyhash_version_byte = 0x4c


class ClubCoinPublicKey(BitcoinPrivateKey):
    _pubkeyhash_version_byte = 0x1c

class PotCoinPublicKey(BitcoinPrivateKey):
    _pubkeyhash_version_byte = 0x37



def GenerateBTC():
    private_key = BitcoinPrivateKey.from_passphrase()
    wif = private_key.to_wif()
    seed = private_key.passphrase()
    address = private_key.public_key().address()
    line = "{},{},{}\n".format(wif, address, seed)
    return line

def GenerateBCH():
    private_key = BitcoinPrivateKey.from_passphrase()
    # seed = private_key.passphrase()
    # private_key._compressed = True
    wif = private_key.to_wif()
    address = convert.to_cash_address(private_key.public_key().address())
    line = "{},{}\n".format(wif, address.replace('bitcoincash:', ''))
    return line

def GenerateLTC():
    private_key = LitecoinPrivateKey.from_passphrase()
    # seed = private_key.passphrase()
    wif = private_key.to_wif()
    address = private_key.public_key().address()
    line = "{},{}\n".format(wif, address)
    return line


def GenerateDASH():
    private_key = DashPublicKey.from_passphrase()
    # private_key._compressed = True
    wif = private_key.to_wif()
    address = private_key.public_key().address()
    line = "{},{}\n".format(wif, address)
    return line


def GenerateCLUB():
    private_key = ClubCoinPublicKey.from_passphrase()
    # private_key._compressed = True
    wif = private_key.to_wif()
    address = private_key.public_key().address()
    line = "{},{}\n".format(wif, address)
    return line

def GeneratePOTE():
    private_key = PotCoinPublicKey.from_passphrase()
    # private_key._compressed = True
    wif = private_key.to_wif()
    address = private_key.public_key().address()
    line = "{},{}\n".format(wif, address)
    return line

def GenerateETH():
    keccak = sha3.keccak_256()

    priv = SigningKey.generate(curve=SECP256k1)
    pub = priv.get_verifying_key().to_string()
    keccak.update(pub)
    address = keccak.hexdigest()[24:]
    priv_hex = codecs.encode(priv.to_string(),'hex')
    line = "{},0x{}\n".format(priv_hex, address)
    return line

def GenerateXMR():
    seed, sk, vk, addr = account.gen_new_wallet()
    line = "{},{},{},{}\n".format(addr,vk,sk,seed)
    return line

def GenerateWaves():
    addr = pw.Address()
    line = "{},{},{},{}\n".format(addr.address, addr.publicKey, addr.privateKey, addr.seed)
    return line

def toNumber(input):
    try:
        return int(input)
    except ValueError:
        print "Please input valid integer! {}".format(input)
        return None


def init():
    max_iterator_count = 10
    out_file_name = 'address.csv'
    coin = 'BTC'

    if len(argv) >= 4:
        max_iterator_count = toNumber(argv[1])
        out_file_name = argv[2]
        coin = argv[3]
    else:
        print "Script will run with default configuration"

    coin = coin.upper()

    if max_iterator_count is None:
        exit(0)

    options = {
        "BTC": GenerateBTC,
        "BCH": GenerateBCH,
        "LTC": GenerateLTC,
        "DASH": GenerateDASH,
        'CLUB': GenerateCLUB,
        'ETH': GenerateETH,
        'XMR':GenerateXMR,
        'WAVES': GenerateWaves,
        'POTE': GeneratePOTE,
    }
    coins = list(options.keys())
    filename = "{}".format(out_file_name)
    if coin in options:
        print "Number of address: {} \nOutput:  {}\nCoin: {} ".format(max_iterator_count, filename, coin)
        if (max_iterator_count > 0):
            with open(filename, 'w') as file:
                if coin == "XMR":
                    file.write("Address,Secret View Key,Secret Spend Key,Secret Mnemonic\n")
                elif coin == "WAVES":
                    file.write("Address,Public Key,Private Key,Seed\n")
                elif coin == "BTC":
                    file.write("WIF,Address,Seed\n")
                else:
                    file.write("WIF,Address\n")
                for i in range(max_iterator_count):
                    line = options[coin]()
                    file.write(line)
                    print "{}/{}".format(i + 1, max_iterator_count)
                file.flush()
                file.close()
                print "Done!"
        else:
            print "Iterator count should be > 0"
    else:
        print "{} is not supported yet, Supported coins are {}".format(coin, ', '.join(coins))
        print "Usage python script.py <number_of_wallets> <file_name.csv> <coin>"
        print "Usage python script.py 10 wallets.csv BTC"


if __name__ == "__main__":
    init()
