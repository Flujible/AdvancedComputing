"""This code represents what we want the mapper to do to each line of the input file"""


def mapper(inputLine, output):
    inputLine = inputLine.split(",")
    for word in inputLine:
        output.key = word
        output.value = 1


# I dont understand how this is supposed to work, it somewhat mimics the wordcount hadoop example
def reducer(kVPairs, output):
    cnt = 0
    for pair in kVPairs:
        cnt+= pair.value
    output.setKey(kVPairs.key)
    output.setValue(cnt)
