"""This code represents what we want the mapper to do to each line of the input file"""


def mapper(inputLine, output):
    inputLine = inputLine.split(",")
    for word in input:
        output.key = word
        output.value = 1
