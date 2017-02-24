# AComp_Passenger_data column headers:
    # column[0] = Passenger ID (XXXnnnnXXn)
    # column[1] = Flight ID (XXXnnnnX)
    # column[2] = Dept. airport code (XXX)
    # column[3] = Arr. airport code (XXX)
    # column[4] = Departure time GMT (n [10] (This is using unix epoch time))
    # column[5] = Total Flight time (mins) (n [1..4])

"""File to contain the functions needed to execute the task:  Determine the number
 of flights from each airport, include a list of any airports not used."""

from KVPair import KVPair
import re

# If the flight code and passenger ID are valid, return a kvpair with the flight code as key, and passenger as value
def mapPassengerToFlight(self, inputLine):
    words = inputLine.split(",")
    if re.match("[a-zA-Z]{3}[0-9]{4}[a-zA-Z]{2}[0-9]{1}", words[0]) and re.match("[a-zA-Z]{3}[0-9]{4}[a-zA-Z]{1}", words[1]):
        return KVPair(words[1], words[0])

# Count the number of passegers per flight code, and return that as a kvpair
def redCountPassengers(self, kvPairs):
    cnt = 0
    for pairs in kvPairs:
        cnt += 1
    return KVPair(kvPairs[0].key, str(cnt))
