"""Defines the parent mapper class, which executes a user defined function on each line of an input file"""

class Mapper:
    def __init__(self):
        self.mappedValues = []

    def mapper(self, inputLine):
        print(":: Default mapper - custom mapper not configured")

    def run(self, inputFile):
        # Read the file, if there's a line then change everything in that line to
        # lowercase, and split on new line character, then run the mapper function on each of those lines
        # and set that array of mapped lines to the variable 'mapped'
        # Mapped will now be an array of arrays where each sub array is the result from mapping each line
        mapped = [ self.mapper(line) for line in inputFile.read().lower().split("\n") if line ]
        print(":: Found " + str(len(mapped)) + " lines")
        return mapped

        # This is only needed if the user's mapper function returns an array of arrays
        # If the length of the array is greater than one then append all the results to first element
        # This means that we dont have an array of maps for each line, we have one array of results for
        # the whole file
        # if len(mapped) > 1:
        #     for line in mapped:
        #         if line == mapped[0]:
        #             continue
        #         mapped[0] = mapped[0] + line
        #         result = mapped[0]
        # else:
        #     result = mapped[0]
        # print(":: Found " + str(len(result)) + " words")
        # return result
