import os
print(os.path.join('usr','bin','spam'))
print(os.getcwd())
os.chdir(os.path.join('\Program Files (x86)'))
print(os.getcwd())
os.chdir(os.path.join('..\\codesandscripts'))
print(os.getcwd())
#os.mkdir(os.path.join('\codesandscripts','newfolder'))
os.chdir('.\\newfolder')
print(os.getcwd())
print(os.path.abspath('..\..'))
print(os.path.getsize(os.path.join('d:','\\')))
for file in os.listdir(os.path.join('\Program Files (x86)','putty')):
    print(file +" size is "+ str(os.path.getsize(os.path.join('\Program Files (x86)\putty', file))/1000)+" kb")
newfile=open(os.path.join('d:\\', 'codesandscripts', 'newfile.txt'),'a')
newfile.write("this is in addition to what was written before")
newfile.close()
newfile=open(os.path.join('d:\\', 'codesandscripts', 'newfile.txt'))
print(newfile.read())

