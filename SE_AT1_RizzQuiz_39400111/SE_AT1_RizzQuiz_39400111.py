import time
import tkinter as tk
import re
from tkinter.font import BOLD
import Window as win
import Quiz as Start

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

root, Frame = win.window()

# Variable Declaration #
SID_var=tk.StringVar()
Name_var=tk.StringVar()
Dict = {"Name": "", "SID":"", "Score":0}

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
    bg="Ivory",
    textvariable=Name_var
    ); entName.grid(row=2, column=0, pady=10)
    
    entSID = tk.Entry(Frame,
    font=efont,
    relief=tk.SUNKEN,
    bd=6,
    fg=etc,
    bg="Ivory",
    textvariable=SID_var
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
    activebackground=bgc,
    command=lambda:btnSubmitCMD()
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

    # Handles the submit button click
    def btnSubmitCMD():
        NameCheck = check_Name()
        SIDCheck = check_SID()
        if NameCheck and SIDCheck:
            start_quiz()

    # Checks the validity of the inputted name
    def check_Name():
        Name=Name_var.get().upper()
        if len(Name) < 3:
            lblStatus.config(text="Name is too short!")
            return False
        IsValid = bool(re.match("^[A-Za-z- ]*$", Name))
        if not IsValid:
            lblStatus.config(text="Invalid Characters in Name!")
            return False
        Dict["Name"]=Name
        return True

    # Checks the validity of the inputted SID
    def check_SID():
        SID=SID_var.get()
        try:
            SID_Length = len(SID)
            SID=int(SID)
        except:
            lblStatus.config(text="SID is not an integer!")
            return False
        if SID_Length != 8:
            lblStatus.config(text="SID is not 8 digits!")
            return False
        Dict["SID"]=str(SID)
        return True
main_menu()

# Begins the quiz
def start_quiz():
    root.destroy()
    Start.Quiz(Dict)

root.mainloop()