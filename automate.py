import os, re
#with open(r'D:\Program Files\Git\license.txt') as workingFile:
 #   for line in workingFile.read():
   #     print(line, end='\n')
def regexTest(text):
    phonenumRegex= re.compile(r'((\(\d\d\d\))?-\d\d\d-\d\d\d\d)')##\-(\d){3}\-(\d){4})')
    mo=phonenumRegex.findall('my phone number is 213-222-4567, (333)-565-7890, 888-444-1234')
    print(mo)
    ##
    batmanregex=re.compile(r'(B|b)(at)((wo)*man|mobile|menace)')
    mo2=batmanregex.search(text)
    pos=text.index(mo2.group())
    mo3=batmanregex.search(text[pos+len(mo2.group()):])
    print(mo2.group(), mo3.group())
    print(pos)
    ##
    ha=re.compile(r'(ha){3}')
    mo4=ha.search(text)
    print(mo4.group())
regexTest("the batmobile of Batman is batwomans biggest attraction, hahahaha")