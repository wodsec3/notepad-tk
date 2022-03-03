from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os


def new():
    text.delete(1.0, END)
    
def new_window():
    os.system('start {}'.format(__file__))
    
def open_file():
    file_name=filedialog.askopenfilename()
    with open(file_name) as f:
        data=f.read()
        text.insert(INSERT, data)
        
def save_file():
    file=filedialog.asksaveasfilename()
    with open(file, "w") as f:
            f.write(text.get(1.0, END))
            
def save_as_file():
    save_name=filedialog.asksaveasfilename()
    with open(save_name, "w") as f:
        f.write(text.get(1.0, END))

def about_us():
    messagebox.showinfo("About us", "Writed By <<muhammad.shafiei>>")
    
def ver():
    messagebox.showinfo("Version 1.0", "Current Version Is 1.0\nnotepad")

window=Tk()
window.title("Notepad")


menu_bar=Menu(window)
file_menu=Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new)
file_menu.add_command(label="New Window", command=new_window)
file_menu.add_command(label="open...", command=open_file)
file_menu.add_command(label="save", command=save_file)
file_menu.add_command(label="save as...", command=save_as_file)
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu=Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about_us)
help_menu.add_command(label="Vesion", command=ver)
menu_bar.add_cascade(label="Help", menu=help_menu)

window.config(menu=menu_bar)


text=Text(window)
text.pack(fill="both", expand=True)


window.geometry("600x600")
window.mainloop()
