"""File to contain the functions needed to execute the task:  Determine the number
 of flights from each airport, include a list of any airports not used."""

from KVPair import KVPair
from regex import stripErrors

# If the flight code and passenger ID are valid, return a kvpair with the flight code as key, and passenger as value
def mapPassengerToFlight(self, inputLine):
    if stripErrors(inputLine):
        words = inputLine.split(",")
        return KVPair(words[1], words[0])
    else:
        print(":: Not valid input: " + inputLine)
        return 0

# Count the number of passegers per flight code, and return that as a kvpair
def redCountPassengers(self, kvPairs):
    cnt = 0
    for pairs in kvPairs:
        cnt += 1
    return KVPair(kvPairs[0].key, str(cnt))
