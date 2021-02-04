from tkinter import *
import gpass
import os
import mainscreen


def showWindow():
    global root
    global pwdE
    global confirmE

    root = Tk()
    root.title("Password Manager")

    root.geometry("500x200")
    root.resizable(0, 0)

    instruction = Label(
        root, text="Please Enter Master Password", font="Helvetica 20 bold"
    )  # This puts a label, so just a piece of text saying 'please enter blah5
    instruction.grid(
        row=0, column=0, columnspan=3, sticky=E
    )  # This just puts it in the window, on row 0, col 0. If you want to learn more look up a tkinter tutorial :)

    headingL = Label(
        root,
        text="\nWelcome to the Password Keeper. We need you to enter a global password which will be asked each time you want to view stored passwords.\n",
        justify="left",
        wraplength=300,
    )  # This just does the same as above, instead with the text new username.
    headingL.grid(
        row=1, column=0, columnspan=3, rowspan=3, sticky=W
    )  # Same thing as the instruction var just on different rows. :) Tkinter is like that.

    pwdL = Label(root, text="Master Password: ")  # ""
    pwdL.grid(row=5, column=0, sticky=W)  # ""

    confirmL = Label(root, text="Confirm Password: ")  # ""
    confirmL.grid(row=6, column=0, sticky=W)  # ""

    pwdE = Entry(
        root, show="*"
    )  # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    pwdE.grid(row=5, column=1)  # ^^

    confirmE = Entry(
        root, show="*"
    )  # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    confirmE.grid(row=6, column=1)  # ^^

    signupB = Button(
        root, text="Sign Up", fg="green", command=checkPwd
    )  # , command=storeGlobalPwd) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    signupB.grid(row=7, column=2, sticky=W)

    cancelB = Button(root, text="Cancel", fg="red", command=root.destroy)
    cancelB.grid(row=7, column=3, sticky=W)


def checkPwd():
    if pwdE.get() == confirmE.get():
        gpass.setgpass(pwdE.get())
        root.destroy()
        mainscreen.initiate()
        mainscreen.initiate_tabs()
        mainscreen.show_welcome()
    else:
        mismatchL = Label(root, text="Passwords don't match", fg="red")
        mismatchL.grid(row=7, column=1)



