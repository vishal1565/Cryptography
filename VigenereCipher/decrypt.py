cipherText = input("Enter CipherText: ")
cipherText.upper()
key = input("Enter Key: ")
m = len(key)
key = key.upper()
mval = [(26-ord(i)+65) for i in key]
text = []
for i in range(len(cipherText)):
    text.append(chr((ord(cipherText[i])+mval[i%m]-65)%26+97))
pt = "".join(i for i in text)
print("PlainText:",pt)