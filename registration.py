#import modules

from tkinter import *
import os
from sort_visualizer import main_window
import mysql.connector
import time
import datetime

# connecting to the database

connectiondb = mysql.connector.connect(
    host="localhost", user="root", passwd="admin", database="LoginDetail")
cursordb = connectiondb.cursor()

# Designing window for registration

main_screen = 0
register_screen = 0
username = 0
password = 0
username_entry = 0
password_entry = 0


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("360x250")
    register_screen.configure(bg="steelblue2")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", fg="blue4", bg="seagreen2").pack()
    Label(register_screen, text="",bg="steelblue2").pack()
    username_lable = Label(register_screen, text="Username", fg="blue4",bg="cyan2")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    Label(register_screen, text="",bg="steelblue2").pack()
    password_lable = Label(register_screen, text="Password", fg="blue4",bg="cyan2")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')#This makes password look *
    password_entry.pack()
    Label(register_screen, text="", fg="blue4",bg="steelblue2").pack()
    Button(register_screen, text="Register", width=10, height=1, fg="blue4", bg="seagreen2", command = register_user).pack()


# Designing window for login

login_screen = 0
username_verify = 0
password_verify = 0
username_login_entry = 0
password_login_entry = 0

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("360x250")
    login_screen.configure(bg="steelblue2")
    Label(login_screen, text="Please enter details below to login", fg="blue4", bg="seagreen2").pack()
    Label(login_screen, text="",bg="steelblue2").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username", fg="blue4", bg="cyan2").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="",bg="steelblue2").pack()
    Label(login_screen, text="Password", fg="blue4", bg="cyan2").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="",bg="steelblue2").pack()
    Button(login_screen, text="Login", width=10, height=1,bg="seagreen2", fg="blue4", command = login_verify).pack()

# Implementing event on register button

def register_user():
    status = "Registered"
    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d  %H:%M:%S'))
    username_info = username.get()
    password_info = password.get()
    #sql = "insert into usertable(username,password,timestamp) values(?,?,?)"
    cursordb.execute("insert into usertable(username,password,status,date_time) values(%s,%s,%s,%s)", (username_info, password_info,status,date))
    connectiondb.commit();
    # connectiondb.close()
    print('User Added on ',date)
    Label(register_screen, text="Registration Successful",
          fg="green", font=("calibri", 11)).pack()

# Implementing event on login button

def login_verify():
    status = "logged in"
    global login_screen
    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d  %H:%M:%S'))
    user_verification = username_verify.get()
    pass_verification = password_verify.get()
    sql = "select * from usertable where username = %s and password = %s"
    query = "insert into usertable(username,password,status,date_time) values(%s,%s,%s,%s)"
    cursordb.execute(sql, [(user_verification), (pass_verification)])
    results = cursordb.fetchall()
    if results:
        for i in results:
            print('Logged in Successfully on ', date)
            cursordb.execute(query, (user_verification, pass_verification,status,date))
            connectiondb.commit()
            login_sucess()
            break
    else:
        user_not_found()

# Designing popup for login success

login_success_screen = 0

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    login_success_screen.config(bg="steelblue2")
    Label(login_success_screen, text="Login Successful",fg="blue4").pack()
    Button(login_success_screen, text="OK",bg="seagreen2", fg="blue4", command=lambda:[delete_login_success(),main_screen.destroy(), main_window()]).pack()

# Designing popup for login invalid password

password_not_recog_screen = 0

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Try Again")
    password_not_recog_screen.geometry("150x100")
    password_not_recog_screen.config(bg="steelblue2")
    Label(password_not_recog_screen, text="Invalid Password ", fg="blue4",bg="cyan2").pack()
    Button(password_not_recog_screen, text="OK",bg="seagreen2",  fg="blue4",command=delete_password_not_recognised).pack()

# Designing popup for user not found

user_not_found_screen = 0

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Try Again")
    user_not_found_screen.geometry("150x100")
    user_not_found_screen.config(bg="steelblue2")
    Label(user_not_found_screen, text="User Not Found", fg="blue4",bg="cyan2").pack()
    Button(user_not_found_screen, text="OK",bg="seagreen2", fg="blue4", command=delete_user_not_found_screen).pack()

# Deleting popups

def delete_login_success():
    login_success_screen.destroy()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

# Designing first window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.configure(bg="steelblue2")#background color
    main_screen.geometry("360x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="seagreen1", width="300", height="2", fg="blue4", font=("Calibri", 13)).pack()
    Label(text="",bg="steelblue2").pack()
    Button(text="Login", height="2", width="30",bg="cyan2", fg="blue4", command = login).pack()
    Label(text="",bg="steelblue2").pack()
    Button(text="Register", height="2", width="30",bg="cyan2", fg="blue4", command=register).pack()

    main_screen.mainloop()

main_account_screen()
