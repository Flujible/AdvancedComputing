"""Defines the tasks for the mapper and the reducer to perform on the data file"""
from Mapper import Mapper
from Reducer import Reducer
from UserCode import FlightInformationUserCode

def start():
    mapper = Mapper()
    reducer = Reducer()

    # Produce a list of all the airports in a csv file with the headings 'Airport Code', and 'Null'
    mapper.setInputFile("./inputFiles/AComp_Passenger_data.csv")
    mapper.setMapFunction(FlightInformationUserCode.mapReOrder)
    reducer.setRedFunction(FlightInformationUserCode.redCalcFlightInfo)
    reducer.setOutputFile("./results/FlightInformation.csv")
    noPassengers = mapper.run()
    reducer.run(noPassengers, 'w')
