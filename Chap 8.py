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
