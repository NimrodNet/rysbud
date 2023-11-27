# from narzedzia.moduly.efekty.tekst import *
from narzedzia.tekst import *
from narzedzia.grafika import *

# Wczytanie listy czcionek
#from tkinter import * 
#from tkinter import font

#root = Tk()  
#list_fonts = list(font.families())  
#print(list_fonts)


rozmiar = (1920, 1080)
kolor = (111, 53, 21)
wyjscie = "grafika/tlo.jpeg"
parametry = [rozmiar, kolor, wyjscie]
grafika = Grafika(parametry)
grafika.zapisz()


wejscie = wyjscie
wyjscie = wyjscie
tekst = "Jesień"
poczatek = (10, 10)
czcionka = "FreeMono.ttf"
rozmiar = 65
kolor = (255, 0, 0)
parametry = [wejscie, wyjscie, tekst, poczatek, czcionka, rozmiar, kolor]
tekst = Tekst(parametry)
tekst.rysuj()

rozmiar = (300, 190)
kolor = (11, 45, 201)
wyjscie = "grafika/tlo-miniatura.jpeg"
parametry = [rozmiar, kolor, wyjscie]
grafika = Grafika(parametry)
grafika.zapisz()

wejscie = wyjscie
wyjscie = wyjscie
tekst = "Jesień"
poczatek = (10, 10)
czcionka = "FreeMono.ttf"
rozmiar = 25
kolor = (255, 0, 0)
parametry = [wejscie, wyjscie, tekst, poczatek, czcionka, rozmiar, kolor]
tekst = Tekst(parametry)
tekst.rysuj()
