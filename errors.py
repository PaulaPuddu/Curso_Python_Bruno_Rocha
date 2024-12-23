#!/ usr/bin/.env python3

import os
import sys

if os.path.exists("names.txt"):
    print("The file exists")
    input("...")
    names = open("names.txt").readlines()
else:
    print("[Error] Files name.txt not found")
    sys.exit(1)


if len(names) >= 3:
    print(names[2])
else:
    print("[Error] Missing name in the list")
    sys.exit(1)
