#!/usr/bin/env python3

from Rubik import Rubik
from Crypto.Util.number import bytes_to_long, long_to_bytes
from base64 import b64encode, b64decode

class RubikEncryption():

    valid = ['U', 'L', 'F', 'R', 'B', 'D', 'M', 'E', 'S', 'Ui', 'Li', 'Fi', 'Ri', 'Bi', 'Di', 'Mi', 'Ei', 'Si']

    def __init__(self, mode=0, debug=False, animation=False):
        # mode: bin -> 0 | hex -> 1
        self.mode = mode
        self.debug = debug
        self.animation = animation
        if mode != 0:
            raise NotImplementedError('meow')

    def encrypt(self, plaintext, key):
        # plaintext
        if type(plaintext) != bytes:
            raise TypeError('Type of plaintext must be bytes')

        plaintext = bin(bytes_to_long(plaintext)).lstrip('0b')
        self.plaintext = self.pad(plaintext)

        if self.debug:
            print('[+] self.plaintext : {}'.format(self.plaintext))

        # key
        if type(key) != list:
            raise TypeError('Key must be list')
        if any(i not in self.valid for i in key):
            raise ValueError('Key invalid')

        self.key = key
        self.part = [self.plaintext[i:i + 54] for i in range(0, len(self.plaintext), 54)]

        # run
        self.ciphertext = self.run()

        if self.debug:
            print('[+] self.ciphertext : {}'.format(self.ciphertext))

        return b64encode(long_to_bytes(int(self.ciphertext, 2))).decode()

    def decrypt(self, ciphertext, key):
        # ciphertext
        if type(ciphertext) != bytes:
            raise TypeError('Type of ciphertext must be bytes')

        ciphertext = bin(bytes_to_long(b64decode(ciphertext))).lstrip('0b')
        self.ciphertext = self.pad(ciphertext)

        if self.debug:
            print('[+] self.ciphertext : {}'.format(self.ciphertext))

        # key
        if type(key) != list:
            raise TypeError('Key must be list')
        if any(i not in self.valid for i in key):
            raise ValueError('Key invalid')

        self.key = [k[0] if 'i' in k else k + 'i' for k in key[::-1]]
        self.part = [self.ciphertext[i:i + 54] for i in range(0, len(self.ciphertext), 54)]

        # run
        self.plaintext = self.run()

        if self.debug:
            print('[+] self.plaintext : {}'.format(self.plaintext))

        return long_to_bytes(int(self.plaintext, 2)).decode()

    def run(self):
        text = ''
        for t in self.part:
            cube = Rubik(list(t), debug=self.debug, animation=self.animation)
            # assert(list(t) == cube.state)
            cube.run(self.key)
            if self.animation:
                text += ''.join(str(_[1]) for _ in cube.state)
            else:
                text += ''.join(str(_) for _ in cube.state)
        return text

    def pad(self, text):
        return '0' * ((54 - len(text) % 54) % 54) + text
