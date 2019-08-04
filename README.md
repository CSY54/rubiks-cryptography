# Rubik's Cryptography

A project for Crypto @ AIS3 2019.

Just a simple demo for a 3 x 3 x 3 Rubik's Cube.
These code were written within 2 hours, there might be lots of bugs in it.

## How It Works

### Encryption

1. Turn the plaintext into binary data
2. Pad 0 in the front of the binary until the length is the multiple of the cube size, which is 54 in 3 x 3 x 3
3. Fill the 0s and 1s in the order mentioned in the next section
4. Rotate using the key, where key should be a array
5. Extract every bit in the order then turn the binary data into string (hex)

(Optional: Compress the key using Huffman Encoding, which is a lossless compression algorithm and will make the size of the key become smaller to store.)

### Decryption

(Optional: Decompress the key file using Huffman Encoding)

1. Turn the ciphertext into binary data
2. Fill the 0s and 1s in the order mentioned in the next section
3. Rotate back using the reverse of the key
4. Extract every bit in the order then turn the binary data into string

## How To Use

Here is a `state` of a Rubik's Cube with id on it.

```
          00 01 02
          03 04 05
          06 07 08

09 10 11  18 19 20  27 28 29  36 37 38
12 13 14  21 22 23  30 31 32  39 40 41
15 16 17  24 25 26  33 34 35  42 43 44

          45 46 47
          48 49 50
          51 52 53
```

Here are valid keys (in Rubik's Cube notation)
`U L F R B D M E S Ui Li Fi Ri Bi Di Mi Ei Si`

### Encryption

```python
#!/usr/bin/env python3

from RubikEncryption import RubikEncryption

pt  = input('[>] Plaintext : ').strip()
key = input('[>] Key : ').strip().split()

re = RubikEncryption()
ct = re.encrypt(pt.encode, key)
print('[+] Ciphertext : {}'.format(ct))
```

### Decryption

```python
#!/usr/bin/env python3

from RubikEncryption import RubikEncryption

ct  = input('[>] Ciphertext : ').strip()
key = input('[>] Key : ').strip().split()

re = RubikEncryption()
pt = re.decrypt(ct.encode(), key)
print('[+] Plaintext : {}'.format(pt))
```
