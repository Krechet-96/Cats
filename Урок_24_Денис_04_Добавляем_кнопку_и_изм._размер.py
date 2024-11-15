from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

from pygame.display import update


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600,480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Произошла ошибка {e}")
        return None


def set_image():
    img = load_image(url)

    if img:
        label.config(image=img)
        label.image = img


window = Tk()
window.title("Cats!")
window.geometry("600x520")

label = Label()
label.pack()

update_button = Button(text="Обновить", command=set_image)
update_button.pack()

url = "https://cataas.com/cat"

set_image()

window.mainloop()
