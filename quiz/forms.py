#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# forms.py

from flask_wtf import FlaskForm
from wtforms import HiddemField, StringField, BooleanField, SelectField
from wtforms import FormField, FieldList

blad1='To pole jest wymagane'

class OdpForm(FlaskForm):
    id = HiddenField()
    pytanie = HiddenField()
    odpowiedz = StringField('Odpowiedz:', validators=[Required(message=blad1)])
    odpok = BooleanField('Poprawna:')
    
class DodajForm(FlaskForm):
    pytanie = StringField('Tresc pytania:', validators=[Required(message=blad1)])
    kategorie = SelectField('Kategoria', coerce=int)
    odpowiedzi = FieldList(FormField(OdpForm), min_entries=3)
    id = HiddenField()
