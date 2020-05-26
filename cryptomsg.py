# -*- coding: utf-8 -*-
"""A MicroPython module to encrypt and decrypt messages with AES CBC mode.

Author: Quan Lin
License: MIT
"""

from ucryptolib import aes

# Project version
__version__ = '0.1.0'
__all__ = ['CryptoMsg']

def pad_msg16(msg):
    """Pad message with space to the nearest length of multiple of 16."""
    pads = (16 - (len(msg) & 0xF)) & 0xF
    return msg + b' ' * pads

def pad_PKCS7(msg):
    """Pad message with PKCS7. It could add another 16 bytes."""
    pads = 16 - (len(msg) & 0xF)
    return msg + bytes([pads]) * pads

class CryptoMsg(object):
    """A class to encrypt and decrypt messages with AES CBC mode."""
    def __init__(self, aes_cbc_key=b'aes_cbc_key', aes_cbc_iv=None):
        self.aes_cbc_key = aes_cbc_key
        if aes_cbc_iv is None:
            self.aes_cbc_iv = self.aes_cbc_key
        else:
            self.aes_cbc_iv = aes_cbc_iv

    def encrypt_msg(self, msg):
        """Encrypt message."""
        aescbc = aes(
            pad_msg16(self.aes_cbc_key)[:32],
            2,
            pad_msg16(self.aes_cbc_iv)[:16]
        )
        msg = bytearray(msg)
        cipher = bytearray()
        while len(msg) >= 16:
            cipher += aescbc.encrypt(msg[:16])
            msg = msg[16:]
        cipher += aescbc.encrypt(pad_PKCS7(msg))
        
        return bytes(cipher)
        
    def decrypt_msg(self, cipher):
        """Decrypt message."""
        aescbc = aes(
            pad_msg16(self.aes_cbc_key)[:32],
            2,
            pad_msg16(self.aes_cbc_iv)[:16]
        )
        cipher = bytearray(cipher)
        decrypted_msg = bytearray()
        while len(cipher) >= 16:
            decrypted_msg += aescbc.decrypt(cipher[:16])
            cipher = cipher[16:]
        if cipher:
            raise Exception('Invalid cipher length!')
        pads = decrypted_msg[-1]
        if pads > 16:
            raise Exception('Invalid cipher padding!')
        decrypted_msg = decrypted_msg[:-pads]
        
        return bytes(decrypted_msg)
