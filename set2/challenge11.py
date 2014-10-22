from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Random import random
import array
import sys
sys.path.append('../set1')
import set1
import set2
import string

rndfile = Random.new()
key = rndfile.read(16)

frontPadLen = random.choice(range(5, 11))
endPadLen = random.choice(range(5, 11))
frontPad = array.array('B', rndfile.read(frontPadLen))
endPad = array.array('B', rndfile.read(endPadLen))

fileBytes = array.array('B',open(sys.argv[1] , "rb").read())

padded = set2.pkcs7Pad(frontPad + fileBytes + endPad, 16)
iv = array.array('B', rndfile.read(16))

if(ord(rndfile.read(1)) % 2):
    cipherObj = AES.new(key, AES.MODE_CBC, iv)  
else:
    cipherObj = AES.new(key, AES.MODE_ECB)

cipherText = cipherObj.encrypt(padded)

count = set1.twoByteMatch(cipherText)
print count
if count > 100:
    print 'ECB'
else:
    print 'CBC'