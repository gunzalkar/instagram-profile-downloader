from re import M
from turtle import bgcolor, down
import instaloader
from instaloader import Profile, Post
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import time
from PIL import Image, ImageTk

instance = instaloader.Instaloader()
root = Tk()
root.iconbitmap("C:/Users/gunja/Desktop/ig.ico")
root.title("Instagram Crawler")
root.geometry('260x350+1000+300')
root.configure(background="white")



def open():
    setting = tk.Toplevel()
    setting.title("Settings")
    setting.iconbitmap("C:/Users/gunja/Desktop/ig.ico")
    global username
    username = Entry(setting)
    passcode = Entry(setting)
    auth = Entry(setting)
    username.grid(row = 0, column = 1, pady = 2)
    passcode.grid(row = 1, column = 1, pady = 2)
    auth.grid(row = 2, column = 1, pady = 2)

    l1 = Label(setting, text = "username:")
    l2 = Label(setting, text = "password:")
    l9 = Label(setting, text = "2FA:")
    l1.grid(row = 0, column = 0, sticky = W, pady = 2)
    l2.grid(row = 1, column = 0, sticky = W, pady = 2)
    l9.grid(row = 2, column = 0, sticky = W, pady = 2)
    def login():
        instance.login(user=username.get(),passwd=passcode.get())
        time.sleep(2)
    def authe():
        instance.two_factor_login(auth.get())
    button_1 = Button(setting, text="Login",command=lambda: [login()])
    button_1.grid(row=3, column=1, pady=2, padx=2)
    button_9 = Button(setting, text="2FA",command=lambda: [authe(), setting.destroy()])
    button_9.grid(row=4, column=1, pady=2, padx=2)
    button_close = Button(setting, text="Close",command=lambda: [setting.destroy()])
    button_close.grid(row=5, column=1, pady=2, padx=2)


def download():
        instance.download_profile(profile_name=profile_id.get())

def step():
    for i in range(5):
        root.update_idletasks()
        my_progress['value'] += 20
        time.sleep(0.5)

def stop():
    time.sleep(1)
    my_progress.stop()

nb_of_columns = 4
button_setting = tk.Button(root, text="Setting",anchor=NW,highlightthickness=3,relief=SUNKEN,bd=1, command=lambda: [open()])
button_setting.configure(background="#f0f0f0")
button_setting.grid(row=0, column=0, sticky='ew', columnspan=nb_of_columns)


l3 = Label(root, text = "@")
l3.grid(row = 2, column = 0)
l3.config(background= "white")
l3.config(font=("Constantia",16, "bold italic"))

profile_id = tk.Entry(root,highlightbackground="black",highlightthickness=3)
profile_id.grid(row = 2, column = 1, pady =25)
profile_id.config(background= "white")
profile_id.config(font=("Constantia", 12))

button_2 = tk.Button(root,highlightbackground="black", text="Get",command=lambda: [download(), step()])
button_2.config(background= "#f0f0f0")
button_2.grid(row=3, column=1, pady=2, padx=2)
button_2.config(font=("Constantia", 14))

l4 = Label(root, text = "Status:")
l4.grid(row = 4, column = 0, sticky = W, pady = 2)
l4.config(background= "white")
l4.config(font=("Constantia", 10))

my_progress = ttk.Progressbar(root, orient="horizontal", length=180, mode="determinate")
my_progress.grid(row=4, column=1, pady=170)
my_progress.config()


l5 = Label(root, text = "")
l5.grid(row = 2, column = 3, padx=15, pady = 0)
l5.config(background= "white")
mainloop()
root.mainloop()
