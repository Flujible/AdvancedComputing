"""Defines the parent mapper class, which executes a user defined function on each line of an input file"""

class Mapper:
    def __init__(self):
        self.mappedValues = []

    def mapper(self, inputLine):
        print(":: Default mapper - custom mapper not configured")

    def run(self, inputFile):
        # Split the file into lines, and then execute the mapper function on each line#
        # lines = inputFile.read().split("\n")
        mapped = [ self.mapper(line) for line in inputFile.read().lower().split("\n") if line ]
        print(":: Found " + str(len(mapped)) + " lines")
        if len(mapped) > 1:
            for line in mapped:
                if line == mapped[0]:
                    continue
                mapped[0] = mapped[0] + line
                result = mapped[0]
        else:
            result = mapped[0]
        print(":: Found " + str(len(result)) + " words")
        return result
