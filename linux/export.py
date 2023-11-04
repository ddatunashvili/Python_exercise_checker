# -*- coding: utf-8 -*-

from check import *

import json

import pandas as pd
print("\n\n")
name = input(" write student name: ")
print("\n\n")
df = pd.DataFrame(result.items())

xl_files_path = Path(current_path + f"/excel_files/{name}.xlsx")

df.to_excel(xl_files_path, sheet_name = name )