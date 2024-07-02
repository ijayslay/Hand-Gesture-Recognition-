import os
import subprocess
import tkinter as tk
import tkinter.font as font
import tkinter.ttk as ttk
from tkinter import font as tkfont



root = tk.Tk()
root.geometry('1100x720')
root.configure(bg='#222')

# define font styles
h1_font = font.Font(family='Comic Sans MS', size=30, weight='bold')
h2_font = font.Font(family='Comic Sans MS', size=20, weight='bold')
p_font = font.Font(family='Comic Sans MS', size=16)

# define style for buttons
style = ttk.Style()
style.configure('Custom.TButton', padding=10, border=1, relief='raised',
                background='#222', foreground='#fff', font=p_font)
style.map('Custom.TButton', background=[('active', '#fff')], foreground=[('active', '#333')])


# define section frame style
section_style = ttk.Style()
section_style.configure('Custom.TFrame', padding=50, border=1, relief='solid',
                        background='#F8F8FF', width=550, height=400)


# define header
header_frame = tk.Frame(root, bg='#222', height=100)
header_frame.pack(side='top', fill='x')
header_label = tk.Label(header_frame, text='Hand Gesture Recognition', font=h1_font, bg='#222', fg='#fff')
header_label.pack()

title_font = tkfont.Font(family='Comic Sans MS', size=30, weight="bold")
text_font = tkfont.Font(family='Comic Sans MS', size=18)

section_frame1 = tk.Frame(root, width=600, height=600, bg="#F8F8FF", highlightthickness=1, highlightbackground="#F8F8FF", padx=20, pady=20)
section_frame1.pack(side="left", padx=30, pady=30)

title_label1 = tk.Label(section_frame1, text="Text to Sign Converter", font=title_font, fg="#fff", bg="#333")
title_label1.pack(pady=(20, 30))

desc_label1 = tk.Label(section_frame1, text="A web tool that converts text to sign language,", font=text_font, fg="#fff", bg="#333", wraplength=500, justify="center")
desc_label1.pack(pady=(0, 30))

button1 = tk.Button(section_frame1, text="Get Started", font=text_font, fg="#fff", bg="#222", bd=1, relief="solid", padx=20, pady=10, cursor="hand2", command=lambda: subprocess.Popen('textToSign.exe'))
button1.pack()

section_frame2 = tk.Frame(root, width=600, height=600, bg="#333", highlightthickness=1, highlightbackground="#fff", padx=20, pady=20)
section_frame2.pack(side="left", padx=30, pady=30)

title_label2 = tk.Label(section_frame2, text="Sign to Text Converter", font=title_font, fg="#fff", bg="#333")
title_label2.pack(pady=(20, 30))

desc_label2 = tk.Label(section_frame2, text="A web tool that converts hand gestures of sign language into text", font=text_font, fg="#fff", bg="#333", wraplength=500, justify="center")
desc_label2.pack(pady=(0, 30))

button2 = tk.Button(section_frame2, text="Get Started", font=text_font, fg="#fff", bg="#222", bd=1, relief="solid", padx=20, pady=10, cursor="hand2", command=lambda: subprocess.Popen('handGestureRecognition.exe'))
button2.pack()

footer_frame = tk.Frame(root, bg="#333")
footer_frame.pack(side="bottom", fill="x")

root.mainloop()
