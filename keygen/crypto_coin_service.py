from abc import abstractmethod
import re


class CoinService:

    def generate_list(self, count):
        return [self.generate() for x in range(0, count)]

    @abstractmethod
    def generate(self):
        return

    def generate_asset_id(self, coin):
        return re.search('^\\w(\\w{6}).+$', coin.address).group(1)

    def get_address_and_id(self, private_key):
        coin = self.get_coin(private_key)
        if coin:
            asset_id = self.generate_asset_id(coin)
            address = coin.address
            return address, asset_id
        return

    #Get address from private key
    def get_address(self, private_key):
        coin = self.get_coin(private_key)
        if (coin):
            return coin.address
        return

    #Returns crypto_coin
    @abstractmethod
    def get_coin(self, private_key):
        return

    def format(self, coin):
        return "{},{},{}\n".format(coin.wif, coin.address, coin.seed)

    def get_csv_header(self):
        return "WIF,Address,Seed\n"
