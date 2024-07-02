import subprocess
import tkinter as tk
import tkinter.font as font
import tkinter.ttk as ttk
from tkinter import font as tkfont


root = tk.Tk()
root.geometry('1200x1000')
root.configure(bg='#9bd7d1')

# load images
text_to_sign_img = tk.PhotoImage(file='1.png').subsample(2, 2)
sign_to_text_img = tk.PhotoImage(file='2.png').subsample(2, 2)

# define font styles
h1_font = font.Font(family='Times', size=30, weight='bold')
h2_font = font.Font(family='Times', size=20, weight='bold')
p_font = font.Font(family='Times', size=16)

# define style for buttons
style = ttk.Style()
style.configure('Custom.TButton', padding=10, border=1, relief='raised',
                background='#222', foreground='#fff', font=p_font)
style.map('Custom.TButton', background=[('active', '#fff')], foreground=[('active', '#333')])


# define section frame style
section_style = ttk.Style()
section_style.configure('Custom.TFrame', padding=50, border=1, relief='solid',
                        background='#FFFFFF', width=550, height=400)


# define header-
header_frame = tk.Frame(root, bg='#9bd7d1', height=100)
header_frame.pack(side='top', fill='x')
header_label = tk.Label(header_frame, text='_______________________________________________________________________________________________________', font=h1_font, bg='#9bd7d1', fg='#ffffff')
header_label.pack()

header_frame = tk.Frame(root, bg='#9bd7d1', height=100)
header_frame.pack(side='top', fill='x')
header_label = tk.Label(header_frame, text='Hand Gesture Recognition', font=h1_font, bg='#9bd7d1', fg='#000000')
header_label.pack()


title_font = tkfont.Font(family='Times', size=30, weight="bold")
text_font = tkfont.Font(family='Times', size=18)

section_frame1 = tk.Frame(root, width=600, height=600, bg="#FFFFFF", highlightthickness=1, highlightbackground="#fff", padx=20, pady=20)
section_frame1.pack(side="left", padx=30, pady=30)

title_label1 = tk.Label(section_frame1, text="Text to Sign Converter", font=title_font, fg="#000000", bg="#FFFFFF")
title_label1.pack(pady=(20, 30))

# add image above description for section_frame1
img_label1 = tk.Label(section_frame1, image=text_to_sign_img, bg="#FFFFFF")
img_label1.pack(pady=(0, 30))

desc_label1 = tk.Label(section_frame1, text="A web tool that converts text to hand gestures of sign language", font=text_font, fg="#000000",bg="#FFFFFF", wraplength=500, justify="center")
desc_label1.pack(pady=(0, 30))

button1 = tk.Button(section_frame1, text="Get Started", font=text_font, fg="#000000", bg="#FFFFFF", bd=1, relief="solid", padx=20, pady=10, cursor="hand2", command=lambda: subprocess.Popen('textToSign.exe'))
button1.pack()

section_frame2 = tk.Frame(root, width=600, height=600, bg="#FFFFFF", highlightthickness=1, highlightbackground="#FFFFFF", padx=20, pady=20)
section_frame2.pack(side="right", padx=30, pady=30)

title_label2 = tk.Label(section_frame2, text="Sign to Text Converter", font=title_font, fg="#000000", bg="#FFFFFF")
title_label2.pack(pady=(20, 30))

# add image above description for section_frame2

img_label2 = tk.Label(section_frame2, image=sign_to_text_img, bg="#FFFFFF")
img_label2.pack(pady=(0, 30))



desc_label2 = tk.Label(section_frame2, text="A web tool that converts hand gestures of sign language into text", font=text_font, fg="#000000", bg="#FFFFFF", wraplength=500, justify="center")
desc_label2.pack(pady=(0, 30))

button2 = tk.Button(section_frame2, text="Get Started", font=text_font, fg="#000000", bg="#FFFFFF", bd=1, relief="solid", padx=20, pady=10, cursor="hand2", command=lambda: subprocess.Popen('handGestureRecognition.exe'))
button2.pack()

footer_frame = tk.Frame(root, bg="#333")
footer_frame.pack(side="bottom", fill="x")

# create a frame for the label
developed_by_frame = tk.Frame(root, bg='#9bd7d1', height=50)
developed_by_frame.pack(side='bottom', fill='x')

# create the label and set its position to the center
developed_by_label = tk.Label(developed_by_frame, text='Developed by Udayraj, Jay, Harsh', font=p_font, bg='#9bd7d1', fg='#000000')
developed_by_label.place(relx=0.2, rely=1.5, anchor='ne')


root.mainloop()
