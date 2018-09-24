#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petlafor.py
#  

def main(args):
    a = int(input('Start: '))
    b = int(input('Stop: '))
    
    while a >= b:
        b = int(input("Blędny zakres"))
    
    for liczba in range(a, b + 1):
        if liczba % 2 == 0:
            print(liczba)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
