#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  minmax.py
#  

import random

def losuj(lista, ile, min=0, maks=100):
    lista = []
    for i in range(ile):
        lista.append(random.randint(min, maks))
    return lista

def minmax(lista):
    min = max = lista[0]
    lista.pop(0)  # usunięcie pierwszego elementu listy
    for liczba in lista:
        if liczba < min:
            min = liczba
        if liczba > max:
            max = liczba
    return min, max


def main(args):
    lista = losuj(50, 10, 90)
    min, max = minmax(lista)
    print("Min: {}, Max: {}".format(min, max))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
