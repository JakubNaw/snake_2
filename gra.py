import time

import funkcje
from functools import partial
from tkinter import *


def granie(session, ikona_dla_okienka, uzytkownik, login, games_played_label, rekord_label):
    okienko_gry = Toplevel()  # ustawienie nowego okna jako glownego
    uzytkownik.withdraw()  # zamykanie starego okna
    okienko_gry.resizable(width=False, height=False)  # ustawienie braku zmiany rozmiaru okna
    okienko_gry.geometry("750x750")  # wybieranie rozdzielczosci
    okienko_gry.configure(bg='#76e95f')  # tlo okna ustawione na zielony kolorek
    okienko_gry.iconphoto(False, ikona_dla_okienka)  # ustawienie ikony
    okienko_gry.title("GRA")  # ustawienie tytulu okna
    # canvas
    canvas = Canvas(okienko_gry, width=750, height=650, bg="black")
    canvas.place(x=0, y=80)
    # zmienne poczatkowe
    wynik = 0
    # label
    wynik_label = Label(okienko_gry, font=('Calibri', 30), bg='#76e95f', text='Wynik: ' + str(wynik))
    wynik_label.place(x=320, y=10)
    # gra
    def start(button):
        button.destroy()
        wonsz = funkcje.Cialo(2, canvas)
        jedzienie = funkcje.Jedzenie(canvas)
        okienko_gry.bind("<w>", lambda event: funkcje.zmiana_kierunku('gora'))
        okienko_gry.bind("<s>", lambda event: funkcje.zmiana_kierunku('dol'))
        okienko_gry.bind("<a>", lambda event: funkcje.zmiana_kierunku('lewo'))
        okienko_gry.bind("<d>", lambda event: funkcje.zmiana_kierunku('prawo'))
        funkcje.ruch(wonsz, jedzienie, okienko_gry, canvas, wynik, wynik_label, uzytkownik, session, ikona_dla_okienka,
                     login, games_played_label, rekord_label)
        # button

    start_button = Button(canvas, text='START',
                          font=('Calibiri', 30), background='white', relief=RAISED, bd=10, compound="bottom")
    start_button.place(x=300, y=300)
    start_button.config(command=partial(start,start_button))
    okienko_gry.mainloop()
