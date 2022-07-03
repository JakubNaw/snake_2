import funkcje
from functools import partial
from tkinter import *
import rejestracja


def login(session, ikona_dla_okienka, menu_start, canvas, glowa):
    okienko_logowania = Toplevel()  # ustawienie nowego okna jako glownego
    menu_start.withdraw()  # zamykanie starego okna
    okienko_logowania.resizable(width=False, height=False)  # ustawienie braku zmiany rozmiaru okna
    okienko_logowania.geometry("750x750")  # wybieranie rozdzielczosci
    okienko_logowania.configure(bg='#76e95f')  # tlo okna ustawione na zielony kolorek
    okienko_logowania.iconphoto(False, ikona_dla_okienka)  # ustawienie ikony
    okienko_logowania.title("EKRAN LOGOWANIA")  # ustawienie tytulu okna
    # guzik do wylogowywania sie
    guzik_powrotu = Button(okienko_logowania, text='<--', font=('Calibiri', 25), background='white',
                            relief=RAISED, bd=10, compound="bottom", state=ACTIVE,
                            command=partial(funkcje.powrot, menu_start, okienko_logowania, canvas, glowa))
    guzik_powrotu.place(x=0, y=0)
    # labele
    login_label = Label(okienko_logowania, font=('Calibri', 25), bg='#76e95f', text='Login')
    login_label.place(x=180, y=200)
    haslo_label = Label(okienko_logowania, font=('Calibri', 25), bg='#76e95f', text='Hasło')
    haslo_label.place(x=180, y=250)
    brak_konta_label = Label(okienko_logowania, font=('Calibri', 15), bg='#76e95f', text='Nie masz konta?')
    brak_konta_label.place(x=345, y=430)
    informacja_logowania_label = Label(okienko_logowania, font=('Calibri', 15), bg='#76e95f',fg='red', text='')
    informacja_logowania_label.place(x=345, y=400)
    # entry boxy
    login_entry = Entry(okienko_logowania, font=("Calibri", 23), background='white')
    login_entry.place(x=265, y=200)
    haslo_entry = Entry(okienko_logowania, font=("Calibri", 23), background='white')
    haslo_entry.place(x=265, y=250)
    # button
    zaloguj_button = Button(okienko_logowania, text='Zaloguj sie',
                          font=('Calibiri', 20), background='white',
                          relief=RAISED, bd=10, compound="bottom",
                          command=partial(funkcje.zaloguj_sie, session, ikona_dla_okienka, okienko_logowania, login_entry, haslo_entry, informacja_logowania_label))
    zaloguj_button.place(x=330, y=310)
    zarejestruj_button = Button(okienko_logowania, text='Zarejestruj sie' ,
                          font=('Calibiri', 15), background='white', relief=RAISED, bd=10, compound="bottom",
                          command= partial(rejestracja.rejestracja, session, ikona_dla_okienka, okienko_logowania))
    zarejestruj_button.place(x=337, y=460)

