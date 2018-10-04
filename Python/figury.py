#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py
#  
# Program buduje wypełniony prostokąt o bokach podanych przez 
# użytkownika za pomocą podanego znaku  

def prostokat1(a, b, znak):
    
    a = int(input("Pierwszy bok: "))
    b = int(input("Drugi bok: "))
    c = int(input("Znak wypełnienia: "))

    for i in range(a):
        for j in range(b):
            print(c, end='')
        print()
        
def prostokat2(a, b, znak):
    
    for i in range(a):
        for j in range(b):
            if i 
            if j == 0 or j == b - 1:
                print(c, end='')
            else:
                print(" ", end='')
        print()


def main(args):
    
    a = int(input("Pierwsza liczba: "))
    b = int(input("Druga liczba: "))
    
    for i in range(a):
        for j in range(b):
            print('#', end='')
        print()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
