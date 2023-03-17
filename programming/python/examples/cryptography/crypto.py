#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# [pycryptodome (stackoverflow)](https://stackoverflow.com/questions/43987779/python-module-crypto-cipher-aes-has-no-attribute-mode-ccm-even-though-pycry)
# pip3 install pycryptodome

import hashlib
# [pycryptodome.readthedocs.io](https://pycryptodome.readthedocs.io/en/latest/src/cipher/cipher.html)
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_v1_5
import base64

def pp(*args, **kwargs):
    print(*args, **kwargs, sep=':\t')

def ctr(head, *args, **kwargs):
    print('\n', f' {head} '.center(79, '-'), sep='', *args, **kwargs)

protokey_str = 'HappinessCakesHappiness'
pp('protokey_str', protokey_str)

ciphered_str = 'japMApYUMaGjl3912bl5z6s6kljFWVBbHV+absB5EdEm7bDQk/qff5qhxpHRILjpdmYCMiwlPcgxvLEwZoomnvu8+FxpHVcK65eHPcCUAM9rHg9NcfgGc07zTpZyS89yqE2RmCOFgxPCxk+2Kc07SAyBU/3NmR74dnWvpxPuexnxS93ZrSmYZupEr5S9KwQ88t2SEKR0Rm052h+BRQWsL1x/BlTGuspMEVcR2UybmzyPseuv/+nNQfhiYZnbC34jTigNSZD7bz0Lw2pYoSHLGhLTGZ/8V5P+Emk42S1JwaCvS7G/xH/AK22C/ekQfk1Q'
pp('ciphered_str', ciphered_str)

ctr('Prepare key from protokey') # --------------------------------------------

protokey_bytes = bytes(protokey_str, 'utf-8')
pp('protokey_bytes', protokey_bytes)

# [hashlib (docs)](https://docs.python.org/3/library/hashlib.html)
key_sha1_bytes = hashlib.sha1(protokey_bytes)
pp('key_sha1_bytes', key_sha1_bytes)

key_sha1 = key_sha1_bytes.digest()  # hexdigest()
pp('type(key_sha1)', type(key_sha1))
pp('len(key_sha1)', len(key_sha1))
pp('key_sha1', key_sha1)

key_sha1_16 = key_sha1[:16]
pp('key_sha1_16', key_sha1_16)

ctr('Decode ciphered message') # ----------------------------------------------
print()

cipher = AES.new(key_sha1_16, AES.MODE_ECB)

decrypted = cipher.decrypt(base64.b64decode(ciphered_str))         # desifruju 
pp('decrypted', decrypted.decode())

# ciphertext = b64decode(data.encode())
# [How to use RSA or similar encryption in Python 3?](https://stackoverflow.com/questions/44223479/how-to-use-rsa-or-similar-encryption-in-python-3)
# rsa_decryption_cipher = PKCS1_v1_5.new(key_sha1_16)
# plaintext = rsa_decryption_cipher.decrypt(encoded_message, 16)
# b64decode(plaintext).decode()

# print(base64.b32encode(bytes(protokey, 'utf-8')))
# print(len(base64.b32encode(bytes(protokey, 'utf-8'))))

