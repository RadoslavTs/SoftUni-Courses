from json import loads, dump
from tkinter import Button, Entry
from canvas import root, frame
from helpers import clean_screen
from buying_page import display_products

def render_entry():
    register_button = Button(
        root,
        text='Register',
        bg='blue',  # background color
        fg='white',  # font color
        borderwidth=0,
        width=20,
        height=3,
        command=register,
    )

    login_button = Button(
        root,
        text='Login',
        bg='green',  # background color
        fg='white',  # font color
        borderwidth=0,
        width=20,
        height=3,
        command=login_func
    )
    frame.create_window(400, 260, window=login_button)
    frame.create_window(400, 320, window=register_button)
    frame.create_text(400, 50, text='Welcome to the candy shop!', font=('Comic Sans MS', 30))
    frame.create_text(400, 90, text='The time is 4:20', font=('Comic Sans MS', 20))
    frame.create_text(400, 130, text='Have some fun!', font=('Comic Sans MS', 20))


def register():
    clean_screen()

    frame.create_text(100, 50, text='First name:')
    frame.create_text(100, 100, text='Last name:')
    frame.create_text(100, 150, text='Username:')
    frame.create_text(100, 200, text='Password')

    frame.create_window(200, 50, window=first_name_box)
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=username_box)
    frame.create_window(200, 200, window=password_box)

    registration_btn = Button(
        root,
        text='Register',
        bg='green',
        fg='white',
        command=registration,
    )

    frame.create_window(300, 250, window=registration_btn)
    frame.create_window(700, 50, window=main_menu_btn)


def registration():
    info_dict = {
        "first_name": first_name_box.get(),
        "last_name": last_name_box.get(),
        "username": username_box.get(),
        "password": password_box.get()
    }

    if check_registration(info_dict):
        with open('db/users_info.txt', 'a') as users_file:
            dump(info_dict, users_file)
            users_file.write('\n')
            display_products()


def check_registration(info):
    for el in info.values():
        if not el.strip():
            frame.create_text(
                300, 300, text='Information missing!', fill='red', tag='error'
            )
            return False

    frame.delete("error")

    info_data = get_users_data()

    for record in info_data:
        if record['username'] == info['username']:
            frame.create_text(300, 300, text='username taken!', fill='red', tag='error', )
            return False

    frame.delete("error")

    return True


def get_users_data():  # TODO - connect to database!
    info_data = []

    with open("db/users_info.txt", 'r') as users_file:
        for line in users_file:
            info_data.append(loads(line))

    return info_data


def login_func():
    clean_screen()

    frame.create_text(100, 50, text='username')
    frame.create_text(100, 100, text='password')

    frame.create_window(200, 50, window=username_box)
    frame.create_window(200, 100, window=password_box)
    login_btn = Button(
        root,
        text='Login',
        bg='blue',
        fg='white',
        command=logging,
    )

    frame.create_window(250, 150, window=login_btn)
    frame.create_window(700, 50, window=main_menu_btn)


def logging():
    if check_logging():
        frame.delete("error")
        display_products()
    else:
        frame.create_text(160, 200, text='Invalid username or password!', fill='red', tag='error')


def check_logging():
    info_data = get_users_data()  # TODO - hash the password!

    current_username = username_box.get()
    current_password = password_box.get()

    for i in range(len(info_data)):
        username = info_data[i]["username"]
        password = info_data[i]["password"]

        if username == current_username and password == current_password:
            return True

    return False


def back_to_main():
    clean_screen()
    render_entry()


main_menu_btn = Button(root, text='Back to main', bg='blue', fg='white', command=back_to_main,)
first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0, show='*')  # TODO - add show/hide functionality
