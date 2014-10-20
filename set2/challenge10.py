from Crypto.Cipher import AES
import array
import sys
sys.path.append('../set1')
import set1
import string
import binascii

def cbcModeDecrypt(key, iv, cipherText):
    cipherObj = AES.new(key, AES.MODE_ECB)
    
    if(len(cipherText) % 16):
        for _ in range(16 - len(cipherText) % 16):
            cipherText.append(0)

    plainText = []
    lastCipherBlock = iv
    for i in range(len(cipherText)/16):
        cipherBlock = cipherText[i * 16 : (i+1) * 16]
        plainTextBlock = array.array('B', cipherObj.decrypt(cipherBlock))
        plainTextBlock = set1.bufferXOR(plainTextBlock, lastCipherBlock)
        plainText += plainTextBlock
        lastCipherBlock = cipherBlock
    return plainText

fileBytes = array.array('B',binascii.a2b_base64(open(sys.argv[1] , "rb").read()))
# fileBytes = array.array('B', set1.strToHex(open(sys.argv[1] , "rb").read()))
iv = []
for _ in range(16):
    iv.append(0)

plainText = cbcModeDecrypt('YELLOW SUBMARINE', iv, fileBytes)

print repr(''.join(format(x, '01c') for x in plainText))
