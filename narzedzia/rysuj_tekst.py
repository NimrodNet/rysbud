from grafika import *
from rysotekst import *

class Tekst:

    def stworz_tlo(self, parametry):
        rozmiar = parametry[0]
        kolor = parametry[1]
        wyjscie = parametry[2]
        parametry = [rozmiar, kolor, wyjscie]
        grafika = Grafika(parametry)
        grafika.zapisz()

    def dopisz_tekst(self, parametry):
        wejscie = parametry[0]
        wyjscie = parametry[1]
        tekst = parametry[2]
        poczatek = parametry[3]
        czcionka = parametry[4]
        rozmiar = parametry[5]
        kolor = parametry[6]
        parametry = [wejscie, wyjscie, tekst, poczatek, czcionka, rozmiar, kolor]
        rysotekst = Rysotekst(parametry)
        rysotekst.rysuj()
