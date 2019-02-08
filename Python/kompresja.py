#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kompresja.py
#  


def main(args):
    Vk = input('Podaj rozmiar danych skompresowanych (Bajty): ')
    Vnk = input('Podaj rozmiar danych nieskompresowanych (Bajty): ')
    Rc = int(Vk) / int(Vnk) * 100
    R2c = (1 - int(Vk) / int(Vnk)) * 100
    print('O ile zmniejszyły się dane: ', R2c)
    print('Współczynnik kompresji: ', Rc)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
