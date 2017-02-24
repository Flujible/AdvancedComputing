from KVPair import KVPair
import re
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

"""Class to contain the functions needed to execute the task:  Determine the number
 of flights from each airport, include a list of any airports not used."""

def mapUnusedAirports(self, inputLine):
    inputLine = inputLine.split(",")
    if re.match("[a-zA-Z]{3}", inputLine[1]):
        print(":: Airport code: " + inputLine[1])
        return KVPair(inputLine[1], "0")
    else:
        print(":: Invalid Airport Code: " + inputLine[1])
        return 0

def mapUsedAirports(self, inputLine):
    inputLine = inputLine.split(",")
    if re.match("[a-zA-Z]{3}", inputLine[2]) and re.match("[a-zA-Z]{3}[0-9]{4}[a-zA-Z]{1}", inputLine[1]):
        print(":: " + inputLine[2] + ", " + inputLine[1])
        return KVPair(inputLine[2], inputLine[1])
    else:
        print(":: Invalid input: " + inputLine[2] + ", " + inputLine[1])
        return 0

def mapMakePairs(self, inputLine):
    inputLine = inputLine.split(",")
    return KVPair(inputLine[0], inputLine[1])

def redUnusedAirports(self, kvPairs):
    return KVPair(kvPairs[0].key, "0")

def redUsedAirports(self, kvPairs):
    flightCodes = [ pair.value for pair in kvPairs ]
    print(":: Found " + str(len(set(flightCodes))) + " from " + kvPairs[0].key)
    return KVPair(kvPairs[0].key, str(len(set(flightCodes))))

def redCountFlights(self, kvPairs):
    val = 0
    for pairs in kvPairs:
        val += int(pairs.value)
    return KVPair(kvPairs[0].key, str(val))
