from Crypto.Cipher import AES
import array
import set1
import sys
import string

fileBytes = array.array('B', set1.strToHex(open(sys.argv[1] , "rb").read()))
cipherObj = AES.new('YELLOW SUBMARINE', AES.MODE_ECB)
cipherText = cipherObj.decrypt(fileBytes)
print cipherText