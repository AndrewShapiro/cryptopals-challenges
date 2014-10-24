from Crypto.Cipher import AES
import array
import binascii
import sys
sys.path.append('../set1')
import set1
from Crypto import Random
from Crypto.Random import random
import string

unknownStr = binascii.a2b_base64('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')
plainText = array.array('B', open('headLikeAHole.txt' , "rb").read()) + array.array('B', unknownStr)

rndfile = Random.new()
key = rndfile.read(16)
cipherObj = AES.new(key, AES.MODE_ECB)

chosenPlain = ''
for i in range(0,128):
    chosenPlain += 'A'

cipherText = cipherObj.encrypt(chosenPlain)

for i in range(1,65):
    if(cipherText[:i] == cipherText[i:2*i]):
        print i
        blockSize = i
        break;

plainText = plainText[(len(plainText) % blockSize):]
cipherText = cipherObj.encrypt(plainText)
count = set1.twoByteMatch(cipherText)
print count
if count > 100:
    print 'ECB mode'

base = ''
for i in range(0,15):
    base += 'A'

base += unknownStr

plainText = ''
for i in range(0,len(base)-15):
    currentCipher = cipherObj.encrypt(base[i:16+i])
    for letter in string.printable + ' ':
        if(currentCipher == cipherObj.encrypt(base[i:15+i]+letter)):
            plainText += letter
print plainText