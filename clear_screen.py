#coding: utf-8


import os

def clear_screen():
    if os.name == "posix":		# Unix/Linux/MacOS/BSD/etc
        os.system('clear')		# Clear the Screen
    elif os.name in ("nt", "dos", "ce"):	# DOS/Windows
        os.system('CLS')					# Clear the Screen
