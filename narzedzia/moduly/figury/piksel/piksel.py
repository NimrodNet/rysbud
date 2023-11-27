from PIL import Image, ImageDraw, ImageFont

class Piksel:

    def __init__(self, grafika):
        self.piksele = self.wczytaj_mape(grafika)

    def wczytaj_mape(self, grafika):
        tlo = grafika.zwroc()
        return tlo.load()

    def rysuj(self, pozycja, kolor):
        x = pozycja[0]
        y = pozycja[1]
        self.piksele[x, y] = kolor

    def zwroc_piksele(self):
        return self.piksele
