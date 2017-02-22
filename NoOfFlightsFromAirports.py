from KVPair import KVPair
# AComp_Passenger_data column headers:
    # column[0] = Passenger ID
    # column[1] = Flight ID
    # column[2] = Dept. airport code
    # column[3] = Arr. airport code
    # column[4] = Departure time GMT (Unix epoch time)
    # column[5] = Total Flight time (mins)


# Mapper for word count
    # newInput = []
    # kvPairs = []
    # for word in inputLine:
        # if word == "":
        #     continue
        # elif "." in word or "," in word:
        #     newWord = word.strip(string.punctuation)
        #     newInput.append(newWord)
        # else:
        #     newInput.append(word)
    # for word in newInput:
    #     pair = KVPair(word, 1)
    #     kvPairs.append(pair)
    # return kvPairs

# Reducer for word count
    # cnt = 0
    # for pair in kvPairs:
    #     cnt += pair.value
    # output = KVPair(kvPairs[0].key, cnt)
    # return output

"""Class to contain the functions needed to execute the task:  Determine the number of flights from each airport, include a list of any airports not used."""
def __init__(self):
    pass

def mapUnusedAirports(self, inputLine):
    inputLine = inputLine.split(",")
    print(":: Airport code: " + inputLine[1])
    return KVPair(inputLine[1], "0")

def mapUsedAirports(self, inputLine):
    inputLine = inputLine.split(",")
    print(":: " + inputLine[2] + ", " + inputLine[1])
    return KVPair(inputLine[2], inputLine[1])

def mapCombine(self, inputLine):
    pass

def redUnusedAirports(self, kvPairs):
    data = []
    for pair in kvPairs:
        data.append(pair)
    return data

def redUsedAirports(self, kvPairs):
    flightCodes = []
    for pair in kvPairs:
        flightCodes.append(pair.value)
    print(":: Found " + str(len(set(flightCodes))) + " from " + kvPairs[0].key)
    return KVPair(kvPairs[0].key, str(len(set(flightCodes))))

def redCombine(self, kvPairs):
    pass
