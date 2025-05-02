import Window as win
import tkinter as tk
import Config_Record as cnfg
import Main

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

def results(Dict):
    root, Frame = win.window()

    lblScore = tk.Label(Frame,
    text="You scored: " + str(Dict["Score"]//100) + "/38",
    font=font,
    relief=tk.SUNKEN,
    bd=6,
    padx=10,
    pady=10,
    fg=tc,
    bg=tbc,
    wraplength=550
    ); lblScore.pack(pady=15)

    lblScorePercent = tk.Label(Frame,
    text=str(Dict["Score"]//38) + "%",
    font=font,
    relief=tk.SUNKEN,
    bd=6,
    padx=10,
    pady=10,
    fg=tc,
    bg=tbc,
    wraplength=550
    ); lblScorePercent.pack(pady=15)

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
    ); lblGrade.pack(pady=15)

    root.mainloop()

def grade(Dict):
    percent = Dict["Score"]//38
    if percent > 100:


def menu(root):
    root.destroy()
    Main.main()