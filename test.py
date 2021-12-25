import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

def func(event):
    print("You hit return.")
root.bind('<Return>', func)

root.mainloop()