#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 10, 2014

@author: anroco

How left justify a string in python?

¿Como justificar a la izquierda un string en python?
'''

#create a str
s = 'many years later'
print(s)

#generates a string of length defined, where is left justified the string 's'.
s_left = s.ljust(30)
print(s_left)

#can specify the padding character
s_left = s.ljust(30, '-')
print(s_left)
