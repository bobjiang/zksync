import csv
import sys
import binascii
import time
from web3 import Account
from Crypto.Hash import keccak
from ecdsa import SigningKey, SECP256k1

# pip3 install pycryptodome
# pip3 install ecdsa

def gen_eth_addr2():
    account = Account.create()

    priv_key = '0x' + str(binascii.hexlify(account.key), 'utf-8')

    print(priv_key)

    print(account.address)

def gen_eth_addr():
    keccak256 = keccak.new(digest_bits=256)

    priv = SigningKey.generate(curve=SECP256k1) # 生成私钥
    pub = priv.get_verifying_key() # 生成公钥

    keccak256.update(pub.to_string() ) # keccak256 哈希运算
    address = "0x" + keccak256.hexdigest()[24:]

    _priv_key = binascii.hexlify( priv.to_string())
    pub_key = binascii.hexlify( pub.to_string())

    priv_key = "0x" + _priv_key.decode()
    print("Public key:  " + pub_key.decode() )

    return priv_key, address

if __name__=="__main__":

    num = 30 # 默认生成30个地址
    if len(sys.argv) > 1:
        input1 = sys.argv[1]
        print(input1)
        num = int(input1)

    ts = str(int(time.time()))

    file = "addrs_" + ts + ".csv"
    with open(file, 'a+', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for i in range(num):
            priv_key, address = gen_eth_addr()

            print("Private key: " + priv_key)
            print("Address:     " + address)
            data_row = [priv_key, address]

            spamwriter.writerow(data_row)
