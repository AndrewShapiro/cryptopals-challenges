from Crypto.Cipher import AES
import array
import binascii
import sys
sys.path.append('../set1')
import set1
import set2
from Crypto import Random
from Crypto.Random import random
import string

unknownStr = array.array('B', binascii.a2b_base64('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK'))
rndfile = Random.new()
key = rndfile.read(16)
randPrefix = array.array('B', rndfile.read(ord(rndfile.read(1))))
plainText = randPrefix + array.array('B', open('headLikeAHole.txt' , "rb").read()) + unknownStr

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
baseSize = -1
blockNum = -1
for i in range(1,48):
    base += 'A'
    plainText = set2.pkcs7Pad(randPrefix + array.array('B', base) + unknownStr, blockSize)
    cipherText = cipherObj.encrypt(plainText)
    for j in range(0, len(cipherText) / 16):
        if(cipherText[j * 16 : (j+1) * 16] == cipherText[(j+1) * 16 : (j+2) * 16]):
            print 'matching blocks: ' + str(i) + ' '+ str(len(randPrefix))
            baseSize = i
            blockNum = j
            break
    if(baseSize != -1):
        break


miniBase = ''
for i in range(0,16):
    miniBase += 'A'

for i in range(0,10):
    base += miniBase
blockNum += 10

miniBase = miniBase[1:]

plainText = ''
for i in range(0, 150):
    base = base[1:]
    currentPlain= set2.pkcs7Pad(randPrefix + array.array('B', base) + unknownStr, blockSize)
    currentCipher = cipherObj.encrypt(currentPlain)[blockNum * 16 : (blockNum + 1) * 16]
    for letter in string.printable + ' ':
        if(currentCipher == cipherObj.encrypt(miniBase+letter)):
            plainText += letter
            miniBase = miniBase[1:] + letter
print plainText