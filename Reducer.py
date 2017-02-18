"""Defines the parent reducer class, which executes a user defined function on the output of the mapper"""

class Reducer:
    def __init__(self):
        self.kvPairs = []

    def reducer(self, kvPair):
        print(":: Default reducer - custom reducer not configured")

    def run(self):
        reducedPairs = []
        for pairs in self.kvPairs:
            keyMatch = []
            for comPairs in self.kvPairs:
                if pairs.key == comPairs.key and comPairs.reduced == False:
                    keyMatch.append(comPairs)
                    comPairs.reduced = True
            reducedPairs.append(self.reducer(keyMatch))
        result = open("result.txt", 'w')
        for pair in reducedPairs:
            result.write(str(pair.key + ": " + pair.value))
