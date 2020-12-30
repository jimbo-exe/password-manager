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
        print("New password set.")


def checkgpass(attempt):
    with open("gsalt.dat", "rb") as file:
        salt = pickle.load(file)

    with open("gpass.dat", "rb") as datfile:
        try:
            passhash = pickle.load(datfile)
        except EOFError:  # If the file is empty, it means no password has been set yet
            print("Correct password not know. Kindly set a password first.")

    attempthash = hashlib.pbkdf2_hmac("sha256", attempt.encode("utf-8"), salt, 100)

    if attempthash == passhash:  # Gpass is correct if the hash matches the stored hash
        return True

    else:
        return False


if __name__ == "__main__":
    path = os.path.join(os.getcwd(), "bin")
    os.chdir(path)  # Im using files from the bin folder so I changed directory to it

    print(
        "What do you want to do:",
        "1 - Set New Password",
        "2 - Enter Password",
        sep="\n",
        end=": ",
    )
    cmd = int(input())

    if cmd == 1:
        while True:
            password = input("Enter the new password: ")
            confirm = input("Confirm password: ")

            if password == confirm:
                break
        setgpass(password)

    elif cmd == 2:
        attempt = input("Enter the password: ")
        if checkgpass(attempt):
            print("Correct password. You're in.")
        else:
            print("Wrong password. Try again")
