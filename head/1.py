#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
from sys import argv

#satir okunmasini saglar
def printFiles(line_count, f):
	a=0
	while a<int(line_count):
		print a+1, f.readline()
		a=a+1

#dosyanın acilmasini saglar saglar
def openFiles(f_data):
	global file1
	try:    
		file1 = open(f_data)
   	except IOError: 
		print "boyle bir dosya bulunmamaktadir",f_data	

if len(sys.argv)==2:
	script, file_name= argv
	openFiles(file_name)
	printFiles(10, file1)
	

elif len(sys.argv)==4:	
	script,option,line_num,file_name= argv
	if option=="-n" and line_num.isdigit():
		openFiles(file_name)
		printFiles(line_num, file1)
	else:
		print "yanlis opsiyon veya rakam girdiniz"
		

else:
	print "dogru arguman sayısı giriniz"
	
