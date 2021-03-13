#
# program: check if a credit card is valid and prints which bank owns
# author: Jose Ramos Briseño
# date: 2021-03-12
#

def isValidLuhnAlgorithm(card):
    # Luhn's algorithm
    aDouble = [0] * len(card)
    i = len(card) - 1
    p = len(card) - 2
    while i >= 0:
        val = 0
        if (p == i):
            val = card[i] * 2
            if (val > 9):
                val = val - 9
            p = p - 2
        else:
            val = card[i]
        aDouble[i] = val
        i = i - 1
    sumDigit = sum(aDouble) % 10

    return sumDigit == 0

def GetTypeCard(card):
    out = "INVALID"
    aAMEX = [34, 37]
    aMC = [51, 52, 53, 54, 55]
    twoDigits = int(str(card[0]) + str(card[1]))
    aVisaCardSizes = [13, 16]
    cardSize = len(card)
    
    if (card[0] == 4 and cardSize in aVisaCardSizes):
        out = "VISA"
    elif (twoDigits in aAMEX and cardSize == 15):
        out = "AMEX"
    elif (twoDigits in aMC and cardSize == 16):
        out = "MASTERCARD"

    return out

if __name__ == "__main__":
    num = ""
    while not num.isdigit():
        num = input('Number: ')
    aNum = [int(i) for i in num]
    aTypeCards = ["VISA", "AMEX", "MASTERCARD"]
    output = GetTypeCard(aNum)

    if (output in aTypeCards):
        if (not isValidLuhnAlgorithm(aNum)):
            output = "INVALID"        
    
    print (output)
