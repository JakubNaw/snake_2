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
