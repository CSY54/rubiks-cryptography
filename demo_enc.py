#!/usr/bin/env python3

from RubikEncryption import RubikEncryption

pt  = input('[>] Plaintext : ').strip().encode()
key = input('[>] Key : ').split()

re = RubikEncryption()
ct = re.encrypt(pt, key)
print('[+] Ciphertext : {}'.format(ct))
