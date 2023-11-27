from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class Tekst:

    def __init__(self, parametry):
        self.wejscie = parametry[0]
        self.wyjscie = parametry[1]
        self.tekst = parametry[2]
        self.poczatek = parametry[3]
        self.czcionka = parametry[4]
        self.rozmiar = parametry[5]
        self.kolor = parametry[6]

    def rysuj(self):
        podstawa = Image.open(self.wejscie)
        grafika = ImageDraw.Draw(podstawa)
        rozmiar = self.rozmiar
        czcionka = ImageFont.truetype(self.czcionka, self.rozmiar)
        kolor = self.kolor
        grafika.text(self.poczatek, self.tekst, font=czcionka, fill=self.kolor)
        podstawa.save(self.wyjscie)

