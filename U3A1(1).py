'''
Unit 3 Assignment 1
Zachary Sisco

This program contains a function that takes an integer argument and tests
whether that integer is a Harshad number. The function will return the
appropriate value. This function will then be used to create a list of all
numbers from 1-500 that are Harshad numbers. This list will be printed.
'''

def isHarshad(num):

    #turn num into list of digits
    digits = list(str(num))

    #convert the str objects to int objects
    for i in range(0, len(digits)):
        digits[i] = int(digits[i])

    #find the sum of digits
    sumDigits = sum(digits)

    #set up bool test for Harshad status
    yesHarshad = (num % sumDigits == 0)

    #test bool
    if yesHarshad:
        return True
    else:
        return False


def listHarshad():
    
    #create empty list for Harshad values
    HarshadList = []

    #use loop to test numbers up to 500 for Harshad status, fill list 
    for i in range(1,501):
        if isHarshad(i) == True:
            HarshadList.append(i)

    print(HarshadList)


print("\nThis program tests for Harshad numbers.\n")
isHarshad(50)
listHarshad()
print("\nHave a great day!\n")
