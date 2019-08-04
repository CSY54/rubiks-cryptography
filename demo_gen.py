#!/usr/bin/env python3

from string import ascii_letters, digits
from random import randint, choice

valid = ['U', 'L', 'F', 'R', 'B', 'D', 'M', 'E', 'S', 'Ui', 'Li', 'Fi', 'Ri', 'Bi', 'Di', 'Mi', 'Ei', 'Si']

plaintext = ''.join(choice(ascii_letters + digits) for _ in range(randint(100, 500)))
key       = ' '.join(choice(valid) for _ in range(randint(10, 64))).split()

print('[+] Plaintext : {}'.format(plaintext))
print('[+] Key : {}'.format(' '.join(k for k in key)))
