#! =/usr/bin/env python3 (sheebang)
"""Hello World Multi-languages

Depending on language configurated, the program will show a correspondent 
message

Usage:

Lang variable duly configurated 

    export LANG=pt_BR

Execution

    python3 hello.py
    ou ./hello.py
"""
__version__="0.0.1"
__author__= "Ana Paula"
__license__= "Unlicense"


import os
#Dunder =  tem dois underlines inicio e fim
current_language = os.getenv("LANG", "en_US")[:5]
# snake case = current_language
# Pascal Case = Current_Language
msg = "Hello,World!"

if current_language =="pt_BR":
    msg = "Ola, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"    

print(msg) #built- in - ja vem prontinho no python
