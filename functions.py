from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


def get_popup(event):
    pmenu.tk_popup(event.x_root, event.y_root)


def get_about_app():
    messagebox.showinfo("About the app", "Version 1.0\nMade in PMA")


def get_about_author():
    messagebox.showinfo("About the author", "Hladkiy Andriy")


def close():
    if messagebox.askyesno("Exit", "Do you realy want to exit?"):
        wn.destroy()


def get_new_file(event=None):
    wn.title("Untitled.txt")
    pole.delete(1.0, END)


def open_file(event=None):
    filename = filedialog.askopenfilename()
    pos = filename.rfind("/") + 1
    new_name = filename[pos:]
    pole.delete(1.0, END)
    file = open(filename, "r")
    content = file.read()
    pole.insert(1.0, content)
    file.close()
    wn.title(new_name)


def save_file(event=None):
    file_name = filedialog.asksaveasfilename()
    file = open(file_name + ".txt", "w")
    content = pole.get(1.0, END)
    file.write(content)
    file.close()


def get_cut(event=None):
    pole.event_generate("<<Cut>>")


def get_copy(event=None):
    pole.event_generate("<<Copy>>")


def get_paste(event=None):
    pole.event_generate("<<Paste>>")


def get_undo(event=None):
    pole.event_generate("<<Undo>>")


def get_redo(event=None):
    pole.event_generate("<<Redo>>")


# створюєм вікно
wn = Tk()
wn.geometry("400x400")
wn.title("Notepad")

# створюєм вернє меню
menubar = Menu()
wn.config(menu=menubar)

fmenu = Menu(menubar)

menubar.add_cascade(label="File", menu=fmenu)  # додаєм кнопку File в верхнє меню

# додаєм підпункти кнопки File
fmenu.add_command(label="New File", accelerator="Ctrl+N", command=get_new_file)
fmenu.add_command(label="Open", accelerator="Ctrl+O", command=open_file)
fmenu.add_command(label="Save", accelerator="Ctrl+S", command=save_file)
fmenu.add_command(label="Close", accelerator="Ctrl+W")

about_menu = Menu(menubar)
menubar.add_cascade(label="About", menu=about_menu)

about_menu.add_command(label="About the app", command=get_about_app)
about_menu.add_command(label="About author", command=get_about_author)

# загружаєм картінки для кнопок
new_file_image = PhotoImage(file="icons/newfile.gif")
open_find_image = PhotoImage(file="icons/open.gif")
save_find_image = PhotoImage(file="icons/save.gif")
undo_image = PhotoImage(file="icons/undo.gif")
redo_image = PhotoImage(file="icons/Redo.gif")

panel = Frame(wn)
panel.pack()

new_file_button = Button(panel, image=new_file_image, command=get_new_file)
new_file_button.grid(row=0, column=0)

open_file_image = Button(panel, image=open_find_image, command=open_file)
open_file_image.grid(row=0, column=1)

save_file_button = Button(panel, image=save_find_image, command=save_file)
save_file_button.grid(row=0, column=2)

undo_button = Button(panel, image=undo_image, command=get_undo)
undo_button.grid(row=0, column=3)

redo_button = Button(panel, image=redo_image, command=get_redo)
redo_button.grid(row=0, column=4)

# створюєм поле для вводу
pole = Text(wn, undo=True)
pole.pack()

# створюєм меню яке показується при натисканні правої кнопки
pmenu = Menu(pole)
pmenu.add_command(label="Cut", command=get_cut)
pmenu.add_command(label="Copy", command=get_copy)
pmenu.add_command(label="Paste", command=get_paste)

pole.bind("<Button-3>", get_popup)
wn.protocol("WM_DELETE_WINDOW", close)
pole.bind("Control-n", get_new_file)
pole.bind("Control-o", open_file)
pole.bind("Control-s", save_file)
