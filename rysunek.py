from PIL import Image, ImageDraw, ImageFont
from narzedzia.moduly.prostokat.prostokat import *
from narzedzia.moduly.linia.linia import *

rozmiar_tla = [800, 800]
tlo = Prostokat(rozmiar_tla)

linia = Linia(tlo)

# obrys
linia.rysuj([10, 10], [10, 790])
linia.rysuj([10, 790], [790, 790])
linia.rysuj([790, 790], [790, 10])
linia.rysuj([790, 10], [10, 10])

# korytarz
linia.rysuj([10, 300], [250, 300])
linia.rysuj([10, 500], [250, 500])

# środkowy pokój
linia.rysuj([250, 300], [250, 170])
linia.rysuj([250, 170], [500, 170])
linia.rysuj([500, 170], [500, 650])
linia.rysuj([500, 650], [250, 650])
linia.rysuj([250, 650], [250, 300])

linia.rysuj([375, 170], [375, 10])
linia.rysuj([375, 650], [375, 790])
linia.rysuj([500, 390], [790, 390])

tlo.zapisz("tlo.jpg")
tlo.pokaz("tlo.jpg")
