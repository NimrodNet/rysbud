from narzedzia.grafika import *

rozmiar = (700, 1000)
kolor = (112, 113, 61)
wyjscie = "grafika/tlo.jpeg"
parametry = [rozmiar, kolor, wyjscie]
grafika = Grafika(parametry)
grafika.zapisz()
