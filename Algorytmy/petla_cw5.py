#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla_cw2.py
#
# DANE WEJŚCIOWE:
# liczby dodatnie podawane przez użytkownika
# DANE WYJŚCIOWE:
# suma liczb podawanych przez użytkownika
# program musi zapewnić poprawność danych,
# program kończy działanie po wprowadzeniu wartości 0

def pobierzMiesiac():
    
    nazwy = ['', 'styczeń', 'luty', 'marzec'. 'kwiecień', 'maj', 'lipiec', 'sierpień','wrzezsień', 'październik'
    
    
    pass


def main(args):
    
    suma = 0 
    liczba = 1
    
    while liczba != 0:
        liczba = int(input("Podaj liczbę: "))
        while liczba < 0:  # pętla zaporowa
            liczba = int(input("Błędne dane! Podaj liczbę: "))
        suma += liczba
    print("Suma", suma)
        
    
    return 0
    
def main2(args):
    
    suma = 0 
    liczba = 1
    
    while liczba != 0:
        liczba = int(input("Podaj liczbę: "))
        if liczba < 0:  # pętla zaporowa
           print("Błędne dane! ", end='')
        else:
            suma += liczba
    print("Suma", suma)
        
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(pobierzMiesiac(sys.argv))
