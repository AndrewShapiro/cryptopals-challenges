import array

def intToCharBase64(num):
    if num >= 0 and num <= 25:
        return  chr(num +  ord('A'))
    elif num >= 26 and num <= 51:
        return  chr(num - 26 + ord('a'))
    elif num >= 52 and num <= 61:
        return  chr(num - 52 + ord('0'))
    elif num == 62:
        return '+'
    elif num == 63:
        return '/'
    elif num == '=':
        return '='


def hexToBase64(hexArr):
    output = []
    loopLen = len(hexArr)/3
    i = 0
    j = 0
    while i < loopLen:
        a = (hexArr[i*3] & int('11111100', 2)) >> 2
        b = (hexArr[i*3] & int('00000011', 2)) << 4 | (hexArr[i*3 + 1] & int('11110000', 2)) >> 4
        c = (hexArr[i*3 + 1] & int('00001111', 2)) << 2 | (hexArr[i*3 + 2] & int('11000000', 2)) >> 6
        d = (hexArr[i*3 + 2] & int('00111111',2))  
        output.append(a)
        output.append(b)
        output.append(c)
        output.append(d)
        i += 1
    if len(hexArr) % 3 == 1:
        a = (hexArr[i*3] & int('11111100', 2)) >> 2
        b = (hexArr[i*3] & int('00000011', 2)) << 4
        output.append(a)
        output.append(b)
        output.append('=')
        output.append('=')
    elif len(hexArr) % 3 == 2:
        a = (hexArr[i*3] & int('11111100', 2)) >> 2
        b = (hexArr[i*3] & int('00000011', 2)) << 4 | (hexArr[i*3 + 1] & int('11110000', 2)) >> 4
        c = (hexArr[i*3 + 1] & int('00001111', 2)) << 2
        output.append(a)
        output.append(b)
        output.append(c)
        output.append('=')
    return ''.join(map(intToCharBase64, output))

hexString = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
hexData = hexString.decode("hex")
array.array('B', hexData)
hexData = map(ord,hexData)
data = hexToBase64(hexData)
print(data)