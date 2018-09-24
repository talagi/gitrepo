#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trojkat.py
#  

def trojkat(a, b, c):
    """
    Funkcja bada możliwość zbudowania trójkąta z trzech podanych boków
    Funkcja zwraca True jeśeli się da, False w przeciwnym wypadku
    """
    
    if a + b > c and a + c > b and b + c > a:
       return True
       
    return False
    


def main(args):
    assert(trojkat(3, 4, 5) == True)
    assert(trojkat(3, 4, 1) == False)
    
    
    # ~a = int(input('Podaj 1. liczbę: '))
    # ~print(a)
    # ~b = int(input('Podaj 2. liczbę: '))
    # ~print(b)
    # ~c = int(input('Podaj 3. liczbę: '))
    # ~print(c)

    # ~if trojkat(a, b, c):
        # ~print("Da się")
    # ~else:
        # ~print("Nie da się")
        
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
