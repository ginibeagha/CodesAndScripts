import os, re
#with open(r'D:\Program Files\Git\license.txt') as workingFile:
 #   for line in workingFile.read():
   #     print(line, end='\n')

lyrics='''On the first day of Christmas
my true love sent to me:
A Partridge in a Pear Tree4

On the second day of Christmas
my true love sent to me:
Two Turtle Doves
and a Partridge in a Pear Tree2

On the third day of Christmas
my true love sent to me:
Three French Hens
Two Turtle Doves
and a Partridge in a Pear Tree1

On the fourth day of Christmas
my true love sent to me:
Four Calling Birds
Three French Hens
Two Turtle Doves
and a Partridge in a Pear Tree1



Read more: Christmas Song - 12 Days Of Christmas Lyrics | MetroLyrics 
    '''
def regexTest(text):
    phonenumRegex= re.compile(r'((\(\d\d\d\)|\d\d\d)-\d\d\d-\d\d\d\d)')##\-(\d){3}\-(\d){4})')
    mo=phonenumRegex.findall('my phone number is 213-222-4567, (333)-565-7890, 888-444-1234')
    print(mo)
    ##
    batmanregex=re.compile(r'((bat)(wo)*man(s)*|mobile|menace)',re.I)
    mo2=batmanregex.search(text)
    pos=text.index(mo2.group())
    mo3=batmanregex.search(text[pos+len(mo2.group()):])
    print(mo2.group(), mo3.group())
    print(pos)
    ##
    ha=re.compile(r'(ha){3}')
    mo4=ha.search(text)
    print(mo4.group())
    ##
    global lyrics
    text=lyrics
    lettereg= re.compile(r'.\w{3}\s')
    songreg=re.compile(r'\s(\w+\sday)')
    mo5= lettereg.findall(text)
    #mo5= songreg.findall(text)
    print(mo5)
    mo6=lettereg.sub(r'1,2,3,4',text)
    #print (mo6)
regexTest("the batmobile of Batman is batwomans biggest attraction, hahahaha")

