def readfile(str):
    with open(str, mode='r', encoding='cp1252', errors='ignore') as datafile:
        for number, line in enumerate(datafile.readlines()):
            print(number,': ',line)
        
readfile('C:\\Users\\Ginibeagha\\Downloads\\pythontest.txt')