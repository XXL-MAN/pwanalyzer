# -*- coding: UTF-8 -*-

#compara primer archivo en ARGV con diccionarios de texto

import sys,os

file1= sys.argv[1]
dicsdir = '-dics-'

file1 = open(file1,'r')
file = []
results = []
for i in file1:
	file.append(i.rstrip())
file1 = file
entradas = len(file1)

results.append("\n\n\n* Numero de registros de entrada : "+str(entradas))


for dic in os.listdir(dicsdir):
	cont = 0
	file2 = open(os.path.join(dicsdir,dic),'r')
	file = []
	for i in file2:
		file.append(i.rstrip())
	file2 = file
	results.append("\n\n*** DICCIONARIO : "+dic+"\n")
	"""
	print ("* Numero1 : "+str(len(file1)))
	print ("* Numero2 : "+str(len(file2)))	
	print file1
	print file2
	"""
	for line in file1:				
			#cortar por los :
			if ":" in line:
				line = line.split(":")[1]
			
			if line in file2:
						print("Found : "+line+"\n")
						cont += 1
	results.append("* Found Passwords : "+str(cont))
	
	
	cont = (cont*100)/entradas
	results.append("* Percentage	  : "+str(cont)+"%")
	
for i in results:
		print i