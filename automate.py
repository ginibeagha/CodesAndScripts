import os, re
with open(r'newfile.txt', mode='r') as workingFile:
    for line in workingFile.readline():
        print(line,end='\n')

