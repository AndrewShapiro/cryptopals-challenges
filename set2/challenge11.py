from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Random import random
import array
import sys
sys.path.append('../set1')
import set1
import string

rndfile = Random.new()
key = rndfile.read(16)

frontPadLen = random.choice(range(5, 11))
endPadLen = random.choice(range(5, 11))
frontPad = array.array('B', rndfile.read(frontPadLen))
endPad = array.array('B', rndfile.read(endPadLen))

fileBytes = array.array('B',open(sys.argv[1] , "rb").read())

padded = frontPad + fileBytes + endPad
print padded