#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  klasa_uczen.py
#  
import os
from peewee import * 

baza_plik = 'test_orm.db'

################# MODEL
baza = SqliteDatabase(baza_plik)
class BazaModel(Model):
    class Meta:
        database = baza
        
class Klasa(BazaModel):
    nazwa = CharField(null=False)
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)
    
class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')
    
class Wynik(BazaModel):
    egz_hum = DecimalField(default=0) 
    egz_mat= DecimalField(default=0) 
    egz_jez = DecimalField(default=0) 
    uczen = ForeignKeyField(Uczen, related_name='wyniki')




def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()
    baza.create_tables([Klasa, Uczen, Wynik])
    
    kl1 = Klasa(nazwa='2A', roknaboru = 2012, rokmatury = 2015)
    kl1.save()
    kl1 = Klasa(nazwa='1A', roknaboru = 2011, rokmatury = 2014)
    kl1.save()
    kl1 = Klasa(nazwa='3A', roknaboru = 2010, rokmatury = 2013)
    kl1.save()
    
    kl2a = Klasa.select().where(Klasa.nazwa == '2A').get()
    u1 = Uczen(imie = 'Jan', nazwisko = 'Kowalski', plec = False, klasa = kl2a)
    u1.save()
    kl3a = Klasa.select().where(Klasa.nazwa == '3A').get()
    u1 = Uczen(imie = 'Kuba', nazwisko = 'Kowalski', plec = False, klasa = kl3a)
    u1.save()
    kl1a = Klasa.select().where(Klasa.nazwa == '1A').get()
    u1 = Uczen(imie = 'Agnieszka', nazwisko = 'Talaga', plec = False, klasa = kl1a)
    u1.save()
    
    uczniowie = Uczen.select()
    for uczen in uczniowie:
        print(klasa.nazwa, klasa.roknaboru, klasa.rokmatury)
        
    klasy = Klasa.select()
    for klasa in klasy:
        print(uczen.id, uczen.imie, uczen.nazwisko)
    
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
