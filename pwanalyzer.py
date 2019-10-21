# -*- coding: UTF-8 -*-

#compara primer archivo en ARGV con diccionarios de texto

import sys,os

file1= sys.argv[1]
dicsdir = '-dics-'

file1 = open(file1,'r')
file = []
for i in file1:
	file.append(i.rstrip())
file1 = file

for dic in os.listdir(dicsdir):
	cont = 0
	file2 = open(os.path.join(dicsdir,dic),'r')
	file = []
	for i in file2:
		file.append(i.rstrip())
	file2 = file
	with open ("output.txt", "w") as out_file:
				print("\n\n*** DICCIONARIO : "+dic+"\n")
				
				for line in file1:
					
					if line in file2:
						print("Found : "+line)
						out_file.write(line)
						cont += 1
	print ("* Found Passwords : "+str(cont))