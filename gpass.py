import hashlib
import pickle
import os


def setgpass(password):
    # Hashlib functions expect byte input, so we need to input the password and convert it into a byte format

    with open("gsalt.dat", "rb") as file:
        salt = pickle.load(file)  # Load the salt from the bin folder

    # The hash we will be storing. Algortihm: SHA256, salt: Read from file, number of iterations: 100
    passhash = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, 100
    )  # Creates the hash of the input password

    with open("gpass.dat", "wb") as datfile:
        pickle.dump(passhash, datfile)  # Gpass stored in the dat file
    return True


def checkgpass(attempt):
    with open("gsalt.dat", "rb") as file:
        salt = pickle.load(file)

    with open("gpass.dat", "rb") as datfile:
        try:
            passhash = pickle.load(datfile)
        except EOFError:  # If the file is empty, it means no password has been set yet
            print("Correct password not known. Kindly set a password first.")

    attempthash = hashlib.pbkdf2_hmac("sha256", attempt.encode("utf-8"), salt, 100)

    if attempthash == passhash:  # Gpass is correct if the hash matches the stored hash
        return True

    else:
        return False



