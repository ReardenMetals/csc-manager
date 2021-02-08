
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
