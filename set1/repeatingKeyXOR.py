import sys
import set1
import array

key = "ICE"
keyBytes = array.array('B', key)
# This will treat files as binary. Use alternate line below for ascii hex
# fileBytes = array.array('B', set1.strToHex(open(sys.argv[1] , "rb").read()))
fileBytes = array.array('B', open(sys.argv[1] , "rb").read())
output = []
i=0
for fileByte in fileBytes:
    output.append(fileByte ^ keyBytes[i % len(key)])
    i += 1
# print ''.join(format(x, '02x') for x in output)

with open(sys.argv[2], 'wb') as outFile:
    outFile.write(bytearray(output))