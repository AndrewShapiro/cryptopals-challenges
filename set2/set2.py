def pkcs7Pad(buf, blockLen):
    padNum = blockLen - len(buf) % blockLen
    if(padNum == blockLen):
        return buf
    for _ in range(padNum):
        buf.append(padNum)
    return buf