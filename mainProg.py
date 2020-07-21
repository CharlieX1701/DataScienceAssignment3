'''
Main Program
Zachary Sisco
Unit 3 Assignment 2

This program is going to import multiple functions and a variable. Additionally,
it will read in a file containing 5000 numbers. The imported functions will
be used to test these numbers for Harshad status, whether the tens place
contains a 7, and whether the Harshad numbers contain a 7 in the tens place.
Harshad numbers that contain a 7 in the tens place will be output to a new
file. Additionally, the program will print to screen the sum of the Harshad
numbers as well as a list of numbers that are Harshad, have a 7 in the tens
place, and are evenly divisible by the imported variable.
'''

#import library containing functions and variable
import myLib

def getData(num):

    #get data, clean it, turn to ints
    nf = open('Rumbers.txt' , 'r')
    data = nf.read()
    nf.close()

    data = data.replace('\n', '\t')
    data = data.split('\t')

    for i in range(0, len(data)):
        data[i] = int(data[i])

    return data


def getNums():
    
    #finding Harshad numbers and numbers that meet all 3 criteria
    HarshadList = []
    Big3 = []

    for i in dataList:
        if myLib.isHarshad(i) == True:
            HarshadList.append(i)
        if (myLib.isHarshad(i) == True) and (myLib.isSiete(i) == True) and (i % myLib.Hodges == 0):
            Big3.append(i)

    print("The sum of the Harshad numbers is: ", sum(HarshadList), '\n')
    print("Numbers that meet all criteria:")
    print(Big3)


def fileHarsh7d():
    
    #creating output file that contains Harshad numbers with 7 in tens place
    outFile = 'HarshOut.txt'
    outVar = open(outFile, 'w')

    for i in dataList:
        if (myLib.isHarshad(i) == True) and (myLib.isSiete(i) == True):
            outVar.write(str(i) + '\n')

    outVar.close()


#create global variable from getData
dataList = getData(1120)

getNums()
fileHarsh7d()

#note of positivity
print("\nAt the end of hardship comes happiness. Have a great day!")
