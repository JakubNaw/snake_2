import funkcje
from functools import partial
from tkinter import *
import gra

def uzytkownik(session, ikona_dla_okienka, okienko_logowania, login):
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
    # labele
    login_label = Label(okienko_uzytkownika, font=('Calibri', 15), bg='#76e95f', text=login)
    login_label.place(x=550, y=20)
    record_label = Label(okienko_uzytkownika, font=('Calibri', 15), bg='#76e95f', text=funkcje.rekord(session, login))
    record_label.place(x=550, y=50)
    games_played_label = Label(okienko_uzytkownika, font=('Calibri', 15), bg='#76e95f',
                               text=funkcje.games_played(session, login))
    games_played_label.place(x=550, y=80)
    tlo_image = PhotoImage(file="C:/Users/user/PycharmProjects/snake_2/zdjecie_w_tle.png")
    tlo_label = Label(okienko_uzytkownika, image=tlo_image, bg='#76e95f')
    tlo_label.place(x=150, y=120)
    # button
    graj_button = Button(okienko_uzytkownika, text='GRAJ',
                         font=('Calibiri', 30), background='white', relief=RAISED, bd=10, compound="bottom",
                         command=partial(gra.granie, session, ikona_dla_okienka, okienko_uzytkownika))
    graj_button.place(x=320, y=560)

    okienko_uzytkownika.mainloop()
