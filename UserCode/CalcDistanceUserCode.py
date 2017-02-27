# PassengerData column headers:
    # column[0] = Passenger ID (XXXnnnnXXn)
    # column[1] = Flight ID (XXXnnnnX)
    # column[2] = Dept. airport code (XXX)
    # column[3] = Arr. airport code (XXX)
    # column[4] = Departure time GMT (n [10] (This is using unix epoch time))
    # column[5] = Total Flight time (mins) (n [1..4])

"""File to contain the functions needed to execute the task:  Create a list of
flights based on the Flight id, this output should include the passenger Id,
relevant IATA/FAA codes, the departure time, the arrival time (times to be
converted to HH:MM:SS format), and the flight times."""

from KVPair import KVPair
from UserCode.DistanceCalculator import haversine

def mapCalcFlightDistances(self, inputLine):
    words = inputLine.split(",")
    return KVPair(str(words[0] + "," + words[1]), str(words[2] + "," + words[3]))

def mapDistaces(self, inputLine):
    words = inputLine.split(",")
    return KVPair(words[1], words[2])

def mapTotalPassengerDistance(self, inputLine):
    words = inputLine.split(",")
    return KVPair(words[0], words[2])

def redCalcFlightDistance(self, kvPairs):
    #kvPair.key column headers:
        # [0] = Passenger ID
        # [1] = Flight ID
    #kvPair.value column headers:
        # [0] = Dept. airport code (XXX)
        # [1] = Arr. airport code (XXX)

    # Open the airport information file and split it on new line
    airports = open("./inputFiles/Top30_airports_LatLong.csv")
    if not airports:
        print(":: Error, could not open airport info file")
    airportInfo = airports.read()
    airportInfo = airportInfo.split("\n")

    # Split the first KVPair's value
    kvPairValues = kvPairs[0].value.split(",")
    # Find the latitude and longitude of the airpots in use and calculate the distance between them
    deptLat = ""
    deptLong = ""
    arrLat = ""
    arrLong = ""
    for line in airportInfo[:-1]:
        info = line.split(",")
        if kvPairValues[0] in info[1].lower():
            # print(":: Found departure airport!")
            deptLat = float(info[2])
            deptLong = float(info[3])
        if kvPairValues[1] in info[1].lower():
            # print(":: Found destinartion airport!")
            arrLat = float(info[2])
            arrLong = float(info[3])
    if len(kvPairs) > 1:
        for pairs in kvPairs:
            print(pairs.key)
            print(pairs.value)
    distance = haversine(deptLat, deptLong, arrLat, arrLong)

    return KVPair(kvPairs[0].key, str(round(distance)))

def redDistances(self, kvPairs):
    return KVPair(kvPairs[0].key, kvPairs[0].value)

def redTotalPassengerDistance(self, kvPairs):
    distance = 0
    for pairs in kvPairs:
        distance += int(pairs.value)
    return KVPair(kvPairs[0].key, str(distance))
