#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  szablon.py

def dodaj():
    print(a + b)

def main(args):
    # a = 0 # inicjacja zmiennej
    a = int(input('Podaj 1. liczbę: '))
    print(a)
    b = int(input('Podaj 2. liczbę: '))
    print(b)
    
    dodaj()
    
    print("Suma: ", a + b)
    print("Różnica: ", a - b)
    print("Iloczyn: ", a * b)
    print("Iloraz: ", a / b)
    
    return 0
    
# Duck typing

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
