"""While it is possible to find the next smallest number by generating all possible solutions by incrementing by +1,
this solution unfortunately becomes unusable when given number has N > 6 due to it's inefficiency.

However, it is possible to find the next number that has same sum by simply applying an operator +1 -1 to the number array.
There are special cases where the least significant digits are 9 9, 0 0 and 9 0 that need to be addressed. """

def findNextSmallest(number: int):

    inputNumber = [int(d) for d in str(number)] #Convert into array of numbers
    leastSignificantNoIndex = len(inputNumber)-1
    outputNumber = -1
    positionFound = False

    indexSearchRight = leastSignificantNoIndex - 2  # Init search indexes, one of operator on left, one for right (LSD)
    indexSearchLeft = leastSignificantNoIndex - 3
    indexFoundLeft = 0
    indexFoundRight = 0

    #Default operator (+1, -1):
    if (inputNumber[leastSignificantNoIndex] != 0) and (inputNumber[(leastSignificantNoIndex-1)] != 9):

        inputNumber[leastSignificantNoIndex]-= 1
        inputNumber[(leastSignificantNoIndex-1)]+=1
        outputNumber = int("".join(map(str, inputNumber))) #join list to a number output


    #CASE of LSDs = 0,0. Operator +1, -x ...... +x-1. Move search window until conditions met:
    if (inputNumber[leastSignificantNoIndex] == 0) and (inputNumber[(leastSignificantNoIndex-1)] == 0):

        while positionFound is False:
            if inputNumber[indexSearchRight] and inputNumber[indexSearchLeft] != 9: #If search conditions satisfied:
                positionFound = True
                indexFoundRight = indexSearchRight
                indexFoundLeft = indexSearchLeft

            else:                                                                   #If not satisfied, move index by 1 to left:
                indexSearchRight-=1
                indexSearchLeft-=1

        inputNumber[indexFoundLeft] += 1    # +1 Operator for number on left
        x = inputNumber[indexFoundRight]    # get x
        inputNumber[indexFoundRight] = 0    # set right digit to 0 (-x)
        inputNumber[leastSignificantNoIndex] = x-1  #set LSD (Least significant digit) to x-1
        outputNumber = int("".join(map(str, inputNumber)))      #join list to a number output


    # CASE of LSDs = 9,9 or 9,0. Search until number on the left is <9, apply default operator (+1, -1):
    if [(inputNumber[leastSignificantNoIndex] == 9) or inputNumber[(leastSignificantNoIndex - 1)] == 0]\
                                                 and (inputNumber[(leastSignificantNoIndex - 1)] == 9):

        while positionFound is False:
            try:
                if inputNumber[indexSearchRight] > 0 and inputNumber[indexSearchLeft] < 9:  # If search conditions satisfied:
                    positionFound = True
                    indexFoundRight = indexSearchRight
                    indexFoundLeft = indexSearchLeft
                    inputNumber[indexFoundLeft] += 1  # +1 Operator for number on left
                    inputNumber[indexFoundRight] -= 1  # -1 Operator for number on the right
                    outputNumber = int("".join(map(str, inputNumber)))  # join list to a number output
                else:  # If not satisfied, move index by 1 to left:
                    indexSearchRight -= 1
                    indexSearchLeft -= 1
            except:
                break


    return outputNumber