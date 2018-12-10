#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  app.py
# 
# http:// - protokół
# lo1.sandomierz.pl - 
# /


from flask import Flask
from flask import render_template
app = Flask(__name__)

# widok domyślny
@app.route("/")
def hello():
    return render_template('index.html')
    
@app.route("/strona")
def strona():
    return render_template('strona.html')


if __name__ == '__main__':
    app.run(debug=True)
