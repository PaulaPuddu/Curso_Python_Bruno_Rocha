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

msg = {
    "en_US": "Hello World!",
    "pt_BR": "Olá Mundo!",
    "it_IT": "Ciao Mondo!",
    "es_SP": "Hola Mundo!",
    "fr_FR": "Bonjour,Monde!",
}

# Set implementa (Hash Table) velocidade de O(1) - constante acesso direto - Otimiza a busca

# Ordem de complexidade O(n) - Ordem de elementos que se precisa pesquisar

#O(1) velocidade constante
print(msg[current_language]) #built- in - ja vem prontinho no python
