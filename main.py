import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from functools import partial
from tkinter import *
import funkcje
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



menu_start.mainloop()