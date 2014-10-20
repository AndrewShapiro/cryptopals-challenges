import set2
import array

plainText = array.array('B', 'YELLOW SUBMARINE')
paddedText = set2.pkcs7Pad(plainText, 20)
print repr(''.join(format(x, '01c') for x in paddedText))