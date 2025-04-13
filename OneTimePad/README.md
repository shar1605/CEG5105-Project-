# One Time Pad Code

This folder contains a python script that parses a .ino file and replaces plaintext strings with a One Time Pad Cipher. The .ino file directory must contain the `otp_cipher.cpp` and `otp_cipher.h` files.

The python scripts generates a random char array `c0` the length of the string, and calculates `c1` where `c0` XOR `c1` will lead to the generation of the plaintext string. The XOR is done during runtime, meaning that running the strings utility on the binary firmware file will not reveal the plaintext string. 

To look at a demo, `ceg5105_code.ino` is the original code while `new_ceg5105_code.ino` represents the new code after `encrypt_string.py` is called on `ceg5105_code`. 