#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma-cyfry.py
#  
# Napisz program, kt�ry sumuje cyfry podanej liczby (minimum dwucyfrowej)
# i wy�wietla ich sum� w terminalu.
#

def sumuj_cyfry1(liczba):
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba = int(liczba / 10)
    return suma
    
def sumuj_cyfry2(liczba):
    suma = 0
    for cyfra in str(liczba):
        suma += int(cyfra)
    return suma


def main(args):
    
    liczba = input("Podaj liczb� 2-cyfrow�: ")
    liczba = int(liczba)
    
    while liczba < 10:
        liczba = input("Podaj liczb� 2-cyfrow�: ")
        liczba = int(liczba)
        
    
    print("Suma: ", sumuj_cyfry2)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
