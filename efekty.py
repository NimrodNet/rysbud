import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from narzedzia.moduly.efekty.kontrast.kontrast import *
from narzedzia.moduly.operacje.operacje import *

# wejscie = 'grafika/jesien.jpg'
# wyjscie = 'grafika/jesien_kontrast_Nimrod22_shstck.jpeg'
# kontrast = Kontrast(wejscie, wyjscie)
# kontrast.kontrast("2.8")

# os.system("ffmpeg -i " + wyjscie + " " + wyjscie)

# operacje = Operacje('grafika/drzewo.jpg', 'grafika/wyciete-drzewo.jpeg')
# gdzie_wyciac = [10, 10, 300, 40]
# operacje.wytnij(gdzie_wyciac)

from narzedzia.wklej import *

wejscie_1 = "grafika/jesien.jpg"
wejscie_2 = "grafika/jesien.jpeg"
poczatek = (200, 450)
wyjscie = "grafika/jesien-1.jpeg"
parametry = [wejscie_1, wejscie_2, poczatek, wyjscie]
wklejanie = Wklej_grafike(parametry)
wklejanie.wklej()
