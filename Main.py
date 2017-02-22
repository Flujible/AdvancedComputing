"""Defines the tasks for the mapper and the reducer to perform on the data file"""
from Mapper import Mapper
from Reducer import Reducer
from NoOfFlightsFromAirports import *

mapper = Mapper()
reducer = Reducer()

mapper.setInputFile("./inputFiles/Top30_airports_LatLong.csv")
mapper.setMapFunction(mapUnusedAirports)
reducer.setRedFunction(redUnusedAirports)
reducer.setOutputFile("./results/redUsedAirports")
unusedAirports = mapper.run()
reducer.run(unusedAirports)
#
# mapper.setInputFile("./inputFiles/AComp_Passenger_data_no_error_DateTime.csv")
# mapper.setMapFunction(mapUsedAirports)
# reducer.setRedFunction(redUsedAirports)
# mapper.run()
