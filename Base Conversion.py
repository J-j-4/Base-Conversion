#Note: the number input must be a String (i.e. surrounded by quotes)

print("""Note: To use baseConversion, the number input must be a String
(i.e. surrounded by quotes), such as: baseConversion(\"1AC3\", 13, 5)
""")

def baseConversion(number, initialBase, targetBase): 
    ## First get any invalid inputs out of the way.
    import sys
    if not(2 <= initialBase <= 16 and 2 <= targetBase <= 16):
        print("Error: Must choose a base between 2 and 16")
        sys.exit()

    hexString = "0123456789ABCDEF"
    valid_digits = hexString[0:initialBase]
        
    for digit in number:
        if digit not in valid_digits:
            print("Error: That number does not exist in that base")
            sys.exit()

    ## Now the program converts the number to base 10.
    baseTenNumber = 0
    exponent = 0
    for digit in reversed(number):
        digitValue = hexString.index(digit)
        baseTenNumber = baseTenNumber + (digitValue * (initialBase ** exponent))
        exponent += 1
        
    ## And then it converts the number to the target base.
    answer = ""
    while baseTenNumber > 0:
        for exponent in range(50, -1, -1):
            if (targetBase ** exponent) > baseTenNumber and answer != "":
                answer = answer + "0"
            else:
                for i in range(targetBase - 1, 0, -1):
                    if (i * (targetBase ** exponent)) <= baseTenNumber:
                        baseTenNumber = baseTenNumber - (i * (targetBase ** exponent))
                        answer = answer + hexString[i]
                    else:
                        pass
    else:
        print(answer)

#TESTS
"""
baseConversion("ABA", 13, 7) #5242
baseConversion("FFF", 16, 10) #4095
baseConversion("FFF", 16, 2) #111111111111
baseConversion("14A2", 11, 16) #787
baseConversion("ABC", 13, 7) #5244
baseConversion("ABA", 13, 7) #5242
baseConversion("124312", 5, 14) #1B41
"""
