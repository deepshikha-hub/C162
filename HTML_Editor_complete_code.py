from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import webbrowser
root = Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.configure(background="gray87")
open_img = ImageTk.PhotoImage(Image.open ("open_file.png"))
save_img = ImageTk.PhotoImage(Image.open ("save_file.png"))
run_img = ImageTk.PhotoImage(Image.open ("run.png"))
label_file_name = Label(root, text="File name")
label_file_name.place(relx=0.28,rely=0.03,anchor= CENTER)
input_file_name = Entry(root)
input_file_name.place(relx=0.46,rely=0.03, anchor= CENTER)
my_text= Text(root,height=35,width=80,bg = "slate gray", fg="white")
my_text.place(relx=0.5,rely=0.55,anchor= CENTER)
name = ""

open_button=Button(root,image=open_img,text="OpenFile", command=openFile)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)
save_button=Button(root, image=save_img,text="Save File", command=save)
save_button.place(relx=0.11,rely=0.03,anchor= CENTER)
run_button=Button(root,image=run_img,text="Exit File", command=run_html_file)
run_button.place(relx=0.17,rely=0.03,anchor= CENTER)
root.mainloop()