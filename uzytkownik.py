import funkcje
from functools import partial
from tkinter import *


def uzytkownik(session, ikona_dla_okienka, okienko_logowania):
    okienko_uzytkownika = Toplevel()  # ustawienie nowego okna jako glownego
    okienko_logowania.withdraw()  # zamykanie starego okna
    okienko_uzytkownika.resizable(width=False, height=False)  # ustawienie braku zmiany rozmiaru okna
    okienko_uzytkownika.geometry("750x750")  # wybieranie rozdzielczosci
    okienko_uzytkownika.configure(bg='#76e95f')  # tlo okna ustawione na zielony kolorek
    okienko_uzytkownika.iconphoto(False, ikona_dla_okienka)  # ustawienie ikony
    okienko_uzytkownika.title("EKRAN UŻYTKOWNIKA")  # ustawienie tytulu okna
    # guzik do wylogowywania sie
    guzik_wyloguj = Button(okienko_uzytkownika, text='Wyloguj sie', font=('Calibiri', 25), background='white',
                            relief=RAISED, bd=10, compound="bottom", state=ACTIVE,
                            command=partial(funkcje.wyloguj_sie, okienko_logowania, okienko_uzytkownika))
    guzik_wyloguj.place(x=0, y=0)
    okienko_uzytkownika.mainloop()