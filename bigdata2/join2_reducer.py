#!/usr/bin/env python
import sys
flag = False		#true if the line has no number
curr_tot_count = 0      #initialize the total count of current show
prev_tv_show = ""       #record the previous show

for line in sys.stdin:
    line = line.strip()
    key_value = line.split('\t')
    curr_tv_show = key_value[0]		#record the current show
    value = key_value[1]		#recour the current value of the current show

    if prev_tv_show != curr_tv_show : 	#check when the show differs between the previous and current show
    	if flag :			#true if the show is from ABC, then print, clear flag and curr_tot_count	
	    print('{0} {1}'.format(prev_tv_show, curr_tot_count))
        flag = False
        curr_tot_count = 0
    
    prev_tv_show = curr_tv_show		#record the previous show for the use in the next running
    
    if value.isdigit():			#ture if the line doesn't contain ABC
        curr_tot_count += int(value)    #add the current value into the total count
    else:
        flag = True			#find the ABC and be ready to print in the next running	

