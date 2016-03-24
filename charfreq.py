#!/usr/local/bin/python

from __future__ import division  #using exact div
import re
import string

freqDict = {}
for word in string.lowercase:   #create a void freq dict, key=a to z
    freqDict[word] = 0

fh = open('./a.txt','r')           #read_only
str = string.lower(fh.read())
fh.close()

total = 0
for l in str:
    if re.match("[a-z]",l):       #if l is a letter, count it
        freqDict[l] += 1
        total += 1

list = sorted(freqDict.iteritems(),key=lambda t:t[1],reverse=True) #sort out
for key,value in list:
    print "%s %6d %6.3f%%" %(key,value,100*value/total)

print "total = %d" %total
