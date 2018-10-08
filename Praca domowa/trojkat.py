#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trojkat.py
#

def main(args):

m = (h-1)*2
  for i in range(h-1, -1, -1):
      for j in range(m+1):
          if j < i or j > m-i:
              print(" ", end='')
          else:
              print("$", end='')
      print()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
