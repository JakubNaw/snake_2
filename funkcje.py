
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from functools import partial
from tkinter import *
baza = declarative_base()
class Dane_do_logowania(baza):
    __tablename__ = 'dane_do_logowania'
    login = db.Column(db.String(100),primary_key=True)
    haslo = db.Column(db.String(100))

def czytaj_dane_do_logowania(session):
    for dane in session.query(Dane_do_logowania):
        print(dane.login, dane.haslo)
    print()