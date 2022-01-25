from itertools import count
from typing import Counter
from cryptography.fernet import Fernet
import base64
from re import M
from turtle import bgcolor, down
from django.conf import settings
import instaloader
from instaloader import Profile, Post
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import time
from PIL import Image, ImageTk
import os
import threading

icon = """
    AAABAAEAICAAAAEAIACoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAABAAAMMOAADDDgAAAAAA
AAAAAAAAAAAAUMb5AGHE4gBSxPIgWcbwgGDI79Bny+/0bM3u+2/N7vtxze37c83s+3XN7Pt1zez7
dszs+3bK7Pt2yOv7dMTr+3C+6/tptuz7Ya3t+1ij7vtQmO/7S43w+0eD8PtHefD7SnHw9E9p8NBU
Y/CAW13wIT1f7QBmYPEAAAAAADi29gAOpP8BQbnxR0m978xQv+79VcLu/1rE7v9exe7/YcXu/2LF
7v9kxe7/ZsXu/2bF7/9mxe//ZsTv/2bD7/9lwO//Yrnv/1yu7/9Wou//T5Xv/0mH7/9Fe+//Qm/v
/0Fl8P9EXvD/SFjw/09T7/1YUO/NYkvuSJk39AFtSPAAOLDtADKv8Eg5su7lQLbt/0W57v9Juu7/
Tbzu/1C+7v9Sve//VL3v/1W97/9Wve//V7zw/1e78P9Xu/D/WLrw/1e38P9VsfD/Uabw/0yZ8P9H
jPD/Q37w/0Bw8P8+ZfD/Plvw/0BU8P9ETfD/Skfw/1RE8P9gQe/laz7xSWBB7QAop/EhLajuyzKq
7f84ru7/O7Hu/z6y7v9Bs+7/Q7Tu/0Oz7v9GtO//TLXv/0+27/9PtfD/ULTw/1Cz8P9QsvD/UK/w
/0+p8P9Mn/D/SZTw/0aI8P9CevD/O2rw/zhe8P86V/D/PlDw/0JK8P9JRfD/UUDw/1w88P9qOfHM
dTf0ISSe8IAnn+79K6Lu/y+m7v8yqO7/NKnu/zWq7v9DsO//eMbz/67d+P/I5/r/zOn7/8zp+//M
6Pv/zOj7/8zo+//M5/v/zOX7/8zj+//L4Pv/y937/8bW+v+rv/j/do/0/0Rd8f87TfD/Qknw/0hE
8P9RP/H/Wzvx/2k38f11NvOBH5Tw0CKV7/8lme//KJ3u/yqe7v8qn+7/VLPx/8Lk+v/6/f//////
///////////////////////////////////////////////////////////////////////6+///
xMz7/2Fu8/9AR/D/SUTw/1E/8f9cO/H/aDfy/3U089EaifHzHIvw/x+P8P8hk+//IZTu/0yp8f/Y
7fz//////+Ty/f+h0Pj/erv0/3W49P92tvT/drX0/3ez9P93sfT/eK/0/3ir9P94p/T/eKP0/3me
9P9/nvX/prj4/+bq/f//////3N/8/2Vp8/9IQvD/Uj/x/1078f9pN/L/djTz9Bd/8vwZgfH/HIXw
/x6I7/8qkO//utz6///////L4/v/T6Hx/yeL7v8mie7/KIfu/ymF7v8qgu7/K4Du/yx97/8see//
LXTv/y1u7/8uae//L2Pv/zBd7/80WO//W3Py/8/U+///////xsb6/1RK8f9UPfH/Xzrx/2s38v94
NPL9GHXy/Bp48f8de/D/HHzv/2Kl9P/4+/7/6fL9/1Ka8v8kfu7/Kn7u/yt97v8tfO//Lnrv/y94
7/8wde//MHHv/y9t7/8xae//M2bv/zRh7/81XO//N1fw/zhS8P83SvD/Y2zz/+vr/f/6+v//hHf1
/1Y58f9jOfH/bjbx/3oz8v0cbfL8H27x/yFw8P8gcvD/nMH4//////+syvn/KHXv/ylz7/8rce//
LHDv/y5v7/8ua+//NGzv/0t78f9gifP/YYbz/05z8f85XfD/NlXw/zlS8P87TvD/PUrw/z9F8f9C
QvH/t7X6//////+0p/n/XDfx/2c38f9yNfH/fTPx/SVk8PwmZfD/Jmbw/ylq8P+5z/r//////4ms
9/8lZfD/K2bw/y1k8P8vY/D/MGHw/1l/8/+vwvn/5ev9//b4/v/2+P7/5en9/7O8+f9hb/P/PUfx
/0BE8f9CQfH/RT7x/0Y48f+ckvf//////8zA+/9lOfH/bDXw/3Y08P+AM/D9MF3u/DBd7v8uXe//
MWHw/8HP+///////hqL3/ylZ8f8vWvH/MVjx/zJW8f9viPX/5On9///////6+v//6er9/+nq/f/6
+v///////+bn/f97efX/RTzy/0g68v9MOPL/TTLy/5yL+P//////0sT7/2w48f9xM/D/ezPv/4My
7/09Vur8Olbr/zdV7f84WO//w836//////+Knff/Lk/x/zRR8f80TvH/WWzz/+Ll/f//////0tT8
/36B9f9cXvL/XV3z/4F99f/U0fz//////+Xj/f9rW/T/TjTy/1I08v9UMPL/oYr4///////UxPv/
cTbx/3Yy7/9/Mu7/hzLt/UlR5fxGUOb/QlDp/0JS7P/Gy/r//////46Z9v82SPD/O0rw/z1J8P+r
sPn//////9bV/P9cXPL/Q0Hw/0hC8P9JQfH/SDzx/2NV8//X0/z//////7Wp+f9WNvL/WTPy/1ov
8v+kivj//////9XE+/92NfD/ejHu/4My7f+KMuz9V03e/FNM4P9OS+T/TU7o/8nJ+P//////k5b1
/z9D7v9DRO//VFPw/97e/P/+/v//ioT1/0c88P9MP/D/TT7w/08+8P9QPPH/Tzbx/5B+9v/+/v//
4tz9/2pF8/9eMfL/YC7y/6iJ9///////18P7/3o17/9+Me3/hjLs/40y6/1lStb8YEna/1pI3v9Z
S+L/zMj3//////+ZlPP/SUDr/0tA7P9qX/D/8O/+//Lx/v9sXvL/Tjrv/1A78P9SOvD/Uzrw/1U4
8f9VNfH/dFfz//Lw/v/y7v7/e1T0/2Mw8v9mLfH/q4n3///////Yw/v/fzXv/4Mx7f+KMev/kDLp
/XNHzvxuRtL/aEbX/2ZJ2//QyPX//////6CT8P9VPeb/Vj7o/3Bb7f/v7f3/9PP+/3Rf8f9TN+//
VTjv/1Y38P9XNvD/WTXw/1ky8P97WPP/9PL+//Ht/v9/UfP/aS/y/2wt8f+uiff//////9rD+v+E
Ne7/hzHs/44x6v+TMuj9gkXF/HxEyv91RM//c0fU/9TH8///////p5Lt/2E84P9iPeP/a0nn/97W
+v//////oIz0/1k07f9bNu//WzTv/1w07/9eM/D/XS/w/6OI9v//////4dX8/3g/8f9xMPD/ci3w
/7KJ9v//////28P6/4k17f+MMer/kjLn/5gy5f2QQ7z8iUPB/4NCx/+ARcz/2Mfw//////+ukun/
bTvZ/2493f9qOuD/tJvx///////n4fz/g2Dx/18x7f9fMO7/YC/u/2Ev7v+FXfL/6OD9//////+5
mPf/dDDv/3gx7/96Le7/tYn1///////dw/n/jzXr/5Iy6P+XMuX/nDPj/Z1BsvyWQbj/kEG+/41E
xP/cxu7//////7WR5P96OtL/eTzX/3U52/+CT+P/4NL4///////q4/z/rZH1/4xj8v+MY/L/rpD2
/+ri/f//////4dL7/4dH7/95Le3/fzHu/4Eu7f+5ifT//////9/D+f+VNun/lzLm/5wy4v+hM+D9
qD6o/KE/rv+bP7T/mEK7/9/G7P//////vJDg/4Y5yv+FO9D/gTnV/3w22v+UXeT/4ND4//7+////
////+vj+//r4/v///////v7//+HP+v+WWO//ikPt/5pZ8P+LN+z/iC3r/76J8///////4cT4/5w2
5v+eMuL/ozPe/6g02/2xPJ78qzyl/6U9q/+iP7H/4MDm///////Gl93/kjjB/5E6x/+NOMz/ijfR
/4U01v+QSN7/vJDs/+DM9v/v4/v/7+T7/+HM+P+9kPD/kEXo/49A6P/eyPn/+PT+/8KO8v+RLub/
xpHx///////hvvX/ozbf/6c02/+sNdf/sTXU/bk6lPy0Opr/rzuh/6o5pv/XpNf//////9++5/+i
Pbj/nTm7/5o4wP+XN8b/lDbK/5A0z/+NMtP/kjzY/5lJ3P+aSd7/kzzd/48x3P+QMN3/o1Hi//Tp
+///////2bHy/6A33//euvT//////9ei7f+qM9f/sDXU/7Q20P+5Nsz9wTmI/Lw5j/+4Opb/szea
/8dvuf/89/v/+fL6/8NyxP+pNqz/pziz/6U4uP+iN7z/oDfB/542xf+cNcj/mzTL/5s0zf+cNc//
njXQ/5810f+iONP/xYDi/9qp6/+2V9r/wG3h//ny/P/89/3/x27d/7Q0zv+5N8v/vjfH/8M4w/3J
OH38xDiE/8E5iv+9OJD/vUCY/+i72///////8+Hx/8t1v/+2P6j/sTeo/681rf+tNbH/qzW1/6o0
uP+pNLv/qTS+/6o0wP+qNcL/qzXE/6w1xf+tM8b/sTzJ/8dy2v/z4Pf//////+i86/++P8j/vzfD
/8M5wP/HOb3/zDm6/dI4cfPNOHj/yTh+/8c5hP/EN4f/zFec//PU5f//////+/T5/+vG4//fpNT/
3J/T/9ye1f/bntb/257Y/9qe2v/antv/257c/9ue3f/bnt7/25/f/96k4f/qxu3/+/T8///////y
1fD/zFjF/8U3uf/IObj/yzm2/885s//UObH02zpk0NY6av/SOnH/zzp3/806e//LOH3/01iT/+66
0v/99vn/////////////////////////////////////////////////////////////////////
///////99vv/7bvh/9JXuf/LOK3/zTqu/886rP/SOav/1jmp/9o5p9HlO1eA4Dtb/do7Y//YO2n/
1jxt/9Q8cP/TO3H/1UN4/99vmP/qobz/8LzP//HB1P/xwdX/8MHW//DB2P/wwdn/8MDa//DA2//w
wNv/8MDc//DA3P/vu9r/6aHN/95utf/TQaH/0jme/9Q6n//VOqD/1zqg/9k5n//bOZ393zmegu8+
SiHqPkzM5D1T/+E9Wv/ePl7/3T5h/9w/Y//cP2T/2j1l/9o9af/ZQW7/2UJy/9hCdv/XQnn/1kF9
/9VBgf/VQYT/1UCG/9ZAiP/WQIn/10CL/9g+jP/YOov/2TmM/9o7jv/aO5D/2zuR/9w7kv/dOpP/
3jqT/+A5k83kOpci60NAAPFDPkntQkLl6UBJ/+ZAT//lQVL/40JT/+NCVf/jQ1f/4kNZ/+FDW//g
Q17/30Nh/99DZP/eQmj/3UJs/91Cbv/dQXH/3kFz/95Adf/fQHf/3z96/+A+fP/gPn7/4D2A/+A9
g//gPIX/4DuH/+A7iP/hO4nm4zuLSuA7hwD4TTAA/1wgAfNJNUnwRznN7UY9/etFQf/qRkP/6UdE
/+lHRf/pR0f/6EdJ/+dHS//nR03/5kdP/+ZHUf/lR1T/5UZX/+VGWf/lRV3/5URg/+ZDZP/mQmj/
5kFs/+VAcf/jQHX/5D54/+Q+ev/jPXz95D1/zuU9gkn4PpMB6j2GAAAAAAD9VSYA4j1EAPZOLyHz
TDKC8Usz0vBLNPXuSzT970s1/e5LNv3uSzb97ks3/e1LOP3tSzn97Us6/e1LO/3tSz397EpA/exJ
Rf3sSEz960dS/epFWf3pRGD96ENm/edCa/3nQW/150Bz0uc/d4LoP3si2T1yAO5AfAAAAAAA4AAA
B4AAAAGAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACA
AAABgAAAAeAAAAc=
    """
icondata= base64.b64decode(icon)
global tempFile 
tempFile= "icon.ico"
iconfile= open(tempFile,"wb")
iconfile.write(icondata)
iconfile.close()

instance = instaloader.Instaloader()
root = Tk()
root.iconbitmap("icon.ico")
root.title("Instagram Crawler")
root.geometry('280x350+1000+300')
root.configure(background="#FFFFFF")
root.iconbitmap(tempFile)

    

def open():
    Cou = 1
    #setting.iconbitmap("icon.ico")
    if Cou < 2:
        Cou = Cou + 1
        setting = tk.Toplevel()
        setting.title("Settings")
        setting.geometry('280x350+1000+300')
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
    disp_tf.config(state=NORMAL)
    disp_tf.delete(0, END)
    disp_tf.insert(END, "Downloading profile: "+profile_id.get()+"\n")
    instance.download_profile(profile_name=profile_id.get())
    disp_tf.delete(0, END)
    disp_tf.insert(END, "Finished Downloading @"+profile_id.get()+"\n")
    disp_tf.config(state=DISABLED)
    

def step():
    for i in range(5):
        root.update_idletasks()
        my_progress['value'] += 20
        disp_tf.insert(END, "Profile "+profile_id.get()+" fetched"+"\n")
        time.sleep(1)

def stop():
    time.sleep(1)
    my_progress.stop()

def coun():
    global Cou
    Cou += 1

nb_of_columns = 4
button_setting = tk.Button(root, text="Setting",anchor=NW,highlightthickness=3,relief=SUNKEN,bd=1, command=lambda: [open()])
button_setting.configure(background="#FFFFFF")
button_setting.grid(row=0, column=0, sticky='ew', columnspan=nb_of_columns)

l3 = Label(root, text = "@")
l3.grid(row = 2, column = 0)
l3.config(background= "#FFFFFF")
l3.config(font=("Constantia",16, "bold italic"))

profile_id = tk.Entry(root,highlightbackground="black",highlightthickness=3)
profile_id.grid(row = 2, column = 1, pady =25)
profile_id.config(background= "#FFFFFF")
profile_id.config(font=("Helvetica", 12))

button_2 = tk.Button(root,relief=GROOVE , bd=1, highlightbackground="black", highlightthickness=1, text="Get",command=lambda: [stop(),threading.Thread(target=download).start(), step()])
button_2.config(background= "#ffffff", height=1, width=8)
button_2.grid(row=3, column=1, pady=2, padx=2)
button_2.config(font=("Helvetica", 14), background="#ffffff")

disp_tf = tk.Entry(root, relief=SUNKEN, bd=1, highlightbackground="black", highlightthickness=1)
disp_tf.grid(row = 4, column = 1, pady = 10,ipady=50, ipadx=40)
disp_tf.config(background= "#ffffff", width=20, justify=CENTER, state=DISABLED)
disp_tf.delete(0, END)

l4 = Label(root, text = "Status :")
l4.grid(row = 5, column = 0, sticky = W, pady = 2)
l4.config(background= "white")

my_progress = ttk.Progressbar(root, orient="horizontal", length=180, mode="determinate")
my_progress.grid(row=5, column=1, pady=30)
my_progress.config()

l5 = Label(root, text = "")
l5.grid(row = 2, column = 3, padx=15, pady = 0)
l5.config(background= "#FFFFFF")
os.remove(tempFile)
mainloop()

root.mainloop()

