"""File to contain the functions needed to execute the task:  Determine the number
 of flights from each airport, include a list of any airports not used."""

from KVPair import KVPair
import re

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
