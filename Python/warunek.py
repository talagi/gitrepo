#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  warunek.py
#  
def warunek():
    
    lista_liczb = []
    
    for i in range(3):
        liczba = float(input("Podaj liczbę"))
        lista_liczb.append(liczba)
    print(max(lista_liczb))


def main(args):
    
    warunek()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
