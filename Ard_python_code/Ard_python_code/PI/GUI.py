from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
import serial
from PythonHub import PythonHub

try:
    ph = PythonHub()
except serial.serialutil.SerialException as e:
    error_message = f"장치가 연결되지 않거나 연결에 문제가 있습니다.\n {e}"
    messagebox.showerror("오류", error_message)
    raise SystemExit # 프로그램 종료


def checkLogin(e_mail, password):
    logon ,message = ph.login(e_mail.get(),password.get())

    if (logon == False):
        error_message = f"장치가 연결되지 않거나 연결에 문제가 있습니다.\n {e}"
        messagebox.showerror("오류", error_message)
    

def login(): # 로그인 화면
    root = Tk()
    root.title("ATP Mouse")

    root.geometry("1280x720")

    root.attributes('-fullscreen', True)
    root.bind("<F11>", lambda event: root.attributes("-fullscreen", not root.attributes("-fullscreen")))

    logoObj = PhotoImage(file = "logo.png")

    e_mail, password = StringVar(), StringVar()

    fontStyle = tkFont.Font(family = "Arial", size = 48)

    logo_label = Label(root, image = logoObj)
    logo_label.pack(padx = 10, pady = 100)

    login_label = Label(root, bg = '#bdbebd')
    login_label.pack(padx = 10, pady = 10)

    id_label = Label(login_label, bg = '#bdbebd', text = "E-mail",font = fontStyle).grid(row = 0, column = 0, padx = 10, pady = 10)
    pw_label = Label(login_label, bg = '#bdbebd', text = "Password",font = fontStyle).grid(row = 1, column = 0, padx = 10, pady = 10)
    id_entry = Entry(login_label, bd = 3, textvariable = e_mail, font = fontStyle).grid(row = 0, column = 1, padx = 10, pady = 10)
    pw_entry = Entry(login_label, bd = 3, textvariable = password, show='*', font = fontStyle).grid(row = 1, column = 1, padx = 10, pady = 10)
    login_btn = Button(login_label, bd = 3, text = "Login", command = lambda: ph.login(e_mail.get(),password.get()), font = fontStyle).grid(row = 2, column = 1, padx = 10, pady = 10)

    root.mainloop()

def main():
    main = Tk()
    main.title("ATP Mouse")

    main.geometry("1280x720")

    main.attributes('-fullscreen', True)
    main.bind("<F11>", lambda event: main.attributes("-fullscreen", not main.attributes("-fullscreen")))


login()
