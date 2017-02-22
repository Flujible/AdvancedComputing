"""Defines the tasks for the mapper and the reducer to perform on the data file"""
from KVPair import KVPair
from Mapper import Mapper
from Reducer import Reducer
import string

class MyMapper(Mapper):
    """Class to override the original mapper class functions"""
    def __init__(self):
        Mapper.__init__(self)

    # The mapper class takes a file and performs the below function on each line of that file
    def mapper(self, inputLine):

        # Mapper for task:
        # Determine the number of flights from each airport, include a list of any airports not used.
        inputLine = inputLine.split(",")
        print(":: " + inputLine[2] + ", " + inputLine[1])
        return KVPair(inputLine[2], inputLine[1])

        # inputLine[0] = Passenger ID
        # inputLine[1] = Flight ID
        # inputLine[2] = Dept. airport code
        # inputLine[3] = Arr. airport code
        # inputLine[4] = Departure time GMT (Unix epoch time)
        # inputLine[5] = Total Flight time (mins)

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

class MyReducer(Reducer):
    """Class to override the original reducer class functions"""
    def __init__(self):
        Reducer.__init__(self)

    # The reducer itterates over KVPairs where the key is the same, then moves onto the next set of keys
    def reducer(self, kvPairs):
        # Reucer code for task
        # Determine the number of flights from each airport, include a list of any airports not used.
        # This doesn't take into account airports not useds
        flightCodes = []
        for pair in kvPairs:
            flightCodes.append(pair.value)
        print(":: Found " + str(len(set(flightCodes))) + " from " + kvPairs[0].key)
        return KVPair(kvPairs[0].key, str(len(set(flightCodes))))

        # Reducer for word count
        # cnt = 0
        # for pair in kvPairs:
        #     cnt += pair.value
        # output = KVPair(kvPairs[0].key, cnt)
        # return output

myMapper = MyMapper()
myReducer = MyReducer()

inputFile = open("./inputFiles/AComp_Passenger_data_no_error_DateTime.csv")
if inputFile:
    print(":: File opened successfully")
else:
    print(":: Could not open file")

mapResults = myMapper.run(inputFile)
redResults = myReducer.run(mapResults)

# for mapResult in mapResults:
#     print(":: " + mapResult.key + ": " + str(mapResult.value))
