text = str(input("Enter the text you want to Encrypt : "))
key = 2

#Encryption 
encrypted = ""
for i in range(len(text)):
    new_pos = (i + key) % len(text)
    # encrypted = text[::-1]
    encrypted = encrypted + text[new_pos]

print("Encrypted Text is : "+encrypted)

# Decryption
decrypted = ""
for i in range(len(encrypted)):
    old_pos = (i - key) % len(encrypted)
    # decrypted = text[::1]
    decrypted = decrypted + encrypted[old_pos]

print("Decrypted text is : "+decrypted)