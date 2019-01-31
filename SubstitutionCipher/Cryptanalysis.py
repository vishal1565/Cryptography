# Python code for Cryptanalysis of Monoalphabetic Substitution Cipher
# Author: yamraj1565

import sys
import os
import itertools

prob = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.996, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]

# Taking input from "input.txt"
# Sorting probs
keys = []
for i in range(26):
    temp = [prob[i],chr(97+i)]
    keys.append(temp)

# Sorting Keys...
keys.sort(reverse = True)
fileName = "input.txt"
fp  = open(fileName,"r")
cipherText = str(fp)

# Trying Replacement for top 10 keys...