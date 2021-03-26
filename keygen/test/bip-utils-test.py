from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, WifDecoder, \
    RippleConf, XrpAddr, Bip32, Bip44Changes

from keygen.crypto_coin import CryptoCoin
from keygen.crypto_coin_service import CoinService

# mnemonic = Bip39MnemonicGenerator.FromWordsNumber(12)

mnemonic = "copy curve retire hidden cover wrap muffin raw crop olympic kingdom right"
# Generate random mnemonic
# mnemonic = Bip39MnemonicGenerator.FromWordsNumber(12)
print("Mnemonic string: %s" % mnemonic)
# Generate seed from mnemonic
seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
# Generate BIP44 master keys
bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN)
# Print master key
print("Master key (bytes): %s" % bip_obj_mst.PrivateKey().Raw().ToHex())
print("Master key (extended): %s" % bip_obj_mst.PrivateKey().ToExtended())
print("Master key (HEX): %s" % bip_obj_mst.PrivateKey().Raw().ToHex())
print("Master key (WIF): %s" % bip_obj_mst.PrivateKey().ToWif())
print("Master key (Address): %s" % bip_obj_mst.PublicKey().ToAddress())
# Generate BIP44 account keys: m/44'/0'/0'
bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(0)
# Generate BIP44 chain keys: m/44'/0'/0'/0
bip_obj_chain = bip_obj_acc.Change(Bip44Changes.CHAIN_EXT)
# Generate the address pool (first 20 addresses): m/44'/0'/0'/0/i
for i in range(5):
    bip_obj_addr = bip_obj_chain.AddressIndex(i)
    print("%d. Address public key (extended): %s" % (i, bip_obj_addr.PublicKey().ToExtended()))
    print("%d. Address Priv key (hex): %s" % (i, bip_obj_addr.PrivateKey().Raw().ToHex()))
    print("%d. Address private key (extended): %s" % (i, bip_obj_addr.PrivateKey().ToExtended()))
    print("%d. Wif: %s" % (i, bip_obj_addr.PrivateKey().ToWif()))
    print("%d. Address: %s" % (i, bip_obj_addr.PublicKey().ToAddress()))