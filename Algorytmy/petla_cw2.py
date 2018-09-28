#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla_cw2.py
#
# DANE WEJŚCIOWE:
# początek i koniec przedziału podanego przez użytkownika
# DANE WYJŚCIOWE:
# liczby naturalne z <start, stop>


def main(args):
    start = int(input("Przedzial lewy: "))
    stop = int(input("Przedzial prawy: "))
    
    for liczba in range(start, stop + 1):
        print(liczba, " ", end='')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
