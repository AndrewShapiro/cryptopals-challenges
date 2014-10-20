from Crypto.Cipher import AES
import array
import sys
sys.path.append('../set1')
import set1
import string
import binascii

def cbcModeEncrypt(key, iv, plainText):
    cipherObj = AES.new(key, AES.MODE_ECB)
    
    # if(len(plainText) % 16):
    #     for _ in range(16 - len(plainText) % 16):
    #         plainText.append(0)

    cipherText = []
    lastCipherBlock = iv
    for i in range(len(plainText)/16):
        currentBlock = plainText[i * 16 : (i+1) * 16]
        currentBlock = set1.bufferXOR(array.array('B', currentBlock), lastCipherBlock)
        print str(currentBlock)
        currentBlock = array.array('B', cipherObj.encrypt(currentBlock))
        cipherText += currentBlock
        lastCipherBlock = currentBlock
    return cipherText

fileBytes = open(sys.argv[1] , "rb").read()
# fileBytes = array.array('B', set1.strToHex(open(sys.argv[1] , "rb").read()))
iv = []
for _ in range(16):
    iv.append(0)

cipherText = cbcModeEncrypt('YELLOW SUBMARINE', iv, fileBytes)

print cipherText
