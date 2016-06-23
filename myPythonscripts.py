def readfile(str):
    with open(str, mode='r', errors='ignore') as datafile:
        for number, line in enumerate(datafile.readlines()):
            print(number,': ',line)
        
#readfile('C:\\Users\\Ginibeagha\\Downloads\\pythontest.txt')

def writeFile(string):
    with open("newfile.txt", 'w') as temp:
        print(string, file=temp)
        
#writeFile('this is just a taste of writing a new file')

def testMethod():
    while True:
        command= input("please choose one of the options [rwq]: ")
        print(command)
        if command=='q':
            break
        elif command.lower()=='r':
            print('you have chosen to move right')
            continue
        elif command=='w':
            print('you have chosen the w option')
            continue
        else:
            print('please one of [rwq]')
            continue

#testMethod()

def testtry():
    while True:
        try:
            value= input('choose a number between 1 and 20: ')
            print(int(value))
            continue
        except ValueError:
            print ('that was not a number try again by hitting the enter key')
            continue
        else:
            if int(value) > 20:
                print('number is too high try again by hitting the enter key')
                continue
            elif int(value) < 1:    
                print ('number too low try again by hitting the enter key')
                continue
            elif value=='q':
                break
            

testtry()        