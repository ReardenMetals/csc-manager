
1. Install python-2.7.amd64.msi (https://www.python.org/download/releases/2.7/)
2. Edit config.json (pathes to files)

{
  "base_file_name": "C:\\Users\\laser\\Desktop\\address.csv",
  "asset_id_file_name": "C:\\Users\\laser\\Desktop\\asset_id.txt",
  "private_file_name": "C:\\Users\\laser\\Desktop\\private.txt",
  "public_file_name": "C:\\Users\\laser\\Desktop\\public.txt",
  "sequence_file_name": "C:\\Users\\laser\\Desktop\\sequence.txt"
}

3. TO GENERATE NEW KEY FILES DOUBLE-CLICK ON keygen.bat

4. TO AUTOMATICALLY delete all the records that were done okay DOUBLE CLICK update.bat

UPDATE FOR PYWAVES

    install pywaves:
    - 1) Install python-2.7.18.msi(when installing add python.exe to Path) and VCForPython27.msi
    - 2) Copy the file stdint.h and paste it in C:\Users\laser\AppData\Local\Programs\Common\Microsoft\Visual C++ for Python\9.0\VC\include\
    - 3) Copy folder MinGW in C:\
    - 4) Add C:\MinGW\bin to environment varaibles
    - 5) Copy the file distutils.cfg and paste it in C:\python27\Lib\distutils
    - 6) Open a new instance of Command prompt: open folder python-axolotl-curve25519-master and run command python setup.py install
    - 7) Then open folder python-axolotl-master and run command python setup.py install

UPDATE FOR BNB, USDT
    install:
    - 1) Python-3.6.8 (https://www.python.org/downloads/release/python-368/)
UPDATE FOR EOS
    install:
    - 1) Python-3.8.6 (https://www.python.org/downloads/release/python-386/)