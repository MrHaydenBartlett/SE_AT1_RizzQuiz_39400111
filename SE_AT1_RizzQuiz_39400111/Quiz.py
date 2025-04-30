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

def Quiz(Dict):
    root, Frame = win.window()

    ### ### Questions ### ###

    # Multiple Choice Questions #
    mc_q="Which option is B?"
    mc_op1="A"
    mc_op2="B"
    mc_op3="C"
    mc_op4="D"
    mc_a=2
    def mc_question():
        lblQuestion = tk.Label(Frame,
        text=mc_q,
        font=("Courier New", 24, BOLD),
        relief=tk.SUNKEN,
        bd=6,
        padx=10,
        pady=5,
        fg=tc,
        bg=tbc
        ); lblQuestion.grid(row=0, column=0, columnspan=2, pady=25)

        radio_var = tk.IntVar()
        radio_var.set(1)
        rbtnOption1 = tk.Radiobutton(Frame,
        text=mc_op1,
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
        text=mc_op2,
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
        text=mc_op3,
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
        text=mc_op4,
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
        command=lambda:mc_submit(radio_var)
        ); btnSubmit.grid(row=3, column=0, pady=15)

        lblScore = tk.Label(Frame,
        text=str(Dict["Score"]//100) + "/30",
        font=font,
        relief=tk.SUNKEN,
        bd=6,
        padx=10,
        pady=10,
        fg=tc,
        bg=tbc
        ); lblScore.grid(row=3, column=1)

    def mc_submit(radio_var):
        mark=""
        if mc_a == radio_var.get():
            Dict["Score"] += 100
            mark="Correct!"
        else:
            mark="Incorrect!"
        display_mark(mark)

    #mc_question()

    # Fill in the Blank Questions #
    fib_q="Charlton, do your ____!"
    fib_a="Clusters"
    def fib_question():
        lblFIB = tk.Label(Frame,
        text="Fill in the Blank:",
        font=("Courier New", 20, BOLD),
        relief=tk.SUNKEN,
        bd=6,
        padx=10,
        pady=5,
        fg=tc,
        bg=tbc
        ); lblFIB.grid(row=0, column=0, columnspan=2, pady=25)

        lblQuestion = tk.Label(Frame,
        text=fib_q,
        font=("Courier New", 20, BOLD),
        relief=tk.SUNKEN,
        bd=6,
        padx=10,
        pady=5,
        fg=tc,
        bg=tbc
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
        command=lambda:fib_submit(string_var)
        ); btnSubmit.grid(row=3, column=0, pady=15)

        lblScore = tk.Label(Frame,
        text=str(Dict["Score"]//100) + "/30",
        font=font,
        relief=tk.SUNKEN,
        bd=6,
        padx=10,
        pady=10,
        fg=tc,
        bg=tbc
        ); lblScore.grid(row=3, column=1)

    def fib_submit(string_var):
        mark=""
        if fib_a.upper() == string_var.get().upper():
            Dict["Score"] += 100
            mark="Correct!"
        else:
            mark="Incorrect!"
        display_mark(mark)

    #fib_question()

    # Rank in Order Questions #
    rio_q="Rank in Order:"
    rio_op1="One"
    rio_op2="Two"
    rio_op3="Three"
    rio_a=[0,1,2]
    def rio_question():
        lblQuestion = tk.Label(Frame,
        text=rio_q,
        font=("Courier New", 24, BOLD),
        relief=tk.SUNKEN,
        bd=6,
        padx=10,
        pady=5,
        fg=tc,
        bg=tbc
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

        string_var = tk.StringVar()
        cmbOp1 = ttk.Combobox(Frame,
        textvariable=string_var
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

        string_var = tk.StringVar()
        cmbOp2 = ttk.Combobox(Frame,
        textvariable=string_var,
        values=[rio_op1, rio_op2, rio_op3]
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

        string_var = tk.StringVar()
        cmbOp3 = ttk.Combobox(Frame,
        textvariable=string_var
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
        command=lambda:rio_submit(string_var)
        ); btnSubmit.grid(row=4, column=0, pady=15)

        lblScore = tk.Label(Frame,
        text=str(Dict["Score"]//100) + "/30",
        font=font,
        relief=tk.SUNKEN,
        bd=6,
        padx=10,
        pady=10,
        fg=tc,
        bg=tbc
        ); lblScore.grid(row=4, column=1)

    def rio_submit():
        pass

    rio_question()

    # Displays the mark, adds a delay and moves to the next question
    def display_mark(mark):
        lblMark = tk.Label(Frame,
        text=mark,
        font=font,
        relief=tk.SUNKEN,
        bd=6,
        padx=10,
        pady=5,
        fg=tc,
        bg=tbc
        ); lblMark.grid(row=4, column=0, columnspan=2)

    root.mainloop()