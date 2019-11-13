# pwanalyzer & pwchecker

A Python way to avoid weak passwords via corporate policy and forbidden words dictionary (PWCHECKER). This also includes an script to validate our full password list to compare to common brute force dictionaries, returning ocurrences and percentages.

You can insert most popular big pw dictionary ROCKYOU.txt and add to -dics- folder:

Link: https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt

This project is based on 2 ideas:
  - send the pw list (obviously decrypted) to compare some dictionaries: pwanalyzer.py
  - send a password to corporate policy and dictionary to get valid or not result: pwchecker.py
  
pwanalyzer.py

USAGE python pwanalyzer.py [password_file]

RETURNS: Number of ocurrences of entries on password file on each dictionary file, with percentages.

pwchecker.py

USAGE python pwchecker.py [password] [dictionary_forbidden_passwords_file]

RETURNS: Exit code 0 or 1 (independant windows or linux)
