import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from functools import partial
from tkinter import *
import funkcje
import time
from PIL import ImageTk, Image
engine = db.create_engine("mysql://root:2002Madzia@localhost:3306/snake")
connection = engine.connect()
metadata = db.MetaData()
print("Success:", engine)#udalo sie polaczyc z baza danych
#utworznnie sesji
Session = sessionmaker(bind=engine)
session = Session()
funkcje.czytaj_dane_do_logowania(session)
funkcje.czytaj_informacje(session)
# tworzenie okna

menu_start = Tk()#tworzenie menu do logowania
ikona_dla_okienka = PhotoImage(file = "C:/Users/user/PycharmProjects/snake_2/window_icon.png")
menu_start.resizable(width = False , height= False) # ustawienie braku mozliwosci zmiany rozmiaru okna
menu_start.geometry("750x750")#wybieranie rozdzielczosci
menu_start.configure(bg='#76e95f', )#tlo okna ustawione na zielony kolorek
menu_start.title("SNAKE ")# ustwienie tytułu okienka
menu_start.iconphoto(False,ikona_dla_okienka)
predkosc_X=5
predkosc_Y=3
predkosc_X_1=5
predkosc_Y_1=3
canvas = Canvas(menu_start,width=750, height= 750,bg="#76e95f")
canvas.pack()
glowa_img_1 = Image.open("C:/Users/user/PycharmProjects/snake_2/window_icon.png")#tworzenie obrazu glowy
glowa_img = glowa_img_1.rotate(315)# przechyalnie obrazu o 315 stopni
glowa_photo = ImageTk.PhotoImage(glowa_img)#tworzenie photoimage z obruconego obrazu
glowa= canvas.create_image(30,26,image = glowa_photo, anchor=NW)
tlo_image = PhotoImage(file= "C:/Users/user/PycharmProjects/snake_2/zdjecie_w_tle.png")
tlo = canvas.create_image(150,0,image = tlo_image, anchor=NW)
start_button = Button(canvas, text = 'START',
                    font = ('Calibiri',25), background='white',
                    relief = RAISED,bd = 10,compound = "bottom",
                    )
start_button.place(x=320, y=450)
rankingi_button = Button(canvas, text = 'RANKINGI',
                    font = ('Calibiri',25), background='white',
                    relief = RAISED,bd = 10,compound = "bottom",
                    )
rankingi_button.place(x=294, y=540)

while True:
    coordinates = canvas.coords(glowa)
    if(coordinates[0]<=0 ):
        predkosc_X= -(predkosc_X)
        if (predkosc_Y > 0):
            glowa_img = glowa_img_1.rotate(315)
            glowa_photo = ImageTk.PhotoImage(glowa_img)
            canvas.itemconfig(glowa, image=glowa_photo)
        else:
            glowa_img = glowa_img_1.rotate(45)
            glowa_photo = ImageTk.PhotoImage(glowa_img)
            canvas.itemconfig(glowa, image=glowa_photo)
    if(coordinates[0]>=710):
        predkosc_X = -(predkosc_X)
        if(predkosc_Y>0):
            glowa_img = glowa_img_1.rotate(225)
            glowa_photo = ImageTk.PhotoImage(glowa_img)
            canvas.itemconfig(glowa, image=glowa_photo)
        else:
            glowa_img = glowa_img_1.rotate(135)
            glowa_photo = ImageTk.PhotoImage(glowa_img)
            canvas.itemconfig(glowa, image=glowa_photo)
    if (coordinates[1] <= 0 ):
        predkosc_Y = -(predkosc_Y)
        if (predkosc_X > 0):
            glowa_img = glowa_img_1.rotate(315)
            glowa_photo = ImageTk.PhotoImage(glowa_img)
            canvas.itemconfig(glowa, image=glowa_photo)
        else:
            glowa_img = glowa_img_1.rotate(225)
            glowa_photo = ImageTk.PhotoImage(glowa_img)
            canvas.itemconfig(glowa, image=glowa_photo)
    if ( coordinates[1] >= 710):
        predkosc_Y = -(predkosc_Y)
        if (predkosc_X > 0):
            glowa_img = glowa_img_1.rotate(45)
            glowa_photo = ImageTk.PhotoImage(glowa_img)
            canvas.itemconfig(glowa, image=glowa_photo)
        else:
            glowa_img = glowa_img_1.rotate(135)
            glowa_photo = ImageTk.PhotoImage(glowa_img)
            canvas.itemconfig(glowa, image=glowa_photo)
    canvas.move(glowa,predkosc_X,predkosc_Y)
    menu_start.update()
    time.sleep(0.01)
menu_start.mainloop()