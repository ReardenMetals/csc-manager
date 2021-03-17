# Introduction to Cold Storage Coins Manager

This is Python desktop offline application for generating & validating Cold Storage Coins of different currencies: BTC, BCH, CLUB, DASH, LTC, ETH, BSV, DOGE, XRP, XMR, BNB, EOS, POTE, WAVES, USDT. Also added implementation of AWS Lambda keygen.

# CSC Manager Installation

This application is working with Python 3.8.6 (pip 20.2.1)

Python-3.8.6 download link: https://www.python.org/downloads/release/python-386/

## Linux Install

Install needed dependencies:

    pip pip install -r requirements.txt
    
Change application config ("config.json" in root folder) to your file pathes:
    
    {
      "base_file_name": "./output/keypair.txt",
      "asset_id_file_name": "./output/snip.txt",
      "private_file_name": "./output/key.txt",
      "public_file_name": "./output/labels.txt",
      "sequence_file_name": "./output/numbers.txt"
    }
    
Run CSC Manager desktop application:

    python csc-manager.py
    
Run CLI Keygen:

    python keygen.py
    
Run CLI Update:

    python update.py
    
## Windows install

Download & Install Visual studio build tool (or Visual Studio 19): https://visualstudio.microsoft.com/visual-cpp-build-tools/

Windows dependencies:
    
    vcredist_x64
    Microsoft Visual C++ 14.0

    vs_buildtools_xxxxx.exe  --layout c:\offlineBuildTool --lang en-us
    
Install needed dependencies:

    pip install -r requirements.txt
    
Change application config ("config.json" in root folder) to your file pathes:

    {
      "base_file_name": "C:\\Users\\laser\\Desktop\\keypair.txt",
      "asset_id_file_name": "C:\\Users\\laser\\Desktop\\snip.txt",
      "private_file_name": "C:\\Users\\laser\\Desktop\\key.txt",
      "public_file_name": "C:\\Users\\laser\\Desktop\\labels.txt",
      "sequence_file_name": "C:\\Users\\laser\\Desktop\\numbers.txt"
    }
    
Run CSC Manager desktop application:

    ./csc-manager.bat
    
Run CLI Keygen:

    ./keygen.bat
    
Run CLI Update:

    ./update.bat

# AWS Lambda keygen installation
    
Install needed dependencies:
    
    pip install --target ~/lambda-package bip_utils==1.7.0 bitsv==0.11.5 cashaddress==1.0.6 aioeos==1.0.2 \
        pywallet==0.1.0 monero==0.8 PyWaves==0.8.15 base58==2.0.0
        
Preparing package for AWS Lambda:

    cp -r ~/csc-manager/keygen ~/lambda-package/
    zip -r9 ~/lambda.zip .
    zip -g ~/lambda.zip ~/csc-manager/aws_lambda.py
    
Upload zip archive to AWS Lambda.

# For a developers:

## Add new Crypto currency support
    
* Create new class, which implements CoinService (keygen/crypto_coin_service.py)
* Register new class in CoinCheckerFactory (keygen/crypto_checker_factory.py)

        @staticmethod
        def get_coin_service(currency):
            ...
            if currency == "EOS":
                return EosCoinService() 
            ...
* Add your currency in CoinCheckerFactory.get_available_currencies
* Add currency icon in ./resources/img/coin-{YOURCOIN}.png
    
# Donations

If you'd like to donate something:

* BTC: 1LEG6G9Qos9GME4vwS1K9Kypy47Vv1bNds
* ETH: 0x2a1a059a580b044cbdfbba1a4f0fcfe79d724c18
* LTC: LUZXdc4moJ7wWu5fEqbsR9iYJDBtemEJRG
* BCH: qqhwmp8th2wazcm9pcvnt6nl05vh9w80gu0n4ar6r4

Thank you very much in advance for your support.

# License
