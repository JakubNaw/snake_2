import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from tkinter import *
from PIL import ImageTk, Image
import time
baza = declarative_base()
# tworzenie modeli
class Dane_do_logowania(baza):
    __tablename__ = 'dane_do_logowania'
    login = db.Column(db.String(100),primary_key=True)
    haslo = db.Column(db.String(100))
class Informacje(baza):
    __tablename__ = 'informacje'
    login = db.Column(db.String(100),primary_key=True)
    record = db.Column(db.Integer)
    games_played = db.Column(db.Integer)


#funkcje
def czytaj_dane_do_logowania(session):
    for dane in session.query(Dane_do_logowania):
        print(dane.login, dane.haslo)
    print()
def czytaj_informacje(session):
    for informacje in session.query(Informacje):
        print(informacje.login, informacje.record, informacje.games_played)
    print()
def powrot(stare_okno, nowe_okno,canvas,glowa):
    # funnkcja powrotu do bylego okna
    nowe_okno.withdraw()
    stare_okno.deiconify()
    predkosc_X = 5
    predkosc_Y = 3
    glowa_img_1 = Image.open("C:/Users/user/PycharmProjects/snake_2/window_icon.png")  # tworzenie obrazu glowy
    glowa_img = glowa_img_1.rotate(315)  # przechyalnie obrazu o 315 stopni
    glowa_photo = ImageTk.PhotoImage(glowa_img)  # tworzenie photoimage z obruconego obrazu
    while True:
        coordinates = canvas.coords(glowa)
        if (coordinates[0] <= 0):
            predkosc_X = -(predkosc_X)
            if (predkosc_Y > 0):
                glowa_img = glowa_img_1.rotate(315)
                glowa_photo = ImageTk.PhotoImage(glowa_img)
                canvas.itemconfig(glowa, image=glowa_photo)
            else:
                glowa_img = glowa_img_1.rotate(45)
                glowa_photo = ImageTk.PhotoImage(glowa_img)
                canvas.itemconfig(glowa, image=glowa_photo)
        if (coordinates[0] >= 710):
            predkosc_X = -(predkosc_X)
            if (predkosc_Y > 0):
                glowa_img = glowa_img_1.rotate(225)
                glowa_photo = ImageTk.PhotoImage(glowa_img)
                canvas.itemconfig(glowa, image=glowa_photo)
            else:
                glowa_img = glowa_img_1.rotate(135)
                glowa_photo = ImageTk.PhotoImage(glowa_img)
                canvas.itemconfig(glowa, image=glowa_photo)
        if (coordinates[1] <= 0):
            predkosc_Y = -(predkosc_Y)
            if (predkosc_X > 0):
                glowa_img = glowa_img_1.rotate(315)
                glowa_photo = ImageTk.PhotoImage(glowa_img)
                canvas.itemconfig(glowa, image=glowa_photo)
            else:
                glowa_img = glowa_img_1.rotate(225)
                glowa_photo = ImageTk.PhotoImage(glowa_img)
                canvas.itemconfig(glowa, image=glowa_photo)
        if (coordinates[1] >= 710):
            predkosc_Y = -(predkosc_Y)
            if (predkosc_X > 0):
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