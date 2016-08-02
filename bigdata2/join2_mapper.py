#!/usr/bin/env python
import sys

for line in sys.stdin:
    line       = line.strip()   #strip out carriage return
    key_value  = line.split(",")   #split line, into key and value, returns a list
    value_in   = key_value[1]   #value is 2nd item 
    key_in     = key_value[0]   #key is the 1st item

    #print <key_in key_out>
    if  (value_in.isdigit() or value_in == 'ABC'):   #if this entry contains number or equals ABC
        print( '%s\t%s' % (key_in, value_in) )  #print show with the number viewers 

