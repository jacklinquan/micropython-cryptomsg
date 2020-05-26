# micropython-cryptomsg
[![PyPI version](https://badge.fury.io/py/micropython-cryptomsg.svg)](https://badge.fury.io/py/micropython-cryptomsg) [![Downloads](https://pepy.tech/badge/micropython-cryptomsg)](https://pepy.tech/project/micropython-cryptomsg)

A MicroPython module to encrypt and decrypt messages with AES CBC mode.

This module only works under MicroPython and it is tested with MicroPython V1.12.

For a compatible CPython version, please find [Python package cryptomsg](https://github.com/jacklinquan/cryptomsg).

Please consider [![Paypal Donate](https://github.com/jacklinquan/images/blob/master/paypal_donate_button_200x80.png)](https://www.paypal.me/jacklinquan) to support me.

## Installation
``` Python
>>> import upip
>>> upip.install('micropython-cryptomsg')
```
Alternatively just copy cryptomsg.py to the MicroPython device.

## Usage
``` Python
>>> from cryptomsg import CryptoMsg
>>> message = 'YOUR MESSAGE'
>>> # Use default key and iv, not secure.
>>> cipher = CryptoMsg().encrypt_msg(message)
>>> cipher
b"E\xa8\x02\x08\xa3+m\xce'1\xc2\x1c\xa3\xeb\x06\x05"
>>> CryptoMsg().decrypt_msg(cipher)
b'YOUR MESSAGE'
>>> # Only set key, and iv is the same as key.
>>> cipher = CryptoMsg(b'YOUR KEY').encrypt_msg(message)
>>> cipher
b'o\x8e\xa8\x13\xda )\x10zS\xfd\xf5\xae\x90\x95\xfb'
>>> CryptoMsg(b'YOUR KEY').decrypt_msg(cipher)
b'YOUR MESSAGE'
>>> # Set both key and iv, strongest encryption. 
>>> cipher = CryptoMsg(b'YOUR KEY', b'YOUR IV').encrypt_msg(message)
>>> cipher
b'\xbflr\xf6\xae\xc1\xf9W\xfc\xcd&\xf3R\xd3\x8b\xde'
>>> CryptoMsg(b'YOUR KEY', b'YOUR IV').decrypt_msg(cipher)
b'YOUR MESSAGE'
```
