#!/usr/bin/env python3

from RubikEncryption import RubikEncryption
from Huffman_code import *
from string import ascii_letters, digits
from random import choice

# Encryption
print('[+] Encrypt')

pt = ''.join(choice(ascii_letters + digits) for _ in range(4))
print('[+] Plaintext : {}'.format(pt))

key = [choice(['U', 'L', 'F', 'R', 'B', 'D', 'M', 'E', 'S', 'Ui', 'Li', 'Fi', 'Ri', 'Bi', 'Di', 'Mi', 'Ei', 'Si']) for _ in range(10)]
print('[+] Key : {}'.format(' '.join(key)))

re = RubikEncryption(debug=False, animation=True)
ct = re.encrypt(pt, key)
print('[+] Ciphertext : {}'.format(ct))

# Huffman encode key to file
with open('key', 'w') as f:
    f.write(' '.join(key))
compress('key', 'key_enc')

print('\n' * 5)

# Decryption
print('[+] Decrypt')

print('[+] Ciphertext : {}'.format(ct))

# read key from key file and decompress it
decompress('key_enc', 'key_dec')
with open('key_dec', 'r') as f:
    key = f.read().split()

print('[+] Key : {}'.format(key))

re = RubikEncryption(debug=False, animation=True)
pt = re.decrypt(ct, key)
print('[+] Plaintext : {}'.format(pt))
