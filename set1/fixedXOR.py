import set1

a = set1.strToHex('1c0111001f010100061a024b53535009181c')
b = set1.strToHex('686974207468652062756c6c277320657965')
result = set1.bufferXOR(a,b)
print ''.join(format(x, '02x') for x in result)