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
    egz_hum = DecimalField(default=0) 
    egz_mat= DecimalField(default=0) 
    egz_jez = DecimalField(default=0) 
    
class Przedmiot(BazaModel):
    przedmiot = CharField(null=False)
    imie_naucz = CharField(null=False)
    nazwisko_naucz = CharField(null=False)
    plec_naucz = BooleanField()
    
class Ocena(BazaModel):
    data = DateField()
    uczen = ForeignKeyField(Uczen, related_name='oceny')
    przedmiot = ForeignKeyField(Przedmiot, related_name='oceny')
    ocena = IntegerField(default=0)




def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()
    baza.create_tables([Klasa, Uczen, Przedmiot, Ocena])
    
    kl1 = Klasa(nazwa='2A', roknaboru = 2012, rokmatury = 2015)
    kl1.save()
    
    kl2a = Klasa.select().where(Klasa.nazwa == '2A').get()
    u1 = Uczen(imie = 'Jan', nazwisko = 'Kowalski', plec = False, klasa = kl2a)
    u1.save()
    
    p1 = Przedmiot(przedmiot = 'fizyka', imie_naucz = 'Kuba', nazwisko_naucz = 'Kowalski', plec_naucz = False)
    p1.save()
    
    o1 = Ocena(data = '12-12-2015', uczen = u1, przedmiot = p1, ocena = 2)
    o1.save()
    
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
