import csv

# example how to process and wotk with CSV data
#File Location
csvF = 'D:\Development Proeckts\Python-Basic-Totorial\example.csv'
#Location of the run
from os import getcwd ; print(getcwd())
#Working with the file
with open(csvF ) as csvfile:
    #Work with CSV File
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    for row in readCSV:
        #Row per row work
        print(row)
        print(row[0])
        print(row[0],row[1],row[2],)
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)
    print(dates)
    print(colors)
    try:
        whatColor = input('What color do you wish to know the date of?:')
        coldex = colors.index(whatColor)
        theDate = dates[coldex]
        print('The date of',whatColor,'is:',theDate)
    except Exception as e:
        print(e)