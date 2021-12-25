import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import _datetime
# Minecraft Hours

root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=720)
canvas.grid(columnspan=9, rowspan=16)

error_text = tk.StringVar()
error = tk.Label(root, textvariable=error_text, font='Minecraft')
error_text.set("")


def date_collector(event):
    birth_date_entry = Entry.get()
    try:
        error_text.set("")
        birth_date = birth_date_entry.split('/')
        date = int(birth_date[0])
        month = int(birth_date[1])
        year = int(birth_date[2])
        birthday = _datetime.date(year, month, date)
        today = _datetime.date.today()
        human_days = today - birthday
        minecraft_hours = human_days.total_seconds() / 50
        if minecraft_hours:
            error.grid_remove()
            text_box = tk.Text(root, height=10, width=50, padx=15, pady=15, wrap='word')
            text_box.insert(1.0, f"You've been alive for {minecraft_hours:,} Minecraft hours!\n")
            text_box.tag_configure("justified", justify="right")
            text_box.configure(font='Minecraft')
            text_box.grid(column=3, row=5)
            text_box.insert(2.0, f"\nThat's a total of {(minecraft_hours/8760):,} ({round(minecraft_hours/8760, 1)}) "
                                 f"Minecraft years!")

            age_text.set("GO AGAIN!")
            error_text.set("")
    except IndexError:
        error_text.set("Please enter correct value!")
        error.grid(column=3, row=4)
    except ValueError:
        error_text.set("Please enter correct value!")
        error.grid(column=3, row=4)
    return None

# Logo


logo = Image.open('Minecraft Logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=3, row=0)

# Basic Instructions
instructions = tk.Label(root, text="Please enter your age\n (dd/mm/yy)", font='Minecraft')
instructions.grid(column=3, row=1)

# Age Entering
Entry = tk.Entry(root)
Entry.grid(column=3, row=2)


# Button
age_text = tk.StringVar()
FindAgeButton = Button(root, textvariable=age_text, bg="#F08080", height=2, width=20)
FindAgeButton.bind('<Button-1>', date_collector)
age_text.set("FIND YOUR AGE!")
FindAgeButton.grid(column=3, row=3)

root.mainloop()
