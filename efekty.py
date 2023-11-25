import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from narzedzia.moduly.efekty.kontrast.kontrast import *
from narzedzia.moduly.operacje.operacje import *

wejscie = 'grafika/jesien.jpg'
wyjscie = 'grafika/jesien_kontrast_Nimrod22_shstck.jpeg'
kontrast = Kontrast(wejscie, wyjscie)
kontrast.kontrast("2.8")

os.system("ffmpeg -i " + wyjscie + " " + wyjscie)

# operacje = Operacje('grafika/drzewo.jpg', 'grafika/wyciete-drzewo.jpeg')
# gdzie_wyciac = [10, 10, 300, 40]
# operacje.wytnij(gdzie_wyciac)
