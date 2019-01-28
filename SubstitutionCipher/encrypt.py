# Python code for Substitution Cipher
# Save PlainText or Message in PlainText.txt
# Key will be generated randomly and will be saved in key.txt
# You will be asked if you want to use Existing Key

import random

msgFile = 'PlainText.txt'
pt = open(msgFile,'r')
print("Taking Message/Plain Text from 'PlainText.txt'..")
keyOption = input("Generate a Random Key? (Y|N): ")
if keyOption == 'Y' or keyOption == 'y':
    # Now generating Random Key
    temp = [i for i in range(26)]
    key = []
    for i in range(26):
        tmp = random.randint(0,len(temp)-1)
        key.append(chr(temp[tmp]+65))
        del temp[tmp]
    print("Saving Key in 'key.txt'....")
    fp = open("key.txt","w")
    fp.write("".join(i for i in key))
else:
    # Using an Existing Key
    fp = open("key.txt","r")
    key = list("".join(i for i in list(fp)))

plainText = (list(pt))[0]
terms = plainText.split()

print("\nNow Encrypting Text...")
cipherText = ""
for i in terms:
    temp = []
    for j in i:
        if ord(j)>96:
            temp.append(key[ord(j)-97])
        else:
            temp.append(key[ord(j)-65])
    cipherText += "".join(i for i in temp)
fp = open("Output.txt","w")
fp.write(cipherText)

print("\nEncryption Successful...\nCipher Text saved in 'Output.txt'")
