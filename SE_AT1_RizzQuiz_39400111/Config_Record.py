from tkinter.font import BOLD

class Configs:
    def __init__(self,
        bgc="Salmon3",
        fgc="LightSalmon2", 
        abgc="Salmon",
        afgc="LightSalmon",
        tc="Salmon4",
        tbc="LightSalmon",
        ebg="Ivory",
        etc="gray4",
        font=("Courier New", 18, BOLD),
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