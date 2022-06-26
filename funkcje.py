import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from functools import partial
from tkinter import *
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
