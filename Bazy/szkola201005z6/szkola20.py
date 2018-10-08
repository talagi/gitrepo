#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import csv


def dane_z_pliku(nazwa_pliku):
    dane = []  # pusta lista na dane
    with open(nazwa_pliku, newline='', encoding='utf-8') as plik:
        tresc = csv.reader(plik, delimiter=';')
        for rekord in tresc:
            rekord = [x.strip() for x in rekord]  # usunięcie białych znaków
            dane.append(rekord)  # dodawanie rekordów do listy
    return dane


def main(args):
    nazwa_bazy = 'szkola20'
    con = sqlite3.connect(nazwa_bazy + '.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora

    # utworzenie tabeli w bazie
    with open(nazwa_bazy + '.sql', 'r') as plik:
        cur.executescript(plik.read())  # tworzenie tabel w bazie

    # dodawanie danych do bazy
    dane = dane_z_pliku('szkoła_z6pr052010_uczniowie.txt')
    print(dane)
    dane.pop(0)  # usuwanie pierwszego elementu listy
    cur.executemany(
        'INSERT INTO Uczniowie VALUES(?, ?, ?, ?, ?, ?)', dane)

    # dodawanie danych do bazy
    dane = dane_z_pliku('szkoła_z6pr052010_oceny.txt')
    print(dane)
    dane.pop(0)  # usuwanie pierwszego elementu listy
    cur.executemany(
        'INSERT INTO Oceny VALUES(?, ?, ?, ?)', dane)

    # dodawanie danych do bazy
    dane = dane_z_pliku('szkoła_z6pr052010_przedmioty.txt')
    print(dane)
    dane.pop(0)  # usuwanie pierwszego elementu listy
    cur.executemany(
        'INSERT INTO Przedmioty VALUES(?, ?, ?, ?)', dane)


    con.commit()  # zatwierdzenie zmian w bazie
    con.close()
    return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
