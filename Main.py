"""Defines the tasks for the mapper and the reducer to perform on the data file"""
import KeyValuePair

def mapper(inputLine):
    inputLine = inputLine.split(" ")
    kvPairs = []
    for word in inputLine:
        pair = KeyValuePair(word.word, 1)
        kvPairs.append(pair)
    return kvPairs

# The reducer itterates over KVPairs where the key is teh same, then moves onto the next set of keys
def reducer(kVPairs, output):
    cnt = 0
    for pair in kVPairs:
        cnt += pair.value
    output.setKey(kVPairs.key)
    output.setValue(cnt)
