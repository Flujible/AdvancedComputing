import re

# AComp_Passenger_data column headers:
    # column[0] = Passenger ID (XXXnnnnXXn)
    # column[1] = Flight ID (XXXnnnnX)
    # column[2] = Dept. airport code (XXX)
    # column[3] = Arr. airport code (XXX)
    # column[4] = Departure time GMT (n [10] (This is using unix epoch time))
    # column[5] = Total Flight time (mins) (n [1..4])

def stripErrors(inputLine):
    inputCopy = inputLine
    words = inputLine.split(",")
    if not re.match("[a-zA-Z]{3}[0-9]{4}[a-zA-Z]{2}[0-9]{1}", words[0]):
        # print(":: Passenger ID incorrect")
        return 0
    elif not re.match("[a-zA-Z]{3}[0-9]{4}[a-zA-Z]{1}", words[1]):
        # print(":: Flight ID incorrect")
        return 0
    elif not re.match("[a-zA-Z]{3}", words[2]):
        # print(":: source airport code incorrect")
        return 0
    elif not re.match("[a-zA-Z]{3}", words[3]):
        # print(":: Destination airpot code incorrect")
        return 0
    elif not re.match("[0-9]{10}", words[4]):
        # print(":: Departure time incorrect")
        return 0
    elif not re.match("[0-9]{1,4}", words[5]):
        # print(":: Total flight time incorrect")
        return 0
    else:
        return inputCopy
