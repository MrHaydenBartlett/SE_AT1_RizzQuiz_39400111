import tkinter as tk
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

# Creates a standardised window that can be executed easily from other modules
def window():
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

    return root, Frame