#!/usr/bin/python
#-*- coding:utf-8 -*-

import re
import sys
from sys import argv
import time

script, file_name= argv

METHOD_AS_RE = 'GET |POST |DELETE |HEAD |OPTIONS |PUT |\?| HTTP|\n'

try:    
	fdata = open(file_name)
except IOError: 
	print "boyle bir dosya bulunmamaktadir",file_name

log={}
utime={}

for line in fdata:
		url=re.split(METHOD_AS_RE,line)[1]
		timestring = re.split(' ~ |\n',line)[1]
		if not timestring=="-":
			time=float(timestring)
		else:
			time=None		
	
		log[url] = log.get(url,0) + 1
		if time>utime.get(url, 0):
			utime.update({url: time})

max_requested_url=max(log, key=log.get)
max_requested_url_num=log[max_requested_url]
most_time_consuming_url=max(utime, key=utime.get)
most_time_consuming_url_time=utime[most_time_consuming_url]
print "*"*75
print "Most requested url is %s and number of its request is %s" %(max_requested_url,max_requested_url_num)
print "The number of distinct url is %s" %len(log)
print "Most time consuming url is %s and its time is %s" %(most_time_consuming_url,most_time_consuming_url_time)
print "*"*75
