"""Defines the parent reducer class, which executes a user defined function on the output of the mapper"""

class Reducer:
    def __init__(self):
        self.kvPairs = []

    def reducer(self, kvPair):
        print(":: Default reducer - custom reducer not configured")

    def run(self, kvPairs):
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
                if pairs.key == comPairs.key and comPairs.reduced == False:
                    matchingPairs.append(comPairs)
                    comPairs.reduced = True
                elif pairs.key == comPairs.key and comPairs.reduced == True:
                    continue
            print(":: '" + pairs.key + "' found " + str(len(matchingPairs)) + " times")
            reducedPairs.append(self.reducer(matchingPairs))
        result = open("result.json", 'w')
        result.write("{\n")
        for pair in reducedPairs:
            result.write('    "' + str(pair.key) + '": ' + str(pair.value) + ",\n")
        result.write("}")
