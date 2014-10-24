from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Random import random
import set2
import array
uid = -1

def parse(fields):
    fields = fields.split('&')
    obj = {}
    for field in fields:
        split = field.split('=')
        obj[split[0]] = split[1]
    return obj

def profile_for(email):
    global uid  
    email= email.translate(None, '&=')
    uid += 1
    return ({'email': email, 'uid': uid, 'role': 'user'}, 'email=' + email + '&uid=' + str(uid) + '&role=user')

# print parse("foo=bar&baz=qux&zap=zazzle")
# print profile_for('foo@bar.com')

profile1 = profile_for('fo0000@bar.com')[1]
maliciousEmail = 'fo@bar.com'+''.join(format(x, '01c') for x in set2.pkcs7Pad(array.array('B', 'admin\0'),16))
profile2 = profile_for(maliciousEmail)[1]

rndfile = Random.new() 
key = rndfile.read(16)
cipherObj = AES.new(key,AES.MODE_ECB) 

forgeFront = cipherObj.encrypt(set2.pkcs7Pad(array.array('B', profile1), 16))
forgeBack = cipherObj.encrypt(set2.pkcs7Pad(array.array('B', profile2), 16))

forgedCredentials = forgeFront[:32] + forgeBack[16:32]

maliciousDecrypt = cipherObj.decrypt(forgedCredentials)
print repr(maliciousDecrypt)
print parse(maliciousDecrypt)