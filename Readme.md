Keygen Md

Install needed dependencies:

    pip install --target ./package pybitcoin pywaves cashaddress ecdsa pysha3
    pip install ph4-moneropy

Run the script:

    python2.7 script.py 10 output/ BTC  

Linux install:

    sudo -i
    sudo add-apt-repository universe
    sudo chmod -R a+rX,u+w /var/cache/app-info/xapian/default
    exit
    sudo apt-get update
    sudo apt install python-pip
    pip install --upgrade --user pip
    pip install pybitcoin==0.9.9
    pip install urllib3==1.21.1
    pip install chardet==3.0.2
    pip install pysha3==1.0.2
    pip install pywaves

Change log:

v7
 - add Monero support

v6
 - added WAVES support
 - added support for PotCoin
 - manually added "pw.setOffline()" to line 87 for WAVES offline generation

v5
 - received 02 Feb 2018
 - includes support for Ethereum
 - includes support for Monero
 - changes compression back to TRUE
 - removes 1st and 4th columns from output file (HEX, PASSPHRASE)


v4b
 - adds line "_wif_version_byte = 0x99" to fix clubcoin compatibility issue

script-v4a.py  (LIVE VERSION)
 - CURRENT WORKING SCRIPT

Dependencies version needed:

    base58==0.2.5
    bitcoin==1.1.42
    bitmerchant==0.1.8
    cachetools==2.1.0
    certifi==2018.4.16
    chardet==3.0.4
    commontools==0.1.0
    ecdsa==0.13
    idna==2.7
    keychain==0.14.2.0
    keylib==0.1.1
    pkg-resources==0.0.0
    pybitcoin==0.9.9
    pyblake2==1.1.2
    python-axolotl-curve25519==0.4.1.post2
    python-bitcoinrpc==0.1
    PyWaves==0.8.15
    requests==2.19.1
    sha3==0.2.1
    six==1.11.0
    urllib3==1.23
    utilitybelt==0.2.6
