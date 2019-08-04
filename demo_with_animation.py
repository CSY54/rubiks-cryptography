#!/usr/bin/env python3

from RubikEncryption import RubikEncryption
from Huffman_code import *
from string import ascii_letters, digits
from random import choice

pt = ''.join(choice(ascii_letters + digits) for _ in range(4)).encode()
print('[+] Plaintext : {}'.format(pt))

key = [choice(['U', 'L', 'F', 'R', 'B', 'D', 'M', 'E', 'S', 'Ui', 'Li', 'Fi', 'Ri', 'Bi', 'Di', 'Mi', 'Ei', 'Si']) for _ in range(10)]
print('[+] Key : {}'.format(' '.join(_ for _ in key)))

re = RubikEncryption(debug=True, animation=True)
ct = re.encrypt(pt, key)
print('[+] Ciphertext : {}'.format(ct))

# Huffman encode key file
with open('key', 'w') as f:
    f.write(' '.join(_ for _ in key))
compress('key', 'key_enc')

############################################################

# read key from key file and decompress it
decompress('key_enc', 'key_dec')
with open('key_dec', 'r') as f:
    key = f.read().split()
print('key = {}'.format(key))
re = RubikEncryption(debug=True, animation=True)
pt = re.decrypt(ct, key)
print('[+] Plaintext : {}'.format(pt))
