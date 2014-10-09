import sys
import array
import set1

def hammingDistance(a, b):
    if len(a) != len(b):
        print "hammingDistance: lengths aren't equal"

    sum = 0
    for byteA, byteB in zip(a,b):
        sum += bin(byteA ^ byteB).count('1')
    return sum

fileContents = open(sys.argv[1] , "rb").read()   

input = set1.strToHex(fileContents)
guesses = []
for keyLenGuess in range (1, 40):
    block1 = input[ : keyLenGuess+1]
    block2 = input[keyLenGuess : (2 * keyLenGuess)+1]
    block3 = input[(2 * keyLenGuess) : (3 * keyLenGuess)+1]
    block4 = input[(3 * keyLenGuess) : (4 * keyLenGuess)+1]


    distanceNorm = (hammingDistance(block1, block2) + hammingDistance(block3, block4) + hammingDistance(block1, block3) + hammingDistance(block4, block1)) / (keyLenGuess * 4.)
    guesses.append((distanceNorm, keyLenGuess))
# print sorted(guesses)
guess = sorted(guesses)[0][1]

lenGuesses = [x[1] for x in sorted(guesses)[:3]]
byteWiseBlocks = [[] for x in range(0, guess)]

for i, byte in enumerate(input):
    byteWiseBlocks[i %  guess].append(byte)

key = ''
for i in range(0,29):
    key += str(set1.breakSingleCharXOR(byteWiseBlocks[i])[1])
print key