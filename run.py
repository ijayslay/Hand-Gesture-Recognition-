import subprocess
import tkinter as tk
import tkinter.font as font
from tkinter.tix import IMAGETEXT
import tkinter.ttk as ttk
from tkinter import Image, font as tkfont


root = tk.Tk()
root.geometry('1400x900')
root.configure(bg='#FFFFE4')

# define font styles
h1_font = font.Font(family='Monaco', size=45, weight='bold')
h2_font = font.Font(family='Monaco', size=20, weight='bold')
p_font = font.Font(family='Monaco', size=16)

# define style for buttons
style = ttk.Style()
style.configure('Custom.TButton', padding=10, border=1, relief='raised', background='#222', foreground='#fff', font=p_font)
style.map('Custom.TButton', background=[('active', '#fff')], foreground=[('active', '#FFFFE4')])


# define section frame style
section_style = ttk.Style()
section_style.configure('Custom.TFrame', padding=50, border=1, relief='solid',
                        background='#FFFFE4', width=550, height=400)

# define header
header_frame = tk.Frame(root, bg='#FFFFE4', height=100)
header_frame.pack(side='top', fill='x')
header_label = tk.Label(header_frame, text='Hand Gesture Recognition', font=h1_font, bg='#FFFFE4', fg='#000')
header_label.pack()

title_font = tkfont.Font(family='Monaco', size=30, weight="bold")
text_font = tkfont.Font(family='Monaco', size=18)

section_frame1 = tk.Frame(root, width=600, height=600, bg="#FFFFE4", highlightthickness=1, highlightbackground="#FFFFE4", padx=20, pady=20)
section_frame1.pack(side="left", padx=30, pady=30)

image = Image.open(r"C:\Final Module HGR\1.png")
print(image.size)
image = image.resize((200, 200))
print(image.size)
img = IMAGETEXT.PhotoImage(image)

title_label1 = tk.Label(section_frame1, image=img)
title_label1.pack(side = "top")

title_label1 = tk.Label(section_frame1, text="Text to Sign Converter", font=title_font, fg="#000", bg="#FFFFE4")
title_label1.pack(pady=(20, 30))

desc_label1 = tk.Label(section_frame1, text="A web tool that converts text to sign language", font=text_font, fg="#000", bg="#FFFFE4", wraplength=500, justify="center")
desc_label1.pack(pady=(0, 30))

button1 = tk.Button(section_frame1, text="Get Started", font=text_font, fg="#000", bg="#FFFFE4", bd=1, relief="solid", padx=20, pady=10, cursor="hand2", command=lambda: subprocess.Popen('textToSign.exe'))
button1.pack()

section_frame2 = tk.Frame(root, width=600, height=600, bg="#FFFFE4", highlightthickness=1, highlightbackground="#fff", padx=20, pady=20)
section_frame2.pack(side="right", padx=30, pady=30)

image = Image.open(r"C:\Users\91635\Downloads\Girl.png")
image = image.resize((200, 200))
img = ImageTk.PhotoImage(image)

title_label1 = tk.Label(section_frame2, image=img)
title_label1.pack(side = "top")

title_label2 = tk.Label(section_frame2, text="Hand Gesture Recognition", font=title_font, fg="#000", bg="#FFFFE4")
title_label2.pack(pady=(20, 30))

desc_label2 = tk.Label(section_frame2, text="A web tool that converts hand gestures of sign language into text", font=text_font, fg="#000", bg="#FFFFE4", wraplength=500, justify="center")
desc_label2.pack(pady=(0, 30))

button2 = tk.Button(section_frame2, text="Get Started", font=text_font, fg="#000", bg="#FFFFE4", bd=1, relief="solid", padx=20, pady=10, cursor="hand2", command=lambda: subprocess.Popen('handGestureRecognition.exe'))
button2.pack()


footer_frame = tk.Frame(root, bg="#333")
footer_frame.pack(side="bottom", fill="x")

root.mainloop()
