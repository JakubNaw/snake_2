import funkcje
from functools import partial
from tkinter import *


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
    login_label.place(x=200, y=200)
    haslo_label = Label(okienko_logowania, font=('Calibri', 25), bg='#76e95f', text='Hasło')
    haslo_label.place(x=200, y=250)
    brak_konta_label = Label(okienko_logowania, font=('Calibri', 15), bg='#76e95f', text='Nie masz konta?')
    brak_konta_label.place(x=270, y=310)

