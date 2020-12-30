from tkinter import *
import os
import gpass as g
import spass as s


def show_welcome():
    global root
    global heading_label
    global tabs

    os.chdir("bin")
    root = Tk()
    root.title("Password Manager")
    root.geometry("800x500")
    root.configure(background="#505050")

    heading_label = Label(root,
                          text='Password Manager',
                          font="Arial 35 bold",
                          justify="center",
                          fg="orange",
                          bg="#505050")

    heading_label.grid(row=0, column=0, columnspan=3)

    def tab_button(text):
        return Button(root,
                      height=3,
                      width=22,
                      text=text,
                      font="Helvetica 15 bold",
                      bg="#505050",
                      foreground="#118ab2")

    tabs = [tab_button("Retrieve Records"),
            tab_button("Add New Record"),
            tab_button("Edit Records")]

    for i in range(len(tabs)):
        tabs[i].grid(row=i + 1, column=0, sticky=W)

    welcome_label = Label(root,
                          text="Welcome to Password Manager! Hope you having a great day!"+
                           "Choose a tab from the left to get started.",
                          font="Helvetica 15",
                          wraplength=500,
                          bg="#505050")

    welcome_label.grid(row=1, column=1, rowspan=3, columnspan=2)

    root.mainloop()


if __name__ == "__main__":
    show_welcome()
