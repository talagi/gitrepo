#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczby23.py
#  
#  
def liczby2():
    """
    Funkcja drukuje wszystkie liczby dwucyfrowe, w których cyfry nie
    powtarzają się. Funkcja zwraca ich liczbę. 
    Wykluczone liczby: 11, 22, 33 itd.
    """
    ile = 0 # licznik
    for i in range(1, 10):
        for j in range(0, 10):
            if i != j:
                print("{}{} ".format(i, j), end='') 
                ile = ile + 1
    return ile 

    
def liczby3():
    """
    Funkcja drukuje wszystkie liczby trzycyfrowe, w których cyfry nie
    powtarzają się. Funkcja zwraca ich liczbę. 
    Wykluczone liczby: 111, 222, 333 itd.
    """


def main(args):
    print("Liczb 2-cyfrowych:", liczby2())
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
