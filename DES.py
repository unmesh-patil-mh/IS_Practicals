# pip install pycyptodome install this to create enviroment

from Crypto.Cipher import DES

key = b'87654321'

cipher = DES.new(key , DES.MODE_ECB)

text = b'HELLO123'

#Encrtption
encrypted = cipher.encrypt(text)
print("Cipher Text is : " , encrypted)

#Decrypt 
decryption = cipher.decrypt(encrypted)
print("Plain Text is : " + decryption.decode())
