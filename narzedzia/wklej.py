from PIL import Image, ImageDraw, ImageFilter

class Wklej_grafike:

    def __init__(self, parametry):
        self.wejscie_1 = parametry[0]
        self.wejscie_2 = parametry[1]
        self.poczatek = parametry[2]
        self.wyjscie = parametry[3]

    def wklej(self):
        grafika_1 = Image.open(self.wejscie_1)  
        grafika_2 = Image.open(self.wejscie_2) 
        grafika_1.paste(grafika_2, self.poczatek) 
        grafika_1.save(self.wyjscie)

