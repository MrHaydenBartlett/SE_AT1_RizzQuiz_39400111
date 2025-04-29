import tkinter as tk
from tkinter.font import BOLD

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
def window():
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