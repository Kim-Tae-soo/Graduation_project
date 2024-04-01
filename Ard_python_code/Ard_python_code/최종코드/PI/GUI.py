from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from collections import deque

import serial
import time

from PythonHub import PythonHub

class MyApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("ATP Mouse")
        self.geometry("1280x1080")
        self.attributes('-fullscreen', False)
        self.bind("<F11>", lambda event: self.attributes("-fullscreen", not self.attributes("-fullscreen")))

        try:
            self.ph = PythonHub()
        except serial.serialutil.SerialException as e:
            error_message = f"장치가 연결되지 않거나 연결에 문제가 있습니다.\n {e}"
            messagebox.showerror("오류", error_message)
            self.destroy()

        # 이미지 크기를 조절하여 불러오기
        logo_path = "logo.png"
        logo_image = Image.open(logo_path)
        logo_image = logo_image.resize((640, 480))
        self.logo_image = ImageTk.PhotoImage(logo_image)

        self.login_frame = LoginFrame(self)
        self.main_frame = MainFrame(self)

        self.show_frame("login")

    def show_frame(self, frame_name):
        if frame_name == "login":
            self.login_frame.grid(row=0, column=0, sticky="nsew")
            self.main_frame.grid_forget()
        elif frame_name == "main":
            self.login_frame.grid_forget()
            self.main_frame.grid(row=0, column=0, sticky="nsew")
            
    def check_login(self, e_mail, password):
        logon, message = self.ph.login(e_mail, password)

        if not logon:
            error_message = f"로그인 실패\n {message}"
            messagebox.showerror("오류", error_message)
        else:
            self.show_frame("main")

class LoginFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.configure(bg='#bdbebd')

        self.logo_label = Label(self, image=master.logo_image)
        self.logo_label.grid(row=0, column=0, columnspan=3, pady=100)

        fontStyle = tkFont.Font(family="Arial", size=48)

        id_label = Label(self, text="E-mail", font=fontStyle)
        pw_label = Label(self, text="Password", font=fontStyle)
        id_entry = Entry(self, bd=3, font=fontStyle)
        pw_entry = Entry(self, bd=3, show='*', font=fontStyle)
        login_btn = Button(self, text="Login", command=lambda: master.check_login(id_entry.get(), pw_entry.get()), font=fontStyle)

        id_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        pw_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        id_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="w")
        pw_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="w")
        login_btn.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

    def show_logo(self):
        self.logo_label.grid(row=0, column=0, padx=10, pady=100)

class MainFrame(Frame):
    run, cool, hot, pet, auto = False, False, False, False, False
    graph, temp, bpm = 0.0, 0.0, 0
    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.configure(bg='#bdbebd')

        self.scan()

        self.scanBtnText = StringVar()
        self.scanBtnText.set("측정 시작")
        
        self.autoBtnText = StringVar()
        self.autoBtnText.set("자동 조정")

        self.coolBtnText = StringVar()
        self.coolBtnText.set("냉풍 OFF")

        self.hotBtnText = StringVar()
        self.hotBtnText.set("온풍 OFF")

        self.petBtnText = StringVar()
        self.petBtnText.set("PET OFF")

        self.messege_label = Label(self, text="Main Frame", font=("Arial", 12))
        self.messege_label.grid(row=0, column=0, padx=10, pady=10)

        self.scanBtn = Button(self, textvariable = self.scanBtnText, command = lambda:self.scanPower)
        self.scanBtn.grid(row=0, column=1, padx=10, pady=10)

        self.autoBtn = Button(self, textvariable = self.autoBtnText, command = lambda:self.autoPower)
        self.autoBtn.grid(row=0, column=2, padx=10, pady=10)

        self.coolBtn = Button(self, textvariable = self.coolBtnText, command = lambda:self.push("cool"))
        self.coolBtn.grid(row=1, column=0, padx=10, pady=10)

        self.hotBtn = Button(self, textvariable = self.hotBtnText, command = lambda:self.push("hot"))
        self.hotBtn.grid(row=1, column=1, padx=10, pady=10)

        self.petBtn = Button(self, textvariable = self.petBtnText, command = lambda:self.push("pet"))
        self.petBtn.grid(row=1, column=2, padx=10, pady=10)

    def scan(self):
        if self.run:
            graph, temp, bpm = self.master.ph.sendData()
            if self.auto: self.autoTemp

        self.after(25, self.scan)  # 10 밀리초마다 scan을 호출

    def push(self, btn):
        self.run = False

        message = self.master.ph.talkListen("push " + btn)
        
        if btn == "cool":
            if self.cool:
                self.cool = False
                self.coolBtnText.set("냉풍 OFF")
            else:
                self.cool = True
                self.coolBtnText.set("냉풍 ON")
                
        elif btn == "hot":
            if self.hot:
                self.hot = False
                self.hotBtnText.set("온풍 OFF")
            else:
                self.hot = True
                self.hotBtnText.set("온풍 ON")

        elif btn == "pet":
            if self.pet:
                self.pet = False
                self.petBtnText.set("PET OFF")
            else:
                self.pet = True
                self.petBtnText.set("PET ON")

        self.run = True

        print(message)
            
    def autoTemp(self):
        if temp > 40:
            self.push("cool")
            if not pet:
                self.push("pet")
            
        elif temp < 20:
            self.push("hot")
            if not pet:
                self.push("pet")

    def autoPower(self):
        if self.auto:
            self.auto = False
            self.autoBtnText.set("조정 OFF")
        else:
            self.auto = True
            self.autoBtnText.set("조정 ON")

    def scanPower(self):
        if self.run:
            self.run = False
            self.scanBtnText.set("측정 ON")
        else:
            self.run = True
            self.scanBtnText.set("측정 OFF")
    
if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
