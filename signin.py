from tkinter import *
import gpass
import mainscreen
import os


def signin_win():
    global root
    global pwdE
    
    os.chdir("bin")
    root = Tk()
    root.title("Sign in")

    root.geometry("250x125")
    root.resizable(0, 0)

    headingL = Label(root, text="Sign in", font="Helvetica 25 bold")
    headingL.grid(row=0, column=0, columnspan=4, rowspan=1)

    pwdL = Label(root, text="Password: ", font="Helvetica 15") 
    pwdL.grid(row=1, column=1, sticky=W)  

    pwdE = Entry(root, show="*")
    pwdE.grid(row=1, column=2, columnspan=2, sticky=W)

    cancelB = Button(root, text="Cancel", fg="red", command=root.destroy)
    cancelB.grid(row=2, column=1, columnspan=2)

    signupB = Button(root, text="Sign in", fg="green", command=attempt )
    signupB.grid(row=2, column=3, sticky=W)

def attempt():
    pwd = pwdE.get()

    if gpass.checkgpass(pwd):
        root.destroy()
        mainscreen.initiate()
        mainscreen.initiate_tabs()
        mainscreen.show_welcome()
        mainscreen.root.mainloop()
    else:
        incorrectL = Label(root, text="Password incorrect", fg="red")
        incorrectL.grid(row=3, column=1)








    

    

