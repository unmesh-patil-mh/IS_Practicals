# Initial permutation
IP = [2,1,5,6,8,7,3,4]

#Final Permutation is
FP = [3,4,5,6,2,1,8,7]

#Permutation Function
def permute(text,table):

    output = ""

    for i in table:
        output = output + text[i - 1]

    return output

#Plain text Input
plaintext = "11100001"

print("The Plain Text is:" , plaintext)

#Initial Permutation
initial = permute(plaintext,IP)

print("Initial Permutation is:" , initial)

#Encryption using key and XOR
key = "11000011"

encryption = ""

for i in range(len(initial)):
    
    if initial[i] == key[i]:
        encryption = encryption + "0"

    else:
        encryption = encryption + "1"

print("The Encrypted text is:" , encryption)

#Final Permutation
cipher = permute(encryption,FP)

print("The Final Permutation is:" , cipher)