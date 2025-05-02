import Window as win
import tkinter as tk
import Config_Record as cnfg
import Main
import Results_Manager as rm

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

# Displays the results page and adds the results to a txt file via the Results_Manager.AddResults function
# Inputs Dict dictionary
# Outputs Dict["Score"] dictionary item to user via label and outputs Dict dictionary to the Results_Manager.AddResults function
# Outputs root to quit_app and retry functions
def results(Dict):
    root, Frame = win.window()

    lblScore = tk.Label(Frame,
    text="You scored: " + str(Dict["Score"]//100) + "/37",
    font=font,
    relief=tk.SUNKEN,
    bd=6,
    padx=10,
    pady=10,
    fg=tc,
    bg=tbc,
    wraplength=550
    ); lblScore.grid(row=0, column=0, pady=15, padx=10)

    lblScorePercent = tk.Label(Frame,
    text=str(Dict["Score"]//37) + "%",
    font=font,
    relief=tk.SUNKEN,
    bd=6,
    padx=10,
    pady=10,
    fg=tc,
    bg=tbc,
    wraplength=550
    ); lblScorePercent.grid(row=0, column=1, pady=15, padx=10)

    lblGrade = tk.Label(Frame,
    text="Grade: " + grade(Dict),
    font=font,
    relief=tk.SUNKEN,
    bd=6,
    padx=10,
    pady=10,
    fg=tc,
    bg=tbc,
    wraplength=550
    ); lblGrade.grid(row=1, column=0, columnspan=2, pady=15)

    btnQuit = tk.Button(Frame,
    text="Quit",
        font=font,
        relief=tk.RAISED,
        bd=5,
        padx=10,
        pady=5,
        fg=tc,
        bg=tbc,
        activeforeground=tbc,
        activebackground=bgc,
        command=lambda:quit_app(root)
    ); btnQuit.grid(row=2, column=0, pady=15, padx=10)

    btnRetry = tk.Button(Frame,
    text="Retry",
        font=font,
        relief=tk.RAISED,
        bd=5,
        padx=10,
        pady=5,
        fg=tc,
        bg=tbc,
        activeforeground=tbc,
        activebackground=bgc,
        command=lambda:retry(root)
    ); btnRetry.grid(row=2, column=1, pady=15, padx=10)

    rm.AddResults(Dict)

    root.mainloop()

# Returns the grade based off of the score
# Grade is based off of the letters of my name (Jayden) where J is 100%, A is the second highest and N is the lowest
# Inputs Dict dictionary
# Retuns grade in char form (could be string, but who knows its python)
def grade(Dict):
    percent = Dict["Score"]//37
    if percent == 100:
        return "J"
    elif percent > 80:
        return "A"
    elif percent > 60:
        return "Y"
    elif percent > 40:
        return "D"
    elif percent > 20:
        return "E"
    else:
        return "N"

# Quits the app
# Inputs root
# Outputs closing window
def quit_app(root):
    root.destroy()

# Restarts from the main menu
# Inputs root
# Outputs by closing window and opening Main.main function
def retry(root):
    root.destroy()
    Main.main()