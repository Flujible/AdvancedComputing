class Reducer:
    """Defines the parent reducer class, which executes a user defined function on the output of the mapper"""

    def __init__(self):
        self.kvPairs = []
        self.reducer = ""
        self.outputFile = ""

    def setRedFunction(self, function):
        self.reducer = function

    def setOutputFile(self, outputFile):
        self.outputFile = outputFile

    def run(self, kvPairs, fileWriteMode):
        reducedPairs = []
        # Take each k/v pair and build a list of k/v pairs with the same key
        for pairs in kvPairs:
            matchingPairs = []
            if(not pairs.reduced):
                matchingPairs.append(pairs)
                pairs.reduced = True
            else:
                continue
            for comPairs in kvPairs:
                if pairs.key == comPairs.key and not comPairs.reduced:
                    matchingPairs.append(comPairs)
                    comPairs.reduced = True
                elif pairs.key == comPairs.key and comPairs.reduced == True:
                    continue
            reducedPairs.append(self.reducer(self, matchingPairs))
        print(reducedPairs)
        result = open(self.outputFile, fileWriteMode)
        for pair in reducedPairs:
            result.write(str(pair.key) + ", " + str(pair.value) + "\n")
        result.close()
