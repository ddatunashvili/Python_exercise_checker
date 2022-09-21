from itertools import count
from unittest import result
from nbformat import read, NO_CONVERT

# path
import os
import sys
from pathlib import Path
current_path = os.getcwd() 

import time
def count_filenames(prefix):
    #we shall store all the file names in this list
    filelist = []
    for root, dirs, files in os.walk(current_path+r"\ipynb_files"):
        for file in files:
            #append the file name to the list
            filelist.append(os.path.join(root,file))
    try: 
        ipynb_count = 0   
        for name in filelist:
            file_prefix = name.split(".")[-1]
            if file_prefix == prefix:
                ipynb_count += 1
        return ipynb_count
    except:              
        pass

ipynb_count = count_filenames("ipynb")
# შეამოწმონს ipynb  ფაილები
if ipynb_count == 0:
    sys.exit(f"there is no 'ipynb' file in current_path (directory) --->  {current_path}\ipynb_files")

# get all python code results and convert to txt
for i in range(1,ipynb_count+1):
    try:
        print(f"converting...")
        time.sleep(2)
        ipynb_path = Path(current_path + f"\\ipynb_files\ex_"+str(i)+".ipynb")
        py_path = Path(current_path + f"\\py_files\ex.py")
        with open(ipynb_path) as fp:
            notebook = read(fp, NO_CONVERT)
        cells = notebook['cells']
        code_cells = [c for c in cells if c['cell_type'] == 'code']
        result_ = ""
        for cell in code_cells:
            result_ +=  cell['source'] 
        with open(py_path,"w") as f:
            f.writelines(result_)
            result_ = ""
    except Exception as e:
        print(e)
        print(f"ex_{i}.ipynb not fount")
    print("converting done !")