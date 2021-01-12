from tkinter import *
import os
import database
import spass
import gpass

hideables = []


def clear():
    global hideables
    if hideables:
        for i in hideables:
            i.destroy()

    hideables = []


def initiate():
    global root, heading_label
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


def label_maker(text):  # Utility function for the functions below
    return Label(root, text=text,
                 font="Helvetica 15 bold",
                 bg="#505050",
                 foreground="#118ab2")


def add_tab():
    global add_labels
    global add_entries
    global okay_button

    clear()

    add_labels = [label_maker("Enter the platform:"),
                  label_maker("Enter the username:"),
                  label_maker("Enter the password:"),
                  label_maker("Confirm Password:"),
                  label_maker("Enter Global Password: ")]

    columns = ("platform", "username", "password", "confirm")

    for i in range(len(add_labels)):
        add_labels[i].grid(row=i + 1, column=1)

    add_entries = [Entry(root) for i in range(len(add_labels))]
    for i in range(len(add_labels)):
        add_entries[i].grid(row=i + 1, column=2)

    status_label = Label(root, text="Awaiting Details...",
                         font="Helvetica 15 bold",
                         bg="#505050",
                         foreground="#ff3838")
    status_label.grid(row=7, column=1, columnspan=2)

    def acquire():
        data = []
        for i in range(len(add_entries)):
            detail = add_entries[i].get()
            if detail.rstrip().lstrip() == "":
                status_label.configure(text=f"{columns[i]} is empty! Please fill it.")
                return None
            else:
                data.append(detail)

        if data[2] != data[3]:
            status_label.config(text="Confirm password doesn't match! Please reenter.")
            return None

        else:
            attempt = data[-1]
            if gpass.checkgpass(attempt):
                database.add(data[0], data[1],
                             spass.encrypt_spass(data[2].encode("utf-8"), spass.get_key(attempt)))
                status_label.config(text="Record successfully added!")
            else:
                status_label.config(text="Global password incorrect... Please reenter")

    okay_button = Button(root, text="Add", fg="#118ab2", bg="#505050",
                         font="Helvetica 15 bold", command=acquire)
    okay_button.grid(row=6, column=1, columnspan=2)
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
    hideables.append(info_label)

    def command_maker(name):  # Returns function for the record buttons
        def cmd():
            clear()
            details = database.retrieve(name)
            platform_label = Label(root, text="Platform: " + details[0],
                                   font="Helvetica 15 bold",
                                   bg="#505050",
                                   foreground="#118ab2")
            username_label = Label(root, text="Username: " + details[1],
                                   font="Helvetica 15 bold",
                                   bg="#505050",
                                   foreground="#118ab2")
            date_label = Label(root, text="Last Edited: " + details[3],
                               font="Helvetica 15 bold",
                               bg="#505050",
                               foreground="#118ab2")
            platform_label.grid(row=1, column=1, columnspan=2)
            username_label.grid(row=2, column=1, columnspan=2)
            date_label.grid(row=3, column=1, columnspan=2)
            hideables.extend([platform_label, username_label, date_label])

            status_label = Label(root, text="Click Below to Get password: ",
                                 font="Helvetica 15 bold",
                                 bg="#505050",
                                 foreground="#ff3838")
            hideables.append(status_label)

            def decrypt():
                attempt_label = Label(root,
                                      text="Enter the global password:",
                                      font="Helvetica 15 bold",
                                      bg="#505050",
                                      foreground="#118ab2")

                attempt_entry = Entry()
                attempt_label.grid(row=6, column=1)
                attempt_entry.grid(row=6, column=2)
                hideables.extend([attempt_entry, attempt_label])

                def get_attempt():
                    attempt = attempt_entry.get()

                    if gpass.checkgpass(attempt):
                        password = spass.decrypt_spass(database.retrieve(name)[2],
                                                       spass.get_key(attempt))
                        password_label = Label(root,
                                               text=b"Password: " + password,
                                               font="Helvetica 15 bold",
                                               bg="#505050",
                                               foreground="#118ab2")
                        password_label.grid(row=8, column=1, columnspan=2)
                        hideables.append(password_label)
                        status_label.configure(text="Password Obtained! Copy and enter where required.")

                        def copy():
                            root.clipboard_clear()
                            root.clipboard_append(password)

                        copy_button = Button(root, text="Copy", fg="#118ab2", bg="#505050",
                                             height=1, width=9,
                                             font="Helvetica 15 bold", command=copy)
                        copy_button.grid(row=7, column=2)
                        hideables.append(copy_button)
                    else:
                        status_label.configure(text="Wrong password! Please Reenter.")

                attempt_okay = Button(root, text="Enter", fg="#118ab2", bg="#505050",
                                      height=1, width=9,
                                      font="Helvetica 15 bold", command=get_attempt)
                attempt_okay.grid(row=7, column=1)
                hideables.append(attempt_okay)

            decrypt_button = Button(root, text="Decrypt", fg="#118ab2", bg="#505050",
                                    height=1, width=9,
                                    font="Helvetica 15 bold", command=decrypt)

            status_label.grid(row=4, column=1, columnspan=2)
            decrypt_button.grid(row=5, column=1, columnspan=2)
            hideables.append(decrypt_button)

            back_button = Button(root, text="<-- Back", fg="#118ab2", bg="#505050",
                                 height=1, width=7,
                                 font="Helvetica 7 bold", command=retrieve_tab)
            back_button.grid(row=9, column=1)
            hideables.append(back_button)

        return cmd

    def button_maker(name):
        return Button(root, text=name, fg="#118ab2", bg="#505050",
                      height=2, width=15,
                      font="Helvetica 15 bold", command=command_maker(name))

    button_list = []
    for i in data:
        button_list.append(button_maker(i))

    for i in range(len(button_list)):
        button_list[i].grid(row=i // 2 + 2, column=i % 2 + 1)

    hideables.extend(button_list)


def edit_tab():
    clear()
    data = database.names()

    info_label = Label(root, text="Select which record to edit: ",
                       font="Helvetica 15 bold",
                       bg="#505050",
                       foreground="#ff3838")

    info_label.grid(row=1, column=1, columnspan=2)
    hideables.append(info_label)

    def command_maker(name):
        def cmd():
            clear()
            status_label = Label(root,
                                 text="Enter new details. Leave empty if not to be changed.",
                                 font="Helvetica 12 bold",
                                 bg="#505050",
                                 foreground="#ff3838")
            status_label.grid(row=4, column=1, columnspan=2)
            hideables.append(status_label)

            edit_labels = [label_maker("Platform: "),
                           label_maker("Username: "),
                           label_maker("Password: ")]

            for i in range(len(edit_labels)):
                edit_labels[i].grid(row=i + 1, column=1)

            edit_entries = [Entry(root), Entry(root), Entry(root)]
            for i in range(len(edit_entries)):
                edit_entries[i].grid(row=i + 1, column=2)

            hideables.extend(edit_entries)
            hideables.extend(edit_labels)

            def acquire():
                edited = False
                details = []
                for i in edit_entries:
                    details.append(i.get())

                for i in details:
                    if i.rstrip().lstrip() != "":
                        edited = True

                column_list = ["platform", "username", "passhash"]
                for i in range(2):
                    if details[i].rstrip().lstrip() != "":
                        database.edit(name, column_list[i], details[i])

                if details[2].lstrip().rstrip() != "":
                    attempt_label = label_maker("Enter global Password: ")
                    attempt_entry = Entry(root)
                    attempt_label.grid(row=6, column=1)
                    attempt_entry.grid(row=6, column=2)
                    hideables.append(attempt_entry)
                    hideables.append(attempt_label)

                    def get_attempt():
                        attempt = attempt_entry.get()
                        if gpass.checkgpass(attempt):
                            key = spass.get_key(attempt)
                            spasshash = spass.encrypt_spass(details[2].encode("utf-8"), key)
                            database.edit(name, column_list[2], spasshash)
                            edited = True
                        else:
                            status_label.configure(text="Wrong password! Please reenter.")

                    gpass_okay_button = Button(root, text="Confirm",
                                               fg="#118ab2", bg="#505050",
                                               height=1, width=9,
                                               font="Helvetica 15 bold", command=get_attempt)
                    gpass_okay_button.grid(row=7, column=1, columnspan=2)
                    hideables.append(gpass_okay_button)

                if edited:
                    status_label.configure(text="Record Edited! Go to retrieve to see changes")
                else:
                    status_label.configure(text="No details entered... ")

            okay_button = Button(root, text="Confirm", fg="#118ab2", bg="#505050",
                                 height=1, width=9,
                                 font="Helvetica 15 bold", command=acquire)
            okay_button.grid(row=5, column=1, columnspan=2)
            hideables.append(okay_button)

        return cmd

    def button_maker(name):
        return Button(root, text=name, fg="#118ab2", bg="#505050",
                      height=2, width=15,
                      font="Helvetica 15 bold", command=command_maker(name))

    button_list = []
    for i in data:
        button_list.append(button_maker(i))

    for i in range(len(button_list)):
        button_list[i].grid(row=i // 2 + 2, column=i % 2 + 1)
    hideables.extend(button_list)


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
    os.chdir("bin")
    initiate()
    initiate_tabs()
    show_welcome()
    root.mainloop()
