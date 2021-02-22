from aioeos.keys import EosKey
from sys import argv


def toNumber(input):
    try:
        return int(input)
    except ValueError:
        print("Please input valid integer! {}".format(input))
        return None


max_iterator_count = 1
if len(argv) >= 2:
    max_iterator_count = toNumber(argv[1])


eos = EosKey()
address = eos.to_public()
wif = eos.to_wif()

print(address)
print(wif)
