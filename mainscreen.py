from tkinter import *
import os
import gpass as g
import spass as s

# hideables = []


def initiate():
    global root, heading_label
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


def add_tab():
    global add_labels
    global add_entrys
    global okay_button

    def label_maker(text):
        return Label(root, text=text,
                     font="Helvetica 15 bold",
                     bg="#505050",
                     foreground="#118ab2")

    add_labels = [label_maker("Enter the platform:"),
                  label_maker("Enter the username:"),
                  label_maker("Enter the password:"),
                  label_maker("Confirm Password:")]

    for i in range(4):
        add_labels[i].grid(row=i + 1, column=1)

    add_entrys = [Entry(root) for i in range(4)]
    for i in range(4):
        add_entrys[i].grid(row=i + 1, column=2)


def retrieve_tab():
    pass


def edit_tab():
    pass


def initiate_tabs():
    def tab_button(text, func):
        return Button(root,
                      height=3,
                      width=22,
                      text=text,
                      font="Helvetica 15 bold",
                      bg="#505050",
                      foreground="#118ab2",
                      command=func)

    tabs = [tab_button("Retrieve Records", retrieve_tab),
            tab_button("Add New Record", add_tab),
            tab_button("Edit Records", edit_tab)]

    for i in range(len(tabs)):
        tabs[i].grid(row=i+1, column=0, sticky=W)


def show_welcome():
    welcome_label = Label(root,
                          text="Welcome to Password Manager! Hope you having a great day!" +
                               "Choose a tab from the left to get started.",
                          font="Helvetica 15",
                          wraplength=500,
                          bg="#505050")

    welcome_label.grid(row=1, column=1, rowspan=3, columnspan=2)

    root.mainloop()


if __name__ == "__main__":
    initiate()
    initiate_tabs()
    add_tab()
    root.mainloop()
