import os
import shutil
import pickle
import database
import signup


def create_folder(folder_name):
    cwd = os.getcwd()
    folder_path = os.path.join(cwd, folder_name)  # The path of the folder to be created

    if not os.path.isdir(folder_path):  # Checking that the folder does not exist already
        try:
            os.makedirs(folder_path)
            print("Created: " + folder_path)
            os.chdir("bin")
            return True

        except OSError:  # If there is some error
            print("Error occurred. Directory not created.")
            return False

    else:  # If the folder does exist already:
        print("Folder already exists.")

        is_empty = len(os.listdir(folder_path)) == 0  # Check if the folder is empty
        if is_empty:
            print("Folder is empty. Continuing installation.")
            os.chdir("bin")  # Just use this folder for operation
            return True  # Changing directly for further operations

        else:
            # Need to wipe data in this folder
            # Add a dialogue box (Tkinter) to confirm wiping or not

            confirm = input()
            if confirm:
                try:
                    shutil.rmtree(
                        folder_path
                    )  # If folder is NOT empty, truncate and recreate
                    os.makedirs(folder_path)
                    os.chdir("bin")
                    print("Folder wiped and recreated.")
                    return True
                except OSError:
                    print("Error occurred. Directory not wiped.")
                    return False


def create_file(file_name):
    with open(file_name, "wb"):
        print("File created: ", file_name)


def create_salt():
    with open("gsalt.dat", "wb") as f:
        salt = os.urandom(16)  # A random string of length 16, our salt
        pickle.dump(salt, f)

    with open("keysalt.dat", "wb") as f:
        salt = os.urandom(16)
        pickle.dump(salt, f)


if __name__ == "__main__":
    if create_folder("bin"):
        file_list = [
            "gpass.dat",
            "gsalt.dat",
            "keysalt.dat",
        ]  # All the needed files in folder bin

        for i in range(len(file_list)):
            create_file(file_list[i])
            if i != 0:
                with open(file_list[i], "wb") as file:
                    create_salt()

    database.initiate_db()
    database.initiate_table()
    signup.showWindow()