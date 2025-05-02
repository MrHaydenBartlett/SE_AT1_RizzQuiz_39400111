import tkinter as tk
import re
from tkinter.font import BOLD
import Window as win
import Config_Record as cnfg
import datetime
import Quiz_Manager as QuizMngr

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

# Displays the main menu, which stores the users name, SID, and time they started the quiz.
def main():
    root, Frame = win.window()

    # Variable Declaration #
    SID_var=tk.StringVar()
    Name_var=tk.StringVar()
    # Score is multiplied by 100 to prevent RAM manipulation
    Dict = {"Name": "", "SID":"", "Score":0, "Date":datetime.datetime.now()}

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
        bg=ebg,
        textvariable=Name_var
        ); entName.grid(row=2, column=0, pady=10)
    
        entSID = tk.Entry(Frame,
        font=efont,
        relief=tk.SUNKEN,
        bd=6,
        fg=etc,
        bg=ebg,
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
        QuizMngr.random_questions(Dict)

    root.mainloop()

# Only executes if the code is executed directly
if __name__ == "__main__":
    main()