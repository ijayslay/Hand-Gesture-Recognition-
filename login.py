import tkinter as tk
import subprocess

def check_login():
    # get the input values from the Entry widgets
    username = username_entry.get()
    password = password_entry.get()

    # check if the input values match the expected values
    if username == "admin"   and password == "2402" :
        result_label.config(text="Login successful", fg="#4CAF50")
        open_main()
        root.destroy() # close the login window after successful login
    else:
        result_label.config(text="Login failed", fg="#030303")

def open_main():
    # replace 'main.py' with the name of your actual file
    subprocess.Popen(["python", "run2.py"])

# create the main window
root = tk.Tk()

def on_return(event):
    # print('return clicked')
    check_login()
root.bind('<Return>', on_return)

root.title("Developed By:Udayraj,Jay,Harsh")
root.geometry("500x300")  # set window size
root.resizable(False, False)
root.configure(bg="#EFEFEF")

# add a heading
heading_label = tk.Label(root, text="LOGIN PAGE", font=("Arial", 24), bg="#EFEFEF", fg="#333")
heading_label.place(relx=0.5, y=40, anchor="center")

# create the input widgets
username_label = tk.Label(root, text="Username", font=("Arial", 14), bg="#EFEFEF", fg="#333")
username_label.place(x=80, y=100)
username_entry = tk.Entry(root, font=("Arial", 14), width=20, bd=2)
username_entry.place(x=200, y=100)

password_label = tk.Label(root, text="Password", font=("Arial", 14), bg="#EFEFEF", fg="#333")
password_label.place(x=80, y=150)
password_entry = tk.Entry(root, show="*", font=("Arial", 14), width=20, bd=2)
password_entry.place(x=200, y=150)

# create the login button and result label
login_button = tk.Button(root, text="Login", font=("Arial", 14), command=check_login, bg="#4CAF50", fg="white", width=10, bd=2, padx=5, pady=5)
login_button.place(relx=0.5, y=220, anchor="center")

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#EFEFEF", fg="#333")
result_label.place(relx=0.5, y=260, anchor="center")

# start the main event loop
root.mainloop()
