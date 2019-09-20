#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla.py
#  
import random

def petla():
    max_quantity = 5
    lista_liczb = []
    
    for i in range(max_quantity):
        lista_liczb.sppend(random.radint(1,30))
    print(lista_liczb)


def main(args):
    
    petla()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
