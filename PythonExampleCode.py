import SomeStatistic as s
import os
#from statistics import mean as m
# #from statistics import mean,...
#from statistics import *
import subprocess

# cx-freeze if you wish to make a executable from python

def printLine (toPrint="No Set Value"):
    print (toPrint)

class DocumentHandler:
    def writeFile(self, text = 'Sample Text to Save\nNew line!', fileName = 'exampleFile.txt'):
        saveFile = open(fileName,'w')
        # to append use 'a'
        saveFile.write(text)
        saveFile.close()

    def readFile(self, filename = 'exampleFile.txt'):
        readMe = open(filename,'r').read()
        return readMe

var = "Printable text"
#matrix eksamples
x = [[2,6],[6,2],[8,2],[5,12]]
y = [[5,2],
     [6,2],
     [3,1],
     [12,6]
    ]
example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5]
# Dictionary of names and ages. 
exDict = {'Jack':15,'Bob':22,'Alice':12,'Kevin':17}
exDict = {'Jack':[15,'blonde'],'Bob':[22, 'brown'],'Alice':[12,'black'],'Kevin':[17,'red']}

example_list.append(10) #add on end
example_list.insert(2,8) #add on index (index, val)
example_list.remove(6) #remove index
example_list.count(1) #count accurences of
example_list.sort()
example_list.reverse()

printLine(var)
#x = input('Input Field: ')
DocumentHandler.writeFile(DocumentHandler)
print(DocumentHandler.readFile(DocumentHandler))
s.someStatistic (example_list)
print(
'''
This
test 
'''
    )

curDir = os.getcwd()
print(curDir)
os.mkdir('newDir')
os.rename('newDir','newDir2')
os.rmdir('newDir2')

intMe = '55'
intMe = int(intMe)

stringMe = 55
stringMe = str(stringMe)

floatMe = 55
floatMe = float(floatMe)

subprocess.call('ls', shell=True) #call console comands
