from PIL import Image, ImageDraw, ImageFont, ImageFilter

class Kontrast:

    def __init__(self, wejscie, wyjscie):
        self.wejscie = str(wejscie)
        self.wyjscie = str(wyjscie)

    def kontrast(self, wartosc):
        im = Image.open(self.wejscie) 
        from PIL import ImageEnhance  
        enh = ImageEnhance.Contrast(im) 
        enh.enhance(float(wartosc)).save(self.wyjscie, quality=100)
