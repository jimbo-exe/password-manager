import install
import database
import signup
import signin
import os

if not os.path.isdir("bin"):    # first run
    if install.create_folder("bin"):
        file_list = [
            "gpass.dat",
            "gsalt.dat",
            "keysalt.dat",
        ]  # All the needed files in folder bin

        for i in range(len(file_list)):
            install.create_file(file_list[i])
            if i != 0:
                with open(file_list[i], "wb") as file:
                    install.create_salt()
    database.initiate_db()
    database.initiate_table()
    signup.showWindow()
    signup.root.mainloop()


else:
    signin.signin_win()
    signin.root.mainloop()