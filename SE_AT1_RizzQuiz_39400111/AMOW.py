import Results
import Window as win
import tkinter as tk
import Config_Record as cnfg

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

# Displays the AMOW window
# Inputs Dict dictionary
# Outputs btnSubmit to enable_button and outputs Dict dictionary and root to submit functions
def amow(Dict):
    root, Frame = win.window()

    lblAMOW = tk.Label(Frame,
    # AMOW yap
    text="I solemnly declare that all the results I have are all my own work. I have not plagarised, used others work, used ai or shared my work with others.",
    font=font,
    relief=tk.SUNKEN,
    bd=6,
    padx=10,
    pady=10,
    fg=tc,
    bg=tbc,
    wraplength=550
    ); lblAMOW.pack(pady=15)

    cbtnAMOW = tk.Checkbutton(Frame,
    text="Agree",
    relief=tk.RAISED,
    bd=5,
    padx=10,
    pady=5,
    fg=tc,
    bg=tbc,
    activeforeground=tbc,
    activebackground=bgc,
    command=lambda:enable_button(btnSubmit)
    ); cbtnAMOW.pack(pady=15)

    btnSubmit = tk.Button(Frame,
    text="Submit",
    state="disabled",
    font=font,
    relief=tk.RAISED,
    bd=5,
    padx=10,
    pady=5,
    fg=tc,
    bg=tbc,
    activeforeground=tbc,
    activebackground=bgc,
    command=lambda:submit(Dict, root)
    ); btnSubmit.pack(pady=15)

    root.mainloop()

# Allows the submit button to be clicked only if the user has agreed to the AMOW statement
# Inputs btnSubmit
# Outputs the toggling of the state of the submit button
def enable_button(btnSubmit):
    # Switches the buttons state based off of the value of the checkbutton
    if btnSubmit["state"] == "disabled":
        btnSubmit.config(state="normal")
    else:
        btnSubmit.config(state="disabled")

# Closes window and runs the Results.results function
# Inputs Dict dictionary and root
# Outputs Dict dictionary to Results.results function
def submit(Dict, root):
    root.destroy()
    Results.results(Dict)