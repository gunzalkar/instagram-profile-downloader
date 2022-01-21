import profile
import instaloader
from instaloader import Profile, Post
from tkinter import *
from tkinter.ttk import *
import time

instance = instaloader.Instaloader()
root = Tk()
root.title("Instagram Profile Downloader")
root.geometry('400x250+1000+300')
root.configure(background="white")

def download():
	instance.download_profile(profile_name=profile_id.get())

def login():
	instance.login(user=username.get(),passwd=passcode.get())

def step():
    for i in range(5):
        root.update_idletasks()
        pb1['value'] += 20
        time.sleep(0.5)
        
l1 = Label(root, text = "username:")
l2 = Label(root, text = "password:")
l3 = Label(root, text = "Scraping ID:")

l1.grid(row = 0, column = 0, sticky = W, pady = 2)
l2.grid(row = 1, column = 0, sticky = W, pady = 2)
l3.grid(row = 2, column = 0, sticky = W, pady = 2)

username = Entry(root)
passcode = Entry(root)
profile_id = Entry(root)

username.grid(row = 0, column = 1, pady = 2)
passcode.grid(row = 1, column = 1, pady = 2)
profile_id.grid(row = 2, column = 1, pady = 2)

button_1 = Button(root, text="Login", command=login)
button_1.grid(row=3, column=1)

button_2 = Button(root, text="Download", command=lambda: [download(), step()])
button_2.grid(row=3, column=2)



pb1 = Progressbar(root, orient=HORIZONTAL, length=100, mode='indeterminate')
pb1.grid(row=4, column=1)


mainloop()
pb1.mainloop()