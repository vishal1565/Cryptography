# Vigenere Cipher
<br>
Vigenere Cipher is a Polyalphabetic Substitution Cipher. That is an alphabet is not mapped to a single alphabet in cipher-text.<br>
<b>Properties:</b><br>
Let m be a positive integer<br>
P = (Z<sub>26</sub>)<sup>m</sup><br>
C = (Z<sub>26</sub>)<sup>m</sup><br>
K = (Z<sub>26</sub>)<sup>m</sup><br><br>
If x is plaintext and x = (x<sub>1</sub>,x<sub>2</sub>,...,x<sub>m</sub>)<br><br>
then encryption can be done as<br>
e<sub>k</sub>(x) = (x<sub>1</sub>+k<sub>1</sub>,x<sub>2</sub>+k<sub>2</sub>,...,x<sub>m</sub>+k<sub>m</sub>) = = (y<sub>1</sub>,y<sub>2</sub>,...,y<sub>m</sub>)<br><br>
and decrytption is done as<br>
d<sub>k</sub>(y) = (y<sub>1</sub>-k<sub>1</sub>,y<sub>2</sub>-k<sub>2</sub>,...,y<sub>m</sub>-k<sub>m</sub>)<br>
