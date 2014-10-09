from Crypto.Cipher import AES
import array
import set1
import sys
import string

lines = (set1.strToHex(line.rstrip('\n')) for line in open('8.txt'))

counted = []
for line in lines:
    i = 0
    count = 0
    while i < len(line)-1:
        byteA = line[i]
        byteB = line[i+1]
        j = i+2
        while j < len(line)-1:
            if(line[j] == byteA and line[j+1] == byteB):
                count += 1
            j += 1
        i+=1
    counted.append((count, ''.join(format(x, '02x') for x in line)))
print sorted(counted)[-1]