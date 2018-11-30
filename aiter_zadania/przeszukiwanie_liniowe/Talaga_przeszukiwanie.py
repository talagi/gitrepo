#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Talaga_przeszukiwanie.py
#  
# 
import random


def wyp(szuk):
    for i in range(10):
        szuk.append((random.randint(0,50))
    print (szuk)

def main(args):
    
    szuk = []
    wyp(szuk)
    i = int(input("Podaj liczbę: "))
    
    for j in range(len(szuk)):
        if szuk.cout(i) == 0 or i > 51:
            print("Element nieznaleziony")
            i += 1
            return
        else:
            print("Element znaleziony")
            return

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
