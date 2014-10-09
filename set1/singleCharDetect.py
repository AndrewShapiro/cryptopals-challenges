import set1
import string

lines = (line.rstrip('\n') for line in open('4.txt'))
best = []
for line in lines:
    best.append(set1.breakSingleCharXOR(set1.strToHex(line)))
print sorted(best)[-1]