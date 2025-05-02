import tkinter as tk
from tkinter.font import BOLD
import Window as win
from tkinter import ttk
import Config_Record as cnfg

#### ### Configs ### ###

bgc = cnfg.Configs().bgc
fgc = cnfg.Configs().fgc
abgc = cnfg.Configs().abgc
afgc = cnfg.Configs().afgc
tc = cnfg.Configs().tc
tbc = cnfg.Configs().tbc
ebg = cnfg.Configs().ebg
etc = cnfg.Configs().etc
font = cnfg.Configs().font
efont = cnfg.Configs().efont

### ### Questions ### ###

# Multiple Choice Question #
# Inputs user input via radio button, Dict dictionary, and question
# Outputs Radio_var IntVar and btnSubmit (so it can be disabled) to mc_submit
def mc_question(Dict, question):
    root, Frame = win.window()

    lblQuestion = tk.Label(Frame,
    text=question[2],
    font=("Courier New", 14, BOLD),
    relief=tk.SUNKEN,
    bd=6,
    padx=10,
    pady=5,
    fg=tc,
    bg=tbc,
    wraplength=550,
    justify="left"
    ); lblQuestion.grid(row=0, column=0, columnspan=2, pady=15)

    radio_var = tk.IntVar()
    radio_var.set(1)
    rbtnOption1 = tk.Radiobutton(Frame,
    text=question[3],
    font=font,
    relief=tk.RAISED,
    bd=5,
    padx=10,
    pady=5,
    fg=tc,
    bg=tbc,
    activeforeground=tbc,
    activebackground=bgc,
    variable=radio_var,
    value=1
    ); rbtnOption1.grid(row=1, column=0, pady=5)

    rbtnOption2 = tk.Radiobutton(Frame,
    text=question[4],
    font=font,
    relief=tk.RAISED,
    bd=5,
    padx=10,
    pady=5,
    fg=tc,
    bg=tbc,
    activeforeground=tbc,
    activebackground=bgc,
    variable=radio_var,
    value=2
    ); rbtnOption2.grid(row=1, column=1, pady=5)

    rbtnOption3 = tk.Radiobutton(Frame,
    text=question[5],
    font=font,
    relief=tk.RAISED,
    bd=5,
    padx=10,
    pady=5,
    fg=tc,
    bg=tbc,
    activeforeground=tbc,
    activebackground=bgc,
    variable=radio_var,
    value=3
    ); rbtnOption3.grid(row=2, column=0, pady=5)

    rbtnOption4 = tk.Radiobutton(Frame,
    text=question[6],
    font=font,
    relief=tk.RAISED,
    bd=5,
    padx=10,
    pady=5,
    fg=tc,
    bg=tbc,
    activeforeground=tbc,
    activebackground=bgc,
    variable=radio_var,
    value=4
    ); rbtnOption4.grid(row=2, column=1, pady=5)

    btnSubmit = tk.Button(Frame,
    text="Submit",
    font=font,
    relief=tk.RAISED,
    bd=5,
    padx=10,
    pady=5,
    fg=tc,
    bg=tbc,
    activeforeground=tbc,
    activebackground=bgc,
    command=lambda:mc_submit(radio_var, btnSubmit)
    ); btnSubmit.grid(row=3, column=0, pady=15)

    lblScore = tk.Label(Frame,
    text=str(Dict["Score"]//100) + "/37",
    font=font,
    relief=tk.SUNKEN,
    bd=6,
    padx=10,
    pady=10,
    fg=tc,
    bg=tbc
    ); lblScore.grid(row=3, column=1)

    # Displays the mark and adds score based on difficulty
    # Score is multiplied by 100 to prevent RAM manipulation
    # Inputs radio_var IntVar and btnSubmit
    # Outputs mark string, Frame, root, and btnSubmit to display_mark function
    def mc_submit(radio_var, btnSubmit):
        mark=""
        if question[7] == radio_var.get():
            Dict["Score"] += 100*question[1]
            mark="Correct!"
        else:
            mark="Incorrect!"
        display_mark(mark, Frame, root, btnSubmit)

    root.mainloop()

# Fill in the Blank Question #
# Inputs user input via entry, Dict dictionary, and question
# Outputs string_var StringVar, and btnSubmit to fib_submit function
def fib_question(Dict, question):
    root, Frame = win.window()

    lblFIB = tk.Label(Frame,
    text="Fill in the Blank:",
    font=("Courier New", 18, BOLD),
    relief=tk.SUNKEN,
    bd=6,
    padx=10,
    pady=5,
    fg=tc,
    bg=tbc
    ); lblFIB.grid(row=0, column=0, columnspan=2, pady=25)

    lblQuestion = tk.Label(Frame,
    text=question[2],
    font=("Courier New", 16, BOLD),
    relief=tk.SUNKEN,
    bd=6,
    padx=10,
    pady=5,
    fg=tc,
    bg=tbc,
    wraplength=550
    ); lblQuestion.grid(row=1, column=0, columnspan=2, pady=10)

    string_var=tk.StringVar()
    entAnswer = tk.Entry(Frame,
    font=efont,
    relief=tk.SUNKEN,
    bd=6,
    fg=etc,
    bg=ebg,
    textvariable=string_var
    ); entAnswer.grid(row=2, column=0, columnspan=2, pady=10)

    btnSubmit = tk.Button(Frame,
    text="Submit",
    font=font,
    relief=tk.RAISED,
    bd=5,
    padx=10,
    pady=5,
    fg=tc,
    bg=tbc,
    activeforeground=tbc,
    activebackground=bgc,
    command=lambda:fib_submit(string_var, btnSubmit)
    ); btnSubmit.grid(row=3, column=0, pady=15)

    lblScore = tk.Label(Frame,
    text=str(Dict["Score"]//100) + "/37",
    font=font,
    relief=tk.SUNKEN,
    bd=6,
    padx=10,
    pady=10,
    fg=tc,
    bg=tbc
    ); lblScore.grid(row=3, column=1)

    # Displays the mark and adds score based on difficulty
    # Score is multiplied by 100 to prevent RAM manipulation
    # Inputs string_var StringVar and btnSubmit
    # Outputs mark string, Frame, root, and btnSubmit to display_mark function
    def fib_submit(string_var, btnSubmit):
        mark=""
        if question[3].upper() == string_var.get().upper():
            Dict["Score"] += 100*question[1]
            mark="Correct!"
        else:
            mark="Incorrect!"
        display_mark(mark, Frame, root, btnSubmit)

    root.mainloop()

# Rank in Order Questions #
# Inputs user input via three combo boxes, Dict dictionary, and question
# Outputs string_var1, 2 and 3 StringVars and btnSubmit to rio_Submit function
def rio_question(Dict, question):
    root, Frame = win.window()

    lblQuestion = tk.Label(Frame,
    text=question[2],
    font=("Courier New", 16, BOLD),
    relief=tk.SUNKEN,
    bd=6,
    padx=10,
    pady=5,
    fg=tc,
    bg=tbc,
    wraplength=550
    ); lblQuestion.grid(row=0, column=0, columnspan=2, pady=10)

    lblOne = tk.Label(Frame,
    text="1.",
    font=font,
    relief=tk.SUNKEN,
    bd=6,
    padx=5,
    pady=5,
    fg=tc,
    bg=tbc
    ); lblOne.grid(row=1, column=0, pady=5)

    string_var1 = tk.StringVar()
    cmbOp1 = ttk.Combobox(Frame,
    textvariable=string_var1,
    state="readonly",
    values=list(set(question[3])),
    font=font
    ); cmbOp1.grid(row=1, column=1)

    lblTwo = tk.Label(Frame,
    text="2.",
    font=font,
    relief=tk.SUNKEN,
    bd=6,
    padx=5,
    pady=5,
    fg=tc,
    bg=tbc
    ); lblTwo.grid(row=2, column=0, pady=5)

    string_var2 = tk.StringVar()
    cmbOp2 = ttk.Combobox(Frame,
    textvariable=string_var2,
    state="readonly",
    values=list(set(question[3])),
    font=font
    ); cmbOp2.grid(row=2, column=1)

    lblThree = tk.Label(Frame,
    text="3.",
    font=font,
    relief=tk.SUNKEN,
    bd=6,
    padx=5,
    pady=5,
    fg=tc,
    bg=tbc
    ); lblThree.grid(row=3, column=0, pady=5)

    string_var3 = tk.StringVar()
    cmbOp3 = ttk.Combobox(Frame,
    textvariable=string_var3,
    state="readonly",
    values=list(set(question[3])),
    font=font
    ); cmbOp3.grid(row=3, column=1)

    btnSubmit = tk.Button(Frame,
    text="Submit",
    font=font,
    relief=tk.RAISED,
    bd=5,
    padx=10,
    pady=5,
    fg=tc,
    bg=tbc,
    activeforeground=tbc,
    activebackground=bgc,
    command=lambda:rio_submit(string_var1, string_var2, string_var3, btnSubmit)
    ); btnSubmit.grid(row=4, column=0, pady=15)

    lblScore = tk.Label(Frame,
    text=str(Dict["Score"]//100) + "/37",
    font=font,
    relief=tk.SUNKEN,
    bd=6,
    padx=10,
    pady=10,
    fg=tc,
    bg=tbc
    ); lblScore.grid(row=4, column=1)

    # Marks the question and adds score based on difficulty
    # Score is multiplied by 100 to prevent RAM manipulation
    # Inputs var1, 2 and 3 StrngVars and btnSubmit
    # Outputs mark string, Frame, root, and btnSubmit to display_mark function
    def rio_submit(var1, var2, var3, btnSubmit):
        mark=""
        guess = [var1.get(), var2.get(), var3.get()]
        if guess == question[3]:
            Dict["Score"] += 100*question[1]
            mark="Correct!"
        else:
            mark="Incorrect!"
        display_mark(mark, Frame, root, btnSubmit)

    root.mainloop()

# Displays the mark, disables the submits buttons and allows the user to move to the next question
# Inputs mark string, Frame, root, and btnSubmit from each question
# Outputs root to btnnextcmd, as well as disabling the submit button to prevent users from submitting multiple attempts
def display_mark(mark, Frame, root, btnSubmit):
    lblMark = tk.Label(Frame,
    text=mark,
    font=font,
    relief=tk.SUNKEN,
    bd=6,
    padx=10,
    pady=5,
    fg=tc,
    bg=tbc
    ); lblMark.grid(row=5, column=0)

    btnNext = tk.Button(Frame,
    text="Next",
    font=font,
    relief=tk.RAISED,
    bd=5,
    padx=10,
    pady=5,
    fg=tc,
    bg=tbc,
    activeforeground=tbc,
    activebackground=bgc,
    command=lambda:btnnextcmd(root)
    ); btnNext.grid(row=5, column=1)

    btnSubmit.config(state="disabled")

# Closes the window which allows the next question to be displayed by the question manager module
# Inputs root
# Outputs closing the window
def btnnextcmd(root):
    root.destroy()