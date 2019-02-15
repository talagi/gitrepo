#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kodmorsea.py
#  

kod = {
        'a':'+-',
        'ą':'+-+-',
        'b':'-+++',
        'c':'-+-+',
        'ć':'-+-++',
        'd':'-++',
        'e':'+',
        'ę':'++-++',
        'f':'++-+',
        'g':'--+',
        'h':'++++',
        'i':'++',
        'j':'+---',
        'k':'-+-',
        'l':'+-++',
        'ł':'+-++-',
        'm':'--',
        'n':'-+',
        'ń':'--+--',
        'o':'---',
        'ó':'---+',
        'p':'+--+',
        'r':'+-+',
        's':'+++',
        'ś':'+++-+++',
        't':'-',
        'u':'++-',
        'w':'+--',
        'z':'--++',
        'ź':'--++-',
        'ż':'--++-+',
        ' ':' '
    }

def koduj(tekst):
    tekst = input("Podaj tekst: ").lower()
    print("".join([kod[1] for 1 in tekst]))
    
    #for l in tekst:
        # print(kod[1])

def dekoduj():
    tekst = []
    lit = ' '
    klucze = list(kod.values())
    litery = list(kod.keys())
    
    while lit > '':
        lit = input('Podaj kod Morsea: ')
        tekst.sppend(lit)
    
    for i in tekst:
        print(litery[klucze.index(i)]

def main(args):
    dekoduj()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
