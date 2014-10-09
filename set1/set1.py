import array

def strToHex(hexString):
    hexData = hexString.decode("hex")
    array.array('B', hexData)
    return map(ord,hexData)

def bufferXOR(a,b):
    output = []
    if len(a) != len(b):
        print 'bufferXOR: buffers not same length!'
    for byteA, byteB in zip(a, b):
        output.append(byteA ^ byteB)
    return output

def byteXOR(buf, byte):
    output = []
    for bufByte in buf:
        output.append(bufByte ^ byte)
    return output

def breakSingleCharXOR(inputBlock):
    freqDict = {'E':12, 'T':9, 'A':8, 'O':7.5, 'I':7, 'N':6.7, 'S':6.3, 'H': 6, 'R':  6, 'D': 4.25, 'L': 4, 'U': 2.75, ' ': 3 }

    pTexts = []
    for char in range(0, 127):
        result = "".join(map(chr, byteXOR(inputBlock, char)))
        pTexts.append((chr(char), result))
    ranked = []
    for (char, text) in pTexts:
        sum = 0

        for letter in text.upper():  
            # if ord(letter) != 0 and (ord(letter) <= 31 or ord(letter) >= 127):
            #     sum = -1
            #     break
            if freqDict.has_key(letter):
                sum += freqDict[letter]
        ranked.append((sum, char, text))
    # for (rank, char,text) in sorted(ranked):
    #     print ('{0},{1},{2}').format(rank,char,text)
    return sorted(ranked)[-1]