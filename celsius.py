#!/usr/bin/env python
# -*- coding: utf8 -*-
# Datum:   Thu Nov  8 08:47:59 2012
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   Program na převod °C -> °F
################################################################

start = input('od: ')
stop  = input('do: ')
krok = input('krok:')

F=start
while F<=stop :
    C = 5.*(F-32)/9.
#   print F, u'°F = ', C, u'°C'
    print u"{1:7.2f}°F = {0:7.2f}°C".format(C,F)
    F = F+krok
    
"""
http://docs.python.org/2.7/library/string.html#formatstrings
"""
print 'Zkouším str.format()...'  
print '###########################'  
print 20/7
print "|{0:<-20d}|".format(17)  # dekadické
print "|{0:^+20x}|".format(-17)  # hexadecimální
print "|{0:020b}|".format(-17)  # dvojkové

print "%2f" % 17

