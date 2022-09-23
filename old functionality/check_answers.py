import pprint


# path
import os
import sys
from pathlib import Path
from turtle import width
current_path = os.getcwd() 



# get code to run
py_path = Path(current_path + f"\\py_files\ex_.py")


codes = []
code = ""
door = "Closed"
with open(py_path) as fp:
    for line in fp:
        line = line.strip()
        
        # თუ სტარტი ნახა გახსნას
        if "#__start__" in line:
            door = "Open"
        # თუ ენდია დახუროს 
        elif "#__end__" in line:
            door = "Closed"
            
            codes.append(code)
            code = ""

        # თუ გახსნა და სტარტი არაა
        if door == "Open" and  "#__start__" not in line:
            code += line 


pprint.pprint(codes[0])


# get func and answer in dictionary

