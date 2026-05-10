def gcd(a,b):
    
    while(b != 0):
        a,b=b,a%b

    return a
    

#Take P and Q as input
p = int(input("ENter the Value of p : "))

q = int(input("Enter the value of q : "))

#finding n and phi
n = p*q

phi = (p - 1)*(q - 1)

#Taking e from user
e = int(input("Enter the Value of e : "))

#Checking our GCD
if gcd(e,phi) == 1:

    print("e and phi are co-prime numbers ")

else:
    print("e and gcd are not co-prime numbers ")
    exit()

#Calculate d
d=1

while (e*d) % phi != 1:
    d += 1

#Print Keys
print("Public Key is: ", (e,n))

print("Private Key is: ", (d,n))

#Take message
msg = int(input("Enter the message : "))

#Encryption and Decryption
encryption = (msg ** e) % n
print("Encryption is : " , encryption)

decryption = (encryption ** d) % n
print("Decryption is : " , decryption)