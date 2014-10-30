from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Random import random
import array
import binascii
import sys
sys.path.append('../set2')
sys.path.append('../set1')
import set1
import set2

def decryptOracle(cipherText, key, iv):
    cipherObj = AES.new(key,AES.MODE_CBC, iv) 
    plainText = cipherObj.decrypt(cipherText)
    return set2.pkcs7Validation(plainText)[0]

plainTexts = ['MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=','MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=','MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==','MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==','MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl','MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==','MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==','MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=','MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=','MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93']
rndfile = Random.new() 
key = rndfile.read(16)
iv = array.array('B', rndfile.read(16))
plainText = array.array('B', binascii.a2b_base64(plainTexts[ord(rndfile.read(1)) % 10]))

cipherObj = AES.new(key,AES.MODE_CBC, iv) 
cipherText = cipherObj.encrypt(set2.pkcs7Pad(plainText,16))
prevCipher = iv
outputText = ''
for blockNum in range(0, len(cipherText) / 16):
    curCipher = array.array('B', cipherText[blockNum * 16:(blockNum+1) * 16])
    cPrime = array.array('B', [ord(rndfile.read(1)) for x in range(0,16)])
    imd = [0 for _ in range(0,16)]
    for i in reversed(range(0,16)):
        for j in range(0,256):
            cPrime[i] = j
            if decryptOracle(curCipher, key, cPrime):
                curImd = j ^ (16 - i)
                # print chr(curImd ^ iv[i])
                imd[i] = curImd

                # prepare cPrime with values that will create correct padding up to the point of interest
                for k in reversed(range(i,16)):
                    cPrime[k] = (17-i) ^ imd[k]
                break;
    outputText +=  ''.join([chr(x) for x in set1.bufferXOR(prevCipher, imd)])
    prevCipher = curCipher
print outputText