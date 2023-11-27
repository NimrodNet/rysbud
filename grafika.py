from narzedzia.grafika import *
import random

numer_grafiki = 1
for indeks in range(100):
    niebieski = random.randint(1, 255)
    czerwony = random.randint(1, 255)
    zielony = random.randint(1, 255)
    rozmiar = (1500, 2850)
    kolor = (czerwony, zielony, niebieski)
    wyjscie = "grafika/tlo" + str(numer_grafiki) + ".jpeg"
    parametry = [rozmiar, kolor, wyjscie]
    grafika = Grafika(parametry)
    grafika.zapisz()
    numer_grafiki += 1
