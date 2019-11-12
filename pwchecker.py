# -*- coding: UTF-8 -*-
# Andres Naranjo @TheXXLMAN - ElevenPaths 2019

# compara una cadena de texto como argumento 1 contra la política de contraseñas
# #especificada y el archivo de contraseñas prohibidas en arg.2

import sys  # ,os

# PASSWORD POLICY DEFINITION contants

MINLENGHT    = 8  # min password lenght
MAXLENGHT    = 25  # max password lenght
NUMCHARS     = True  # numeric characters
UPPERCHARS   = True  # UPPERCASE characters
LOWERCHARS   = True  # Lowercase characters
SPECIALCHARS = True  # Special chars (below list) in password
SpecialSym = ['$', '@', '#', '%']  # list of special chars, edit to add more


# Password validation in Python
# Function to validate the password 
def password_check(passwd):
    val = True

    if len(passwd) < MINLENGHT:
        print('Password length should be at least ' + str(MINLENGHT))
        val = False

    if len(passwd) > MAXLENGHT:
        print('Password length should be not be greater than ' + str(MAXLENGHT))
        val = False

    if NUMCHARS == True:
        if not any(char.isdigit() for char in passwd):
            print('Password should have at least one numeral')
            val = False
    if UPPERCHARS == True:
        if not any(char.isupper() for char in passwd):
            print('Password should have at least one uppercase letter')
            val = False

    if LOWERCHARS == True:
        if not any(char.islower() for char in passwd):
            print('Password should have at least one lowercase letter')
            val = False

    if SPECIALCHARS == True:
        if not any(char in SpecialSym for char in passwd):
            print('Password should have at least one of the symbols : '),
            for i in SpecialSym:
                print i,
            val = False
    if val:
        return val

try:
    passwd = sys.argv[1]
    dic = sys.argv[2]
except:
    print("USAGE python pwchecker.py [password] [dictionary_forbidden_passwords_file]")
    sys.exit(2)


file1 = open(dic,'r')
file = []
results = []
for i in file1:
	file.append(i.rstrip())
dic = file

if password_check(passwd) and (not passwd in file):
	sys.exit(0)
else:
	sys.exit(1)
	
#print(password_check(passwd))
