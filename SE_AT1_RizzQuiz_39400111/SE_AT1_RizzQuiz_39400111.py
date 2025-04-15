import tkinter as tk

### Configs ###
# Background Colour
bgc="Salmon3"
# Foreground Colour
fgc="LightSalmon2"
# Active Background Colour
abgc="Salmon"
# Active Foreground Colour
afgc="LightSalmon"

# Root Creatiation & Customisation
root = tk.Tk()
root.resizable(False,False)
root.geometry("640x480")
root.config(bg=bgc)
root.title("Quiz")




root.mainloop()