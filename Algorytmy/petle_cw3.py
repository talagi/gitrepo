#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petle_cw3.py
#  

def main(args):
	kwa = 0
	a = int(input("Podaj: "))
	
	for x in range(a+1):
		kwa = a*a
		print(kwa)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
