
"""Defines the tasks for the mapper and the reducer to perform on the data file"""
from Mapper import Mapper
from Reducer import Reducer
from UserCode import StripErrorsUserCode

def start():
    mapper = Mapper()
    reducer = Reducer()

    mapper.setInputFile("./inputFiles/AComp_Passenger_data.csv")
    mapper.setMapFunction(StripErrorsUserCode.mapDuplicates)
    reducer.setRedFunction(StripErrorsUserCode.redWrite)
    reducer.setOutputFile("./inputFiles/PassengerData.csv")
    pairs = mapper.run()
    reducer.run(pairs, 'w')

    mapper.setInputFile("./inputFiles/PassengerData.csv")
    mapper.setMapFunction(StripErrorsUserCode.mapSpelling)
    pairs = mapper.run()
    reducer.run(pairs, 'w')
