import array
import set2
import sys
sys.path.append('../set1')
import set1
import re
import string
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Random import random

def encode(userStr, cipherObj):
    front = "comment1=cooking%20MCs;userdata="
    back = ";comment2=%20like%20a%20pound%20of%20bacon"

    regex = re.compile('(=)')
    userStr = regex.sub('"="', userStr)
    regex = re.compile('(;)')
    userStr = regex.sub('";"', userStr)
    message = set2.pkcs7Pad(array.array('B', front + userStr + back), 16)
    
    return cipherObj.encrypt(message)

def decode(cipherText, cipherObj):
    plainText = cipherObj.decrypt(cipherText)
    print plainText
    if(string.find(plainText, ';admin=true;') >= 0):
        print True
    else:
        print False

rndfile = Random.new() 
key = rndfile.read(16)
iv = array.array('B', rndfile.read(16))
cipherObj = AES.new(key, AES.MODE_CBC, iv)
cipherText = encode("YELLOW SUBMARINEYELLOW SUBMARINE", cipherObj)
cipherText = array.array('B', cipherText)
cipherText[32:47] = array.array('B', set1.bufferXOR(set1.bufferXOR(array.array('B', 'YELLOW SUBMARINE'), set2.pkcs7Pad(array.array('B', ';admin=true;'), 16)),  cipherText[32:47]) )

cipherObj = AES.new(key, AES.MODE_CBC, iv)
decode(cipherText, cipherObj)
