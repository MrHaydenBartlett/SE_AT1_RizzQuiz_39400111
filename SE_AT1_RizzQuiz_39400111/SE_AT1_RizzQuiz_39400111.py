import tkinter as tk
from tkinter.font import BOLD
from tkinter.tix import COLUMN

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

# Root Creation & Customisation #
root = tk.Tk()
root.resizable(False,False)
root.geometry("640x480")
root.config(bg=tc)
root.title("Quiz")

# Main Frame (I'm past the firewall and I've hacked into mainframe) #
Frame = tk.Frame(root,
bg=bgc,
relief=tk.RAISED,
bd=5,
pady=15,
padx=25
); Frame.pack(pady=20)

### ### Main Menu ### ###

def main_menu():
    lblTitle = tk.Label(Frame,
    text="11 Software Engineering Test",
    font=("Courier New", 24, BOLD),
    relief=tk.SUNKEN,
    bd=6,
    padx=10,
    pady=5,
    fg=tc,
    bg=tbc
    ); lblTitle.grid(row=0, column=0, columnspan=2, pady=25)

    lblName = tk.Label(Frame,
    text="Input Name",
    font=font,
    relief=tk.SUNKEN,
    bd=6,
    padx=10,
    pady=5,
    fg=tc,
    bg=tbc
    ); lblName.grid(row=1, column=0, pady=10)

    lblSID = tk.Label(Frame,
    text="Input Student ID",
    font=font,
    relief=tk.SUNKEN,
    bd=6,
    padx=10,
    pady=5,
    fg=tc,
    bg=tbc
    ); lblSID.grid(row=1, column=1, pady=10)

    entName = tk.Entry(Frame,
    font=efont,
    relief=tk.SUNKEN,
    bd=6,
    fg=etc,
    bg="Ivory"
    ); entName.grid(row=2, column=0, pady=10)

    entSID = tk.Entry(Frame,
    font=efont,
    relief=tk.SUNKEN,
    bd=6,
    fg=etc,
    bg="Ivory"
    ); entSID.grid(row=2, column=1, pady=10)

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
    ); btnSubmit.grid(row=3, column=0, columnspan=2, pady=20)

    lblStatus = tk.Label(Frame,
    text="...",
    font=font,
    relief=tk.SUNKEN,
    bd=6,
    padx=10,
    pady=5,
    fg=tc,
    bg=tbc
    ); lblStatus.grid(row=4, column=0, columnspan=2, pady=10)

main_menu()

### ### Questions ### ###

# Testing question layout #
def test_multichoice_question():
    lblQuestion = tk.Label(Frame,
    text="Which option is B?",
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
    text="A",
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
    text="B",
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
    text="C",
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
    text="D",
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
    text="0/30",
    font=font,
    relief=tk.SUNKEN,
    bd=6,
    padx=10,
    pady=10,
    fg=tc,
    bg=tbc,
    ); lblScore.grid(row=3, column=1)
#test_multichoice_question()

# Multiple Choice Questions #


# Fill in the Blnak Questions #


# Rank in Order Questions #



root.mainloop()