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


def isSiete(num):

    #turn number into digits
    digits = list(str(num))

    #convert str objects into int
    for i in range(0, len(digits)):
        digits[i] = int(digits[i])

    #check for 7 in tens place, excluding numbers without tens place
    if len(digits) >= 2:
        for i in digits:
            if digits[-2] == 7:
                return True
            else:
                return False


Hodges = 14
isHarshad(270)
isSiete(777)
    
