from Crypto.Cipher import AES
import sys
import array
import binascii
import array
import struct
sys.path.append('../set1')
import set1
if(len(sys.argv) == 2):
    inputText = array.array('B',open(sys.argv[1] , "rb").read())
else:
    inputText = array.array('B', binascii.a2b_base64('L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=='))
key = 'YELLOW SUBMARINE'
cipherObj = AES.new(key,AES.MODE_ECB) 
nonce = "\x00\x00\x00\x00\x00\x00\x00\x00"
counter = 0
output = []
keyBlockLen = 16
numBlocks = len(inputText) / 16

if (len(inputText) % 16 != 0):
    numBlocks += 1

for block in range(0, numBlocks):
    if (block == numBlocks -1 ):
        keyBlockLen = len(inputText) % 16

    countStr = struct.pack('L', counter)
    counter += 1
    keyBlock = array.array('B', cipherObj.encrypt(nonce + countStr))
    output += set1.bufferXOR(keyBlock[:keyBlockLen],inputText[16*block:16*(block+1)])

# print output
print ''.join([chr(x) for x in output])