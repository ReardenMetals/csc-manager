Keygen Md

Install needed dependencies:

    pip install --target ./package pybitcoin pywaves cashaddress ecdsa pysha3
    pip install ph4-moneropy

Run the script:

    python3.8 script.py

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
    pip install bip_utils
    pip install aioeos
    pip install monero
    pip install cashaddress
    pip install Pillow
    pip install opencv-python
    pip install pyzbar
    pip install imutils
    pip install asynctkinter
    pip install pygame

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

    base58==0.2.5 +
    bitcoin==1.1.42 +
    bitmerchant==0.1.8 +
    cachetools==2.1.0 down
    certifi==2018.4.16 down
    chardet==3.0.4 down
    commontools==0.1.0 +
    ecdsa==0.13 down
    idna==2.7 down
    keychain==0.14.2.0 +
    keylib==0.1.1 +
    pkg-resources==0.0.0 ?
    pybitcoin==0.9.9 +
    pyblake2==1.1.2 +
    python-axolotl-curve25519==0.4.1.post2 +
    python-bitcoinrpc==0.1+
    PyWaves==0.8.15 +
    requests==2.19.1 down
    sha3==0.2.1 ?
    six==1.11.0 down
    urllib3==1.23 down
    utilitybelt==0.2.6 +

For a Rob:

    install pywaves:
    - 1) Install python-2.7.18.msi(when installing add python.exe to Path) and VCForPython27.msi
    - 2) Copy the file stdint.h and paste it in C:\Users\laser\AppData\Local\Programs\Common\Microsoft\Visual C++ for Python\9.0\VC\include\
    - 3) Copy folder MinGW in C:\
    - 4) Add C:\MinGW\bin to environment varaibles
    - 5) Copy the file distutils.cfg and paste it in C:\python27\Lib\distutils
    - 6) Open a new instance of Command prompt: open folder python-axolotl-curve25519-master and run command python setup.py install
    - 7) Then open folder python-axolotl-master and run command python setup.py install

For a developer:
    
    install project:
    - 1) Install python-2.7.18.msi(when installing add python.exe to Path) and VCForPython27.msi
    - 2) Copy the file stdint.h and paste it in C:\Users\Administrator\AppData\Local\Programs\Common\Microsoft\Visual C++ for Python\9.0\VC\include\
    - 3) Install mingw-get-setup.exe
    - 4) Add C:\MinGW\bin to environment varaibles
    - 5) Create a new file named distutils.cfg, put this new file in the Lib/distutils folder of your python installation e.g C:\python27\Lib\distutils
        inside this file add these 2 lines and save:
            [build]
            compiler=mingw32
    - 6) Open a new instance of Command prompt and run this commands: mingw-get.exe install gcc
    - 7) run this commands: mingw-get.exe install zlib
    - 8) Open project in PyCharm
    - 9) in terminal run commands:open folder python-axolotl-curve25519-master and run command python setup.py install,
        then open folder python-axolotl-master and run command python setup.py install
    - 11) in terminal run commands: pip install --target ./package pybitcoin PyWaves==0.8.15 cashaddress ecdsa pysha3
    pip install ph4-moneropy