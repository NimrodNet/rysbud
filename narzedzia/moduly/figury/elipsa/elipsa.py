from PIL import Image, ImageDraw, ImageFont

class Elipsa:

    def __init__(self, tlo, srodek, rozmiar):
        self.tlo = tlo
        self.srodek = srodek
        self.rozmiar = rozmiar

    def rysuj(self):
        grafika = self.tlo.zwroc()
        x = self.srodek[0]
        y = self.srodek[1]
        szerokosc = self.rozmiar[0]
        wysokosc = self.rozmiar[1]
        ksztalt = [(x, y), (szerokosc, wysokosc)]
        rysunek = ImageDraw.Draw(grafika)
        rysunek.ellipse(ksztalt, outline="black")
