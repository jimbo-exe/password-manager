import pickle
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import gpass as G
import base64
import os


def get_key(gpass):
    with open("gsalt.dat", "rb") as file:
        keysalt = pickle.load(file)

    encryption = PBKDF2HMAC(algorithm=hashes.SHA256(),
                            length=32,
                            salt=keysalt,
                            iterations=1000)

    key = encryption.derive(bytes(gpass, "utf-8"))
    return base64.urlsafe_b64encode(key)


def encrypt_spass(spass, key):
    cipher = Fernet(key).encrypt(spass)
    # add record to database

    return cipher


def decrypt_spass(spasshash, key):
    return Fernet(key).decrypt(spasshash)

