from json import load, dump
from tkinter import Button

from PIL import ImageTk
from PIL import Image
from canvas import frame, root

from helpers import clean_screen


def display_products():
    clean_screen()
    display_stock()


def display_stock():
    global info
    with open("db/products_data.json", 'r') as stock:
        info = load(stock)

    x, y = 150, 50

    for item_name, item_info in info.items():
        item_img = ImageTk.PhotoImage(Image.open(item_info["image"]))
        images.append(item_img)
        frame.create_text(x, y, text=item_name, font=('Comic Sans MS', 15))
        frame.create_image(x, y + 100, image=item_img)

        if item_info["quantity"]:
            color = 'green'
            text = f"In stock: {item_info['quantity']}"

            item_btn = Button(
                root,
                text='Buy',
                font=("Comic Sans MS", 12),
                bg='green',
                fg='white',
                width=5,
                command=lambda func_name=item_name: buy_product(func_name)
            )

            frame.create_window(x, y + 240, window=item_btn)
        else:
            color='red'
            text='Out of stock'

        frame.create_text(x, y+200, text=text, font=('Comic Sans MS', 12), fill=color)
        x += 250

        if x > 550:
            x = 150
            y += 350


def buy_product(product):
    info[product]["quantity"] -= 1

    with open("db/products_data.json", 'w') as stock:
        dump(info, stock)

    display_products()


images = []
info = {}