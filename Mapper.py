"""Defines the parent mapper class, which executes a user defined function on each line of an input file"""

class Mapper:
    def __init__(self):
        self.mappedValues = []

    def mapper(self, inputLine):
        print(":: Default mapper - custom mapper not configured")

    def run(self, inputFile):
        #Split the file into lines, and then execute the mapper function on each line
        lines = inputFile.readLine()
        kvPairs = []
        for line in lines:
            kvPairs.append(self.mapper(line))
        return kvPairs
