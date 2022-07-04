import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from tkinter import *
from PIL import ImageTk, Image
import time
from sqlalchemy.orm import relationship
import uzytkownik

baza = declarative_base()
# tworzenie modeli


class Dane_do_logowania(baza):
    __tablename__ = 'dane_do_logowania'
    login = db.Column(db.String(100), primary_key=True)
    haslo = db.Column(db.String(100))
    relacja_1 = relationship('Informacje', backref='dane_do_logowania')


class Informacje(baza):
    __tablename__ = 'informacje'
    login = db.Column(db.String(100), db.ForeignKey('dane_do_logowania.login'), primary_key=True)
    record = db.Column(db.Integer)
    games_played = db.Column(db.Integer)


# funkcje
def czytaj_dane_do_logowania(session):
    for dane in session.query(Dane_do_logowania):
        print(dane.login, dane.haslo)
    print()


def czytaj_informacje(session):
    for informacje in session.query(Informacje):
        print(informacje.login, informacje.record, informacje.games_played)
    print()


def powrot(stare_okno, nowe_okno, canvas, glowa):
    # funnkcja powrotu do bylego okna
    nowe_okno.withdraw()
    stare_okno.deiconify()
    predkosc_X = 5
    predkosc_Y = 3
    glowa_img_1 = Image.open("C:/Users/user/PycharmProjects/snake_2/window_icon.png")  # tworzenie obrazu glowy

    while True:
        coordinates = canvas.coords(glowa)
        if coordinates[0] <= 0:
            predkosc_X = -predkosc_X
            if predkosc_Y > 0:
                glowa_img = glowa_img_1.rotate(315)
                glowa_photo = ImageTk.PhotoImage(glowa_img)
                canvas.itemconfig(glowa, image=glowa_photo)
            else:
                glowa_img = glowa_img_1.rotate(45)
                glowa_photo = ImageTk.PhotoImage(glowa_img)
                canvas.itemconfig(glowa, image=glowa_photo)
        if coordinates[0] >= 710:
            predkosc_X = -predkosc_X
            if predkosc_Y > 0:
                glowa_img = glowa_img_1.rotate(225)
                glowa_photo = ImageTk.PhotoImage(glowa_img)
                canvas.itemconfig(glowa, image=glowa_photo)
            else:
                glowa_img = glowa_img_1.rotate(135)
                glowa_photo = ImageTk.PhotoImage(glowa_img)
                canvas.itemconfig(glowa, image=glowa_photo)
        if coordinates[1] <= 0:
            predkosc_Y = -predkosc_Y
            if predkosc_X > 0:
                glowa_img = glowa_img_1.rotate(315)
                glowa_photo = ImageTk.PhotoImage(glowa_img)
                canvas.itemconfig(glowa, image=glowa_photo)
            else:
                glowa_img = glowa_img_1.rotate(225)
                glowa_photo = ImageTk.PhotoImage(glowa_img)
                canvas.itemconfig(glowa, image=glowa_photo)
        if coordinates[1] >= 710:
            predkosc_Y = -predkosc_Y
            if predkosc_X > 0:
                glowa_img = glowa_img_1.rotate(45)
                glowa_photo = ImageTk.PhotoImage(glowa_img)
                canvas.itemconfig(glowa, image=glowa_photo)
            else:
                glowa_img = glowa_img_1.rotate(135)
                glowa_photo = ImageTk.PhotoImage(glowa_img)
                canvas.itemconfig(glowa, image=glowa_photo)
        canvas.move(glowa, predkosc_X, predkosc_Y)
        stare_okno.update()
        time.sleep(0.01)
    stare_okno.mainloop()


def zaloguj_sie(session, ikonka_dla_okienka, okienko_logowania, login_entry, haslo_entry, info_label):
    login_1 = login_entry.get()
    haslo_1 = haslo_entry.get()
    try:
        sprawdzenie = session.query(Dane_do_logowania).filter(
            Dane_do_logowania.login == login_1).one()
        if sprawdzenie.haslo == haslo_1:
            uzytkownik.uzytkownik(session, ikonka_dla_okienka, okienko_logowania, login_1)
        else:
            info_label.place(x=320, y=400)
            info_label.config(text='podałeś błędne hasło')
    except BaseException:
        info_label.place(x=250, y=400)
        info_label.config(text='użytkownik o danym loginie nie istnieje')


def wyloguj_sie(stare_okno, nowe_okno):
    nowe_okno.withdraw()
    stare_okno.deiconify()
    stare_okno.mainloop()


def wypelnianie_rankingu(session, listbox):
    lista_recordy = []
    lista_loginy = []
    for rekord in session.query(Informacje):
        lista_recordy.append(rekord.record)
        lista_loginy.append(rekord.login)
    lista = [lista_loginy, lista_recordy]
    for i in lista:
        print(i)
    print(lista[0][1])
    print(len(lista))
    quicksort(lista, 0, len(lista[0])-1)
    lista[0].reverse()
    lista[1].reverse()
    for i in lista:
        print(i)
    x = 1
    while x <= len(lista[0]):
        listbox.insert(x, '   ' + str(lista[0][x-1])+'  '+str(lista[1][x-1]))
        print(x)
        x = x+1


def quicksort(lista, lewy, prawy):
    i = int((lewy + prawy) / 2)
    piwot = lista[1][i]
    piwot_login = lista[0][i]
    lista[1][i] = lista[1][prawy]
    lista[0][i] = lista[0][prawy]
    j = lewy
    i = lewy
    while i < prawy:
        if lista[1][i] < piwot:
            # print(i)
            # print(j)
            pomocnicza = lista[1][i]
            pomocnicza_2 = lista[0][i]
            lista[0][i] = lista[0][j]
            lista[0][j] = pomocnicza_2
            lista[1][i] = lista[1][j]
            lista[1][j] = pomocnicza
            j = j+1
        i = i+1

    lista[0][prawy] = lista[0][j]
    lista[1][prawy] = lista[1][j]
    lista[1][j] = piwot
    lista[0][j] = piwot_login
    if lewy < j - 1:
        quicksort(lista, lewy, j - 1)
    if j + 1 < prawy:
        quicksort(lista, j + 1, prawy)


def rejestracja(session, login_entry, haslo_entry, haslo_again_entry, informacja_label, ikonka_dla_okienka,
                okinko_rejestracji):
    login_1 = login_entry.get()
    haslo_1 = haslo_entry.get()
    haslo_2 = haslo_again_entry.get()
    # print(len(login_1))
    if len(login_1) < 5:
        informacja_label.config(text='login jest za krótki')
    elif len(login_1) > 15:
        informacja_label.config(text='login jest za długi')
    elif len(haslo_1) < 5:
        informacja_label.config(text='haslo jest za krótkie')
    elif len(haslo_1) > 15:
        informacja_label.config(text='haslo jest za długie')
    elif haslo_1 != haslo_2:
        informacja_label.place(x=320, y=460)
        informacja_label.config(text='podano dwa różne hasła')
    else:
        try:
            session.add(Dane_do_logowania(login=login_1, haslo=haslo_1))
            session.add(Informacje(login=login_1, record=0, games_played=0))
            session.commit()
            uzytkownik.uzytkownik(session, ikonka_dla_okienka, okinko_rejestracji, login_1)
            informacja_label.config(text='udało się zarejestrować uzytkownika')
        except BaseException:
            informacja_label.place(x=275, y=460)
            informacja_label.config(text='uzytkownik o danym loginie istnieje')


def rekord(session, login_1):
    rekord_1 = session.query(Informacje).filter(
        Informacje.login == login_1).one()
    return str(rekord_1.record)


def games_played(session, login_1):
    games_played_1 = session.query(Informacje).filter(
        Informacje.login == login_1).one()
    return str(games_played_1.games_played)
