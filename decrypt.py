"""
File: decrypt.py
Decrypts an input string of lowercase letters and prints the result.
The other input is the distance value.
"""

code = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))
plainText = ""
for ch in code:
    ordValue = ord(ch)
    cipherValue = ordValue - distance
    if cipherValue < ord('a'):
        cipherValue = ord('z') - (distance - (ord('a') - ordValue + 1))
    plainText += chr(cipherValue)
print(plainText)


"""
# Prompt user to enter a message
code = input("Enter the coded text: ")
# Prompt user to enter a shift
distance = int(input("Enter the distance value: "))
# Print the decrypted message
plainText = ""
for ch in code:
    ordValue = ord(ch)
    cipherValue = ordValue + distance
    if cipherValue > ord('z'):
        cipherValue = ord('a') + (distance - (ord('z') - ordValue + 1))
        cipherValue -= 102
    plainText += chr(cipherValue)
print(plainText)
print(cipherValue)
"""