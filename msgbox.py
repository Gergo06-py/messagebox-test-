from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Image")
root.iconbitmap("C:/Users/borbe/Pictures/code.ico")

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askquestion("This is my Popup!", "Hello World!")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You clicked Yes").pack()
    elif response == 0:
        Label(root, text="You clicked No").pack()

Button(root, text="Popup", command=popup).pack()


root.mainloop()
