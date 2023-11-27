from PIL import Image

class Grafika:

    def __init__(self, parametry):
        self.rozmiar = parametry[0]
        self.kolor = parametry[1]
        self.wyjscie = parametry[2]
        self.stworz()

    def stworz(self):
        self.rysunek = Image.new( mode = "RGB", size = self.rozmiar, color = self.kolor )

    def zwroc(self):
        return self.rysunek

    def zapisz(self):
        self.rysunek.save(self.wyjscie)
