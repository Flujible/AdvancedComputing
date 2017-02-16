"""Defines the parent reducer class, which executes a user defined function on the output of the mapper"""

class Reducer:
    def __init__(self):
        pass

    def reducer(self, kvPairs):
        print(":: Default reducer - custom reducer not configured")

    def run(self):
        #Split the file into lines, and then execute the mapper function on each line
        kvPairs = []
        for line in lines:
            kvPairs.append(self.mapper(line))
        return kvPairs
