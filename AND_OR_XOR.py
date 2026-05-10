text = "Hello World"

and_op = ""

or_op = ""

xor_op = ""

for ch in text:

    and_op = and_op + chr(ord(ch) & 127)

    or_op = or_op + chr(ord(ch) | 127)

    xor_op = xor_op + chr(ord(ch) ^ 127)

print("AND Output is : " + and_op)
print("OR Output is : " + or_op)
print("XOR Output is : "+ xor_op)