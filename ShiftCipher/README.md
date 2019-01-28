# Shift Cipher
It is one of the classical Cryptosystem. </br>
It can be characterized by</br>
P = Z<sub>26</sub> = {0,1,2,3...,25}</br>
C = Z<sub>26</sub></br>
K = Z<sub>26</sub></br></br>
Encryption:</br>
    if x is the plaintext then</br>
    e<sub>k</sub> = (x+k) mod 26 = y (cipher text)</br>
    Also, y ∈ Z<sub>26</br></br>
    
Decryption:</br>
    if y is the cipher text then</br>
    d<sub>k</sub>(y) = (y-k) mod 26</br></br>
    
NOTE: Caeser Cipher is a paticular case of Shift Cipher where k = 3.</br>
