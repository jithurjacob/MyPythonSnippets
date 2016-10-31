#!/usr/bin/python
# -*- coding: utf-8 -*-
import string
n = int(raw_input())
for t in range(0, n):
    keyw = [ch for ch in raw_input()]
    keyw_temp = list(keyw)
    key = set()
    ciph = [ch for ch in raw_input()]
    for x in keyw:
        key.add(x)
    keyw.reverse()
    #print keyw
    for i in keyw:
        if(keyw.count(i)>1):
            keyw.remove(i)
    keyw.reverse()
    #print keyw
    keyz = list(key)
    keyz.sort()
    alph=[' ']
    for x in string.ascii_uppercase:
        alph.append(x)
        if x not in keyw:
            keyw.append(x)
    ckey=[' ']
    for j in keyz:
        for i in range(keyw.index(j),len(keyw), len(key)):
            ckey.append(keyw[i])
    #print ckey
    #print alph
    for i in range(0,len(ciph)):
        ciph[i]=alph[ckey.index(ciph[i])]
    print ''.join(ciph)
    
			
