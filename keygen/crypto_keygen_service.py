from abc import abstractmethod

class CryptoKeygenService:

    def generateList(self, count):
        return [self.generate() for x in range(0, count)]

    @abstractmethod
    def generate(self):
        return

    def generate_asset_id(self, coin):
        coin_address = coin.address
        return coin_address[1:7]

    def format(self, coin):
        return "{},{}\n".format(coin.wif, coin.address)

    def get_csv_header(self):
        return "WIF,Address\n"
