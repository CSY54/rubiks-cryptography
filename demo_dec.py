#!/usr/bin/env python3

from RubikEncryption import RubikEncryption

ct  = input('[>] Ciphertext : ').strip().encode()
key = input('[>] Key : ').split()

re = RubikEncryption()
pt = re.decrypt(ct, key)
print('[+] Plaintext : {}'.format(pt))
