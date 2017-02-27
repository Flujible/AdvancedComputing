"""File to contain the functions needed to execute the task:  Determine the number
 of flights from each airport, include a list of any airports not used."""

from KVPair import KVPair

def mapUnusedAirports(self, inputLine):
    inputLine = inputLine.split(",")
    return KVPair(inputLine[1], "0")

def mapUsedAirports(self, inputLine):
    inputLine = inputLine.split(",")
    return KVPair(inputLine[2], inputLine[1])

def mapMakePairs(self, inputLine):
    inputLine = inputLine.split(",")
    return KVPair(inputLine[0], inputLine[1])

def redUnusedAirports(self, kvPairs):
    return KVPair(kvPairs[0].key, "0")

def redUsedAirports(self, kvPairs):
    flightCodes = [ pair.value for pair in kvPairs ]
    # print(":: Found " + str(len(set(flightCodes))) + " from " + kvPairs[0].key)
    return KVPair(kvPairs[0].key, str(len(set(flightCodes))))

def redCountFlights(self, kvPairs):
    val = 0
    for pairs in kvPairs:
        val += int(pairs.value)
    return KVPair(kvPairs[0].key, str(val))
