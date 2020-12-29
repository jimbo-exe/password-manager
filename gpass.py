import hashlib
import pickle
import os

def setgpass(password):
    # Hashlib functions expect byte input, so we need to input the password and convert it into a byte format
    

    with open("gsalt.dat", "rb") as file:
        salt = pickle.load(file)        # Load the salt from the bin folder

    # The hash we will be storing. Algortihm: SHA256, salt: Read from file, number of iterations: 100
    passhash = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100)  # Creates the hash of the input password

    with open("gpass.dat", "wb") as datfile:
        pickle.dump(passhash, datfile)      # Gpass stored in the dat file
        print("New password set.")


def checkgpass():
    with open("gsalt.dat", "rb") as file:
        salt = pickle.load(file)

    with open("gpass.dat", "rb") as datfile:
        try:
            passhash = pickle.load(datfile)
        except EOFError:        # If the file is empty, it means no password has been set yet
            print("Correct password not know. Kindly set a password first.")

    attempt = bytes(input("Enter the password: "), "utf-8")     # Change to byte, since hashlib expects byte
    attempthash = hashlib.pbkdf2_hmac("sha256", attempt, salt, 100)

    if attempthash == passhash:     # Gpass is correct if the hash matches the stored hash
        print("Correct password. You're in.")

    else:
        print("Incorrect password. Try Again.")


if __name__ == "__main__":
    path = os.path.join(os.getcwd(), "bin")
    os.chdir(path)      # Im using files from the bin folder so I changed directory to it

    print("What do you want to do:",
          "1 - Set New Password",
          "2 - Enter Password", sep="\n", end=": ")
    cmd = int(input())

    if cmd == 1:
        setgpass()

    elif cmd == 2:
        checkgpass()
