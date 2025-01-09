#!/usr/bin/env python3


"""Hello World multi linguas.
"""
import os

__version__="0.0.1"
__author__="Monique Graciano"
__license__="Unlicense"

current_language=os.getenv("LANG")[:5]
msg="Hello, World!"

if current_language=="pt_BR":
    msg="Olá, Mundo!"
elif current_language=="it_IT":
    msg="Ciao, Mondo!"

print(msg)


