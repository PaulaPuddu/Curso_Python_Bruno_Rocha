#!/ usr/bin/.env python3

import os
import sys

# EAFP  - Easy to ask Forgiveness than permission

try: 
    names = open("names.txt").readlines() # FileNotFoundError
except FileNotFoundError as e:
    print(f" {str(e)}.")
    sys.exit(1)
    # TODO usar retry
else:
    print("Sucesso!!!")


try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)
