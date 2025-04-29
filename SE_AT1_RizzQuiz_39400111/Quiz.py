import tkinter as tk
from tkinter.font import BOLD
import Window as win


### ### Configs ### ###

# Background Colour
bgc="Salmon3"
# Foreground Colour
fgc="LightSalmon2"
# Active Background Colour
abgc="Salmon"
# Active Foreground Colour
afgc="LightSalmon"
# Text Colour
tc="Salmon4"
# Text Background Colour
tbc="LightSalmon"
# Entry Text Colour
etc="gray4"
# Font
font=("Courier New", 18, BOLD)
# Entry Font
efont=("Courier New", 14, BOLD)

def Quiz(Dict):
    root, Frame = win.window()

    ### ### Questions ### ###

    # Multiple Choice Questions #
    question="Which option is B?"
    op1="A"
    op2="B"
    op3="C"
    op4="D"
    answer=2
    def MC_question():
        lblQuestion = tk.Label(Frame,
        text=question,
        font=("Courier New", 24, BOLD),
        relief=tk.SUNKEN,
        bd=6,
        padx=10,
        pady=5,
        fg=tc,
        bg=tbc
        ); lblQuestion.grid(row=0, column=0, columnspan=2, pady=50)

        radio_var = tk.IntVar()
        rbtnOption1 = tk.Radiobutton(Frame,
        text=op1,
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
        text=op2,
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
        text=op3,
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
        text=op4,
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
        activebackground=bgc
        ); btnSubmit.grid(row=3, column=0, pady=15)

        lblScore = tk.Label(Frame,
        text=str(Dict["Score"]//100) + "/30",
        font=font,
        relief=tk.SUNKEN,
        bd=6,
        padx=10,
        pady=10,
        fg=tc,
        bg=tbc,
        ); lblScore.grid(row=3, column=1)
    MC_question()

    # Fill in the Blank Questions #
    def FIB_question():
        pass
    #FIB_question()

    # Rank in Order Questions #
    def RIO_question():
        pass
    #RIO_question()

    root.mainloop()