"""Defines the tasks for the mapper and the reducer to perform on the data file"""
from Mapper import Mapper
from Reducer import Reducer
from UserCode import PassengersOnEachFlightUserCode

def start():
    mapper = Mapper()
    reducer = Reducer()

    # Produce a list of all the airports in a csv file with the headings 'Airport Code', and 'Null'
    mapper.setInputFile("./inputFiles/AComp_Passenger_data.csv")
    mapper.setMapFunction(PassengersOnEachFlightUserCode.mapPassengerToFlight)
    reducer.setRedFunction(PassengersOnEachFlightUserCode.redCountPassengers)
    reducer.setOutputFile("./results/NumberOfPassengersOnEachFlight.csv")
    noPassengers = mapper.run()
    reducer.run(noPassengers, 'w')
