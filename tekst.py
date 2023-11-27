from narzedzia.moduly.efekty.tekst import *

from tkinter import * 
from tkinter import font 
#create root window 
root = Tk() 
#get all the supported font families 
list_fonts = list(font.families()) 
#display them 
print(list_fonts)

FreeTypeFont()
load()
load_path()

wejscie = "grafika/jesien.jpg"
wyjscie = "grafika/jesien.jpeg"
tekst = "Jesień"
poczatek = (10, 10)
czcionka = "Go Medium.ttf"
rozmiar = 65
kolor = (255, 0, 0)
parametry = [wejscie, wyjscie, tekst, poczatek, czcionka, rozmiar, kolor]
tekst = Tekst(parametry)
tekst.rysuj()
