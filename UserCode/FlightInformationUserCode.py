"""File to contain the functions needed to execute the task:  Create a list of
flights based on the Flight id, this output should include the passenger Id,
relevant IATA/FAA codes, the departure time, the arrival time (times to be
converted to HH:MM:SS format), and the flight times."""

from KVPair import KVPair
from datetime import datetime, timedelta

def mapReOrder(self, inputLine):
    words = inputLine.split(",")
    return KVPair(words[1], str(words[0] + "," + words[2] + "," + words[3] + "," + words[4] + "," + words[5]))

def redCalcFlightInfo(self, kvPairs):
    #kvPair.value column headers:
        # [0] = Passenger ID (XXXnnnnXXn)
        # [1] = Dept. airport code (XXX)
        # [2] = Arr. airport code (XXX)
        # [3] = Arr. airport code Departure time GMT (n [10] (This is using unix epoch time))
        # [4] = Total Flight time (mins) (n [1..4])
    retVal = ""

    # Split the first KVPair's value
    words = kvPairs[0].value.split(",")

    # Add airport codes to return value
    retVal += words[1]
    retVal += "," + words[2]

    # Add departure time to return value
    timestamp = datetime.fromtimestamp(int(words[3]))
    hms = str(timestamp).split(" ")
    retVal += "," + hms[1]

    # Add flight duration to the return value
    secs = int(words[4])*60
    mins, seconds = divmod(secs, 60)
    hours, minutes = divmod(mins, 60)
    retVal += "," + (str(hours) + ":" + str(minutes) + ":" +  str(seconds))

    # Add arrival time to the return value
    arrivalTime = timestamp + timedelta(hours=hours,minutes=minutes,seconds=seconds)
    hms = str(arrivalTime).split(" ")
    retVal += "," + hms[1]

    # Add passenger IDs to return value
    passengers = ""
    for pair in kvPairs:
        values = pair.value.split(",")
        passengers += (";" + values[0])
    retVal += "," + passengers
    return KVPair(kvPairs[0].key, retVal)
