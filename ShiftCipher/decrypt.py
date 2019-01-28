# code for Decryption of Shift Cipher
# for caesar cipher use k = 3

cipherText = input("Enter Cipher Text: ")
terms = cipherText.split()
k = int(input("Enter the Key: "))

plainText = ""

for i in terms:
    temp = []
    for j in i:
        if ord(j)>96:
            temp.append(chr(((ord(j)-97-k)%26)+97))
        else:
            temp.append(chr(((ord(j)-65-k)%26)+65))
    plainText += "".join(i for i in temp)
    plainText += " "

print("\nMessage is:")
print(plainText)
