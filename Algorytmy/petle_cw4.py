#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petle_cw4.py


def main(args):
	
	for a in range(10, 101):
		if a %2 ==0 and a %3 == 0:
			print (a)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
