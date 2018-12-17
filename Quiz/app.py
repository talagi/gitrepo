#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  app.py
# 
# http:// - protokół
# lo1.sandomierz.pl - 
# /


from flask import g
from modele import *
from views import *


@app.before_request
def before_request():
    g.db = baza
    g.db.connect()
    
@app.after_request
def after_request(response):
    g.db = baza
    return response


if __name__ == '__main__':
    app.run(debug=True)
