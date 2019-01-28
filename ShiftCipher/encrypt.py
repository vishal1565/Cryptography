# code for encryption using Shift Cipher
# for caesar cipher use k = 3

plainText = input("Enter Plaintext: ")
terms = plainText.split()
k = int(input("Enter Key: "))
while k>25 or k<0:
    k = int(input("Key must be between 0-25(both inclusive)\nTry Again\nEnter Key: "))

cipherText = ""

for i in terms:
    temp = []
    for j in i:
        if ord(j)>96:
            temp.append(chr(((ord(j)+k-97)%26)+97))
        else:
            temp.append(chr(((ord(j)+k-65)%26)+65))
    cipherText += "".join(i for i in temp)
    cipherText += " "
print("\nGenerated CipherText is: ")
print(cipherText)