from Crypto.Cipher import AES
import array
import set1
import sys
import string

lines = (set1.strToHex(line.rstrip('\n')) for line in open('8.txt'))

counted = []
for line in lines:
    count = set1.twoByteMatch(line)
    counted.append((count, ''.join(format(x, '02x') for x in line)))
print sorted(counted)[-1]