"""Defines the tasks for the mapper and the reducer to perform on the data file"""
from Mapper import Mapper
from Reducer import Reducer
import NoOfFlightsFromAirports

mapper = Mapper()
reducer = Reducer()

# Produce a list of all the airports in a csv file with the headings 'Airport Code', and 'Null'
mapper.setInputFile("./inputFiles/Top30_airports_LatLong.csv")
mapper.setMapFunction(NoOfFlightsFromAirports.mapUnusedAirports)
reducer.setRedFunction(NoOfFlightsFromAirports.redUnusedAirports)
reducer.setOutputFile("./results/Airports.csv")
unusedAirports = mapper.run()
reducer.run(unusedAirports)

# Produce a list of all the airports used in the passenger data file in a csv file with the headings 'Airport Code', and 'Number of flights from that airport'
mapper.setInputFile("./inputFiles/AComp_Passenger_data.csv")
mapper.setMapFunction(NoOfFlightsFromAirports.mapUsedAirports)
reducer.setRedFunction(NoOfFlightsFromAirports.redUsedAirports)
usedAirports = mapper.run()
reducer.run(usedAirports)

# Combine the two above results to give a list of all flights from each airport, including those that aren't used
# Heading titles: 'Airport code', 'No. of flights from that airport'
mapper.setMapFunction(NoOfFlightsFromAirports.mapMakePairs)
mapper.setInputFile("./results/Airports.csv")
reducer.setOutputFile("./results/finalResult.csv")
allAirports = mapper.run()
reducer.setRedFunction(NoOfFlightsFromAirports.redCountFlights)
reducer.run(allAirports)
