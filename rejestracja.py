import funkcje
from functools import partial
from tkinter import *


def rejestracja(session, ikona_dla_okienka, okienko_logowania):
    okienko_rejestracji = Toplevel()  # ustawienie nowego okna jako glownego
    okienko_logowania.withdraw()  # zamykanie starego okna
    okienko_rejestracji.resizable(width=False, height=False)  # ustawienie braku zmiany rozmiaru okna
    okienko_rejestracji.geometry("750x750")  # wybieranie rozdzielczosci
    okienko_rejestracji.configure(bg='#76e95f')  # tlo okna ustawione na zielony kolorek
    okienko_rejestracji.iconphoto(False, ikona_dla_okienka)  # ustawienie ikony
    okienko_rejestracji.title("EKRAN UŻYTKOWNIKA")  # ustawienie tytulu okna
    # guzik do wylogowywania sie
    guzik_portow = Button(okienko_rejestracji, text='<--', font=('Calibiri', 25), background='white',
                          relief=RAISED, bd=10, compound="bottom", state=ACTIVE,
                          command=partial(funkcje.wyloguj_sie, okienko_logowania, okienko_rejestracji))
    guzik_portow.place(x=0, y=0)

    # label
    login_label = Label(okienko_rejestracji, font=('Calibri', 25), bg='#76e95f', text='Login')
    login_label.place(x=180, y=200)
    haslo_label = Label(okienko_rejestracji, font=('Calibri', 25), bg='#76e95f', text='Hasło')
    haslo_label.place(x=180, y=250)
    haslo_again_label = Label(okienko_rejestracji, font=('Calibri', 25), bg='#76e95f', text='Powtórz Hasło')
    haslo_again_label.place(x=60, y=300)
    informacja_rejestracji_label = Label(okienko_rejestracji, font=('Calibri', 15), bg='#76e95f', fg='red', text='')
    informacja_rejestracji_label.place(x=345, y=460)

    # entrybox
    login_entry = Entry(okienko_rejestracji, font=("Calibri", 23), background='white')
    login_entry.place(x=265, y=200)
    haslo_entry = Entry(okienko_rejestracji, font=("Calibri", 23), background='white')
    haslo_entry.place(x=265, y=250)
    haslo_again_entry = Entry(okienko_rejestracji, font=("Calibri", 23), background='white')
    haslo_again_entry.place(x=265, y=300)

    # button
    zarejestruj_button = Button(okienko_rejestracji, text='Zarejestruj się',
                                font=('Calibiri', 20), background='white',
                                relief=RAISED, bd=10, compound="bottom",
                                command=partial(funkcje.rejestracja, session, login_entry, haslo_entry,
                                                haslo_again_entry, informacja_rejestracji_label, ikona_dla_okienka,
                                                okienko_rejestracji))
    zarejestruj_button.place(x=320, y=370)

    okienko_rejestracji.mainloop()
