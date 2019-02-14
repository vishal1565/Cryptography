msg = input("Enter a Message:").split()
key = input("Enter Key: ")
m = len(key)
key = key.upper()
mval = [(ord(i)-65) for i in key]
msg = "".join(i for i in msg)
msg = msg.lower()
text = []
for i in range(len(msg)):
    text.append(chr((ord(msg[i])-97+mval[i%m])%26+65))
cipherText = "".join(i for i in text)
print("CipherText:",cipherText)
