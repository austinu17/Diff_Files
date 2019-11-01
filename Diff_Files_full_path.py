#!/usr/bin/env python
import pandas as pd 
import os
import subprocess
import sys
cwd = os.getcwd()

file_1 = sys.argv[1]
file_2 = sys.argv[2]

#Runs Diff Command on inputs and exports to txt file
if os.path.exists('Diff_Files_1.txt') == False:
    new = open('Diff_Files_1.txt', 'w')
    subprocess.run(['diff', '-rq',file_1, file_2], stdout= new )

#Converts input to list of strings of individual variables
Text_String = []
with open('Diff_Files_1.txt','r') as f:
    for line in f:
        for word in line.split():
            Text_String.append(word)


# Sort through files to remove extraneous files
file_paths = []
extension = tuple(['benchmark.txt','log','benchmarks.txt'])
for word in Text_String:
    if word.endswith((extension)) == False and word.startswith("proteomic_workflow_final_OS_16GB_4C_Test_2"):
        file_paths.append(word)


#Print full path of files to output 
with open("diff_file_path.txt", "w") as att_file:
    for item in file_paths:
        att_file.write(cwd +"/"+ item + "\n")

