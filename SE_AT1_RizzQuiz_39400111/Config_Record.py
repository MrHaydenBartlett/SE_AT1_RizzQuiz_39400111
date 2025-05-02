from tkinter.font import BOLD

# A class to hold most of the theming settings so if a change in theme is required, it can be done easily in one place
class Configs:
    def __init__(self,
        # Sets the duefault value as the theming variables
        bgc="Salmon3",
        fgc="LightSalmon2", 
        abgc="Salmon",
        afgc="LightSalmon",
        tc="Salmon4",
        tbc="LightSalmon",
        ebg="Ivory",
        etc="gray4",
        font=("Courier New", 14, BOLD),
        efont=("Courier New", 14, BOLD)):

        self.bgc = bgc
        self.fgc = fgc
        self.abgc = abgc
        self.afgc = afgc
        self.tc = tc
        self.tbc = tbc
        self.ebg = ebg
        self.etc = etc
        self.font = font
        self.efont = efont