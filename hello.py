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
__version__="0.1.3"
__author__= "Ana Paula"
__license__= "Unlicense"


import os
import sys

arguments = {
    'lang': None,
    'count':1,
}
for arg in sys.argv[1:]:
    # TO DO: Tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option {key}")
        sys.exit()
    arguments[key] = value
    
#Dunder =  tem dois underlines inicio e fim
current_language = arguments ["lang"]
if current_language is None:
     current_language = os.getenv("LANG")
     # TODO: Usar repetição
     if current_language is None:
            current_language = input("Choose a language:")

current_language = current_language[:5]
# snake case = current_language
# Pascal Case = Current_Language

msg = {
    "en_US": "Hello World!",
    "pt_BR": "Olá Mundo!",
    "it_IT": "Ciao Mondo!",
    "es_SP": "Hola Mundo!",
    "fr_FR": "Bonjour,Monde!",
}

print(msg[current_language] * int(arguments["count"]))
