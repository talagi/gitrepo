#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wej-wyj.py
#  
def name ():
    name = input("Podaj swoje imię: ")
    surname = input("Podaj swoje nazwisko: ")
    
    print("Witaj" + " " + name + " " + surname)

def main(args):
    
    name()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
