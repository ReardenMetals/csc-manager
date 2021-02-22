from abc import abstractmethod


class CoinService:

    @abstractmethod
    def get_address_and_id(self, private_key):
        coin = self.get_coin(private_key)
        if (coin):
            asset_id = self.generate_asset_id(coin)
            address = coin.address
            return address, asset_id
        return

    #Get address from private key
    @abstractmethod
    def get_address(self, private_key):
        coin = self.get_coin(private_key)
        if (coin):
            return coin.address
        return

    #Returns crypto_coin
    @abstractmethod
    def get_coin(self, private_key):
        return



    def generate_asset_id(self, coin):
        return coin.address[1:7]
