import pickle
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import gpass as G
import base64


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


if __name__ == "__main__":
    attempt = input("Enter the global password: ")
    while not G.checkgpass(attempt):
        print("Password incorrect. Please reenter.")
        attempt = input("Enter the global password: ")

    gpass = attempt

    key = get_key(gpass)

    spass = input("Enter the password of this account: ").encode("utf-8")
    spasshash = encrypt_spass(spass, key)
    print(decrypt_spass(spasshash, key))