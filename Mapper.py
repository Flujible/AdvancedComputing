from KVPair import KVPair

class Mapper:
    """Defines the mapper class, which executes a user defined function on each line of an input file"""
    def __init__(self):
        self.mapper = ""
        self.inputFile = ""

    def setMapFunction(self, function):
        self.mapper = function

    def setInputFile(self, inputFile):
        inFile = open(inputFile)
        if inFile:
            print(":: File set successfully")
            self.inputFile = inputFile
            inFile.close()
        else:
            print(":: File could not be set")

    def run(self):
        # Read the file, if there's a line then change everything in that line to
        # lowercase, and split on new line character, then run the mapper function on each of those lines
        # and set that array of mapped lines to the variable 'mapped'
        # Mapped will now be an array of arrays where each sub array is the result from mapping each line
        if not self.mapper:
            print(":: No mapper function set")
            return 0
        else:
            inFile = open(self.inputFile)
            if inFile:
                print(":: File opened successfully")
            else:
                print(":: File could not be opened")
            mapped = [ self.mapper(self, line) for line in inFile.read().lower().split("\n") if line ]
            print(":: Found " + str(len(mapped)) + " lines")
            output = []
            for pair in mapped:
                # print(type(pair))
                if str(type(pair)) == "<class 'KVPair.KVPair'>":
                    output.append(KVPair(pair.key, pair.value))
                # else:
                    # print(":: Not of class KVPair")
            return output

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
