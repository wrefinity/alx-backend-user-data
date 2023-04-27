#!/usr/bin/env python3
"""
password encryptions
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    return a bytes of salted and hashed password
    """
    enc = password.encode()
    encrypted = bcrypt.hashpw(enc, bcrypt.gensalt())
    return encrypted


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    check that hashed password and new password is same
    """
    is_val = False
    enc = password.encode()
    if bcrypt.checkpw(enc, hashed_password):
        is_val = True
    return is_val
