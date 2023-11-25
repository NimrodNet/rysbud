from PIL import Image
import numpy as np

class Operacje:

    def __init__(self, wejscie, wyjscie):
        self.wejscie = wejscie
        self.wyjscie = wyjscie

    def wytnij(self, parametry):
        im = Image.open(self.wejscie)
        po_konwersji = parametry
        lewa = po_konwersji[0]
        gora = po_konwersji[1]
        prawa = po_konwersji[2]
        dol = po_konwersji[3]
        im1 = im.crop((lewa, gora, prawa, dol))
        im1.save(self.wyjscie)
