"""Defines the parent reducer class, which executes a user defined function on the output of the mapper"""

class Reducer:
    def __init__(self):
        self.kvPairs = []

    def reducer(self, kvPair):
        print(":: Default reducer - custom reducer not configured")

    def run(self, kvPairs):
        print("::" + str(len(kvPairs)))
        # reducedPairs = []
        # Take each k/v pair and build a list of k/v pairs with the same key
        for pairs in kvPairs:
            matchingPairs = []
            if(not pairs.reduced):
                # print("\n:: " + pairs.key + " found")
                matchingPairs.append(pairs)
                pairs.reduced = True
            else:
                # print("\n:: " + pairs.key + " found but already counted")
                continue
            for comPairs in kvPairs:
                # print(":: Comparing " + pairs.key + " with " + comPairs.key)
                if pairs.key == comPairs.key and comPairs.reduced == False:
                    # print(":: " + comPairs.key + " is a match")
                    matchingPairs.append(comPairs)
                    comPairs.reduced = True
                elif pairs.key == comPairs.key and comPairs.reduced == True:
                    continue
                    # print(":: " + comPairs.key + " is a match, but is already being considered")
            print(":: '" + pairs.key + "' found " + str(len(matchingPairs)) + " times")
            # reducedPairs.append(self.reducer(keyMatch))
        # result = open("result.txt", 'w')
        # for pair in reducedPairs:
        #     result.write(str(pair.key + ": " + pair.value))
