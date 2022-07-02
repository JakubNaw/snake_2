import funkcje
from functools import partial
from tkinter import *
def rankingi(session, ikona_dla_okienka, menu_start, canvas,glowa):
    okienko_rankingow = Toplevel()  # ustawienie nowego okna jako glownego
    menu_start.withdraw()  # zamykanie starego okna
    okienko_rankingow.resizable(width=False, height=False)  # ustawienie braku zmiany rozmiaru okna
    okienko_rankingow.geometry("750x750")  # wybieranie rozdzielczosci
    okienko_rankingow.configure(bg='#76e95f')  # tlo okna ustawione na zielony kolorek
    okienko_rankingow.iconphoto(False, ikona_dla_okienka)  # ustawienie ikony
    okienko_rankingow.title("RANKINGI")  # ustawienie tytulu okna
    # guzik do wylogowywania sie
    guzik_powrotu = Button(okienko_rankingow, text='<--', font=('Calibiri', 25), background='white',
                            relief=RAISED, bd=10, compound="bottom", state=ACTIVE,
                            command=partial(funkcje.powrot, menu_start, okienko_rankingow,canvas, glowa)
                            )
    guzik_powrotu.place(x=0, y=0)
    #label
    ranking_label = Label(okienko_rankingow, font=('Calibri', 25), bg='#76e95f', text='RANKING')
    ranking_label.place(x=320, y=50)
    # lista
    ranking = Listbox(okienko_rankingow, font=("Calibri", 15), bg='white',
                      width=67, height=25)
    ranking.place(x=40, y=100)
    funkcje.wypelnianie_rankingu(session,ranking)