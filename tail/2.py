#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
from sys import argv
import itertools
import time

def printFiles(line_count,f,lines):
    i=lines-line_count
    lc=-1
    for line in f:
         lc+=1
         if lc>=i and lc<=lines:
              print line

def openFiles(f_data):
	global file1
	try:    
		file1 = open(f_data)
   	except IOError: 
		print "boyle bir dosya bulunmamaktadir",f_data	

def countLine(file_name):
	lines_counter = 0
	for line in file_name:
		if line != '\n':
			lines_counter += 1
	file_name.seek(0)
	return lines_counter

if len(sys.argv)==2:
	script, file_name= argv
	openFiles(file_name)
	lines=countLine(file1)
	printFiles(10, file1,lines)

elif len(sys.argv)==3:	
	script,option,file_name= argv
	if option=="-f":
		openFiles(file_name)
		lines=countLine(file1)
		printFiles(10, file1,lines)	
		
		while True:
		    line = file1.readline()
		    if not line:
			time.sleep(1)
		    else:
			print line
	else:
		print "yanlis opsiyon veya rakam girdiniz"

elif len(sys.argv)==4:	
	script,option,line_num,file_name= argv
	if option=="-n" and line_num.isdigit():
		openFiles(file_name)
		lines=countLine(file1)
		printFiles(int(line_num), file1,lines)
	else:
		print "yanlis opsiyon veya rakam girdiniz"
		

else:
	print "dogru arguman sayısı giriniz"
	
