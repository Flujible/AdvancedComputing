from KVPair import KVPair
from regex import stripErrors

def mapDuplicates(self, inputLine):
    if stripErrors(inputLine):
        inputLine = inputLine.split(",")
        return KVPair(inputLine[0] + "," + inputLine[1], inputLine[2] + "," + inputLine[3] + "," + inputLine[4] + "," + inputLine[5])
    else:
        print(":: ERROR: Input line not propely formed, removed from dataset: " + inputLine)

def mapSpelling(self, inputLine):
    words = inputLine.split(",")
    airportCodes = ["atl", "pek", "lhr", "ord", "hnd", "lax", "cdg", "dfw", "fra", "hkg",
    "den", "dxb", "cgk", "ams", "mad", "bkk", "jfk", "sin", "can", "las", "pvg", "sfo", "phx",
    "iah", "clt", "mia", "muc", "kul", "fco", "ist"]
    if words[2] in airportCodes and words[3] in airportCodes:
         return KVPair(words[0] + "," + words[1], words[2] + "," + words[3] + "," + words[4] + "," + words[5])
    else:
        print(":: ERROR: Airport not found, removed from dataset: " + inputLine)

def redWrite(self, kvPairs):
    return KVPair(kvPairs[0].key, kvPairs[0].value)
