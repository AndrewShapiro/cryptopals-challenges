def pkcs7Pad(buf, blockLen):
    padNum = blockLen - len(buf) % blockLen
    if(padNum == blockLen):
        return buf
    for _ in range(padNum):
        buf.append(padNum)
    return buf

def pkcs7Validation(str):
    if ord(str[-1]) < 32:
        i = 2
        while(i <= ord(str[-1])):
            if ord(str[-i]) != ord(str[-1]):
                return (False, '')
            i += 1
        return (True, str[:-(i-1)])
    return (False, '')