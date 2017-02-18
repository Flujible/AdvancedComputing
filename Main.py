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
        inputLine = inputLine.split(" ")
        kvPairs = []
        for word in inputLine:
            if "." in word or "," in word:
                newWord = word.strip(string.punctuation)
                inputLine.remove(word)
                inputLine.append(newWord)
            if word == "":
                inputLine.remove(word)
        for word in inputLine:
            pair = KVPair(word, 1)
            kvPairs.append(pair)
        return kvPairs

class MyReducer(Reducer):
    """Class to override the original reducer class functions"""
    def __init__(self):
        Reducer.__init__(self)

    # The reducer itterates over KVPairs where the key is teh same, then moves onto the next set of keys
    def reducer(self, kVPairs):
        cnt = 0
        for pair in kVPairs:
            cnt += pair.value

        output = KVPair(kVPairs.key, cnt)
        return output

myMapper = MyMapper()
myReducer = MyReducer()

inputFile = open("./inputFiles/Sample.txt")
if inputFile:
    print(":: File opened successfully")
else:
    print(":: Could not open file")

results = myMapper.run(inputFile)

for result in results[0]:
    print(result.key + ": " + str(result.value))
