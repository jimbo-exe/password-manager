from tkinter import *
import os
import database

hideables = []


def clear():
    global hideables
    if hideables:
        for i in hideables:
            i.destroy()

    hideables = []


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
    global add_entries
    global okay_button

    clear()

    def label_maker(text):
        return Label(root, text=text,
                     font="Helvetica 15 bold",
                     bg="#505050",
                     foreground="#118ab2")

    add_labels = [label_maker("Enter the platform:"),
                  label_maker("Enter the username:"),
                  label_maker("Enter the password:"),
                  label_maker("Confirm Password:")]
    columns = ("platform", "username", "password", "confirm")

    for i in range(4):
        add_labels[i].grid(row=i + 1, column=1)

    add_entries = [Entry(root) for i in range(4)]
    for i in range(4):
        add_entries[i].grid(row=i + 1, column=2)

    status_label = label_maker("Awaiting details...")
    status_label.grid(row=6, column=1, columnspan=2)

    def acquire():
        data = []
        for i in range(len(add_entries)):
            detail = add_entries[i].get()
            if detail.rstrip().lstrip() == "":
                status_label.configure(text=f"{columns[i]} is empty! Please fill it.")
                return None
            else:
                data.append(detail)

        if data[-1] != data[-2]:
            status_label.config(text="Confirm password doesn't match! Please reenter.")
            return None

        else:
            database.add(data[0], data[1], data[2])
            status_label.config(text="Record successfully added!")

    okay_button = Button(root, text="Add", fg="#118ab2", bg="#505050",
                         font="Helvetica 15 bold", command=acquire)
    okay_button.grid(row=5, column=1, columnspan=2)
    hideables.append(okay_button)
    hideables.append(status_label)
    hideables.extend(add_entries)
    hideables.extend(add_labels)


def retrieve_tab():
    clear()
    data = database.names()

    info_label = Label(root, text="Select which record you want to view:",
                       font="Helvetica 15 bold",
                       bg="#505050",
                       foreground="#118ab2")

    info_label.grid(row=1, column=1, columnspan=2)

    def command_maker(name):  # Returns function for the record buttons
        def cmd():
            clear()
            details = database.retrieve(name)
            platform_label = Label(root, text=details[0],
                                   font="Helvetica 15 bold",
                                   bg="#505050",
                                   foreground="#118ab2")
            username_label = Label(root, text=details[1],
                                   font="Helvetica 15 bold",
                                   bg="#505050",
                                   foreground="#118ab2")
            date_label = Label(root, text=details[0],
                               font="Helvetica 15 bold",
                               bg="#505050",
                               foreground="#118ab2")
            #tbc
        return cmd

    def button_maker(text):
        return Button(root, text=text, fg="#118ab2", bg="#505050",
                      height=2, width=15,
                      font="Helvetica 15 bold", command=command_maker)

    button_list = []
    for i in data:
        button_list.append(button_maker(i))

    for i in range(len(button_list)):
        button_list[i].grid(row=i // 2 + 2, column=i % 2 + 1)


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
        tabs[i].grid(row=2 * i + 1, column=0, sticky=W, rowspan=2)


def show_welcome():
    global welcome_label
    welcome_label = Label(root,
                          text="Welcome to Password Manager! Hope you having a great day!" +
                               "Choose a tab from the left to get started.",
                          font="Helvetica 15",
                          wraplength=500,
                          bg="#505050")

    welcome_label.grid(row=1, column=1, rowspan=3, columnspan=2)
    hideables.append(welcome_label)


if __name__ == "__main__":
    initiate()
    initiate_tabs()
    show_welcome()
    root.mainloop()
