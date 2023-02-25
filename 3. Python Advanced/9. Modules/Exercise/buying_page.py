from json import load

from PIL import ImageTk
from PIL import Image
from canvas import frame

from helpers import clean_screen


def display_products():
    clean_screen()
    display_stock()


def display_stock():
    with open("db/products_data.json", 'r') as stock:
        info = load(stock)

    x, y = 150, 50

    for item_name, item_info in info.items():
        item_img = ImageTk.PhotoImage(Image.open(item_info["image"]))
        images.append(item_img)
        frame.create_text(x, y, text=item_name, font=('Comic Sans MS', 15))
        frame.create_image(x, y + 100, image=item_img)


images = []