import set2

str = "ICE ICE BABY\x04\x04\x04\x04"
print set2.pkcs7Validation(str)

str = "ICE ICE BABY\x05\x05\x05\x05"
print set2.pkcs7Validation(str)

str = "ICE ICE BABY\x01\x02\x03\x04"
print set2.pkcs7Validation(str)
