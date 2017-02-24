"""Defines the tasks for the mapper and the reducer to perform on the data file"""
from Mapper import Mapper
from Reducer import Reducer
from UserCode import NoOfFlightsFromAirportsUserCode

def start():
    mapper = Mapper()
    reducer = Reducer()

    # Produce a list of all the airports in a csv file with the headings 'Airport Code', and 'Null'
    mapper.setInputFile("./inputFiles/Top30_airports_LatLong.csv")
    mapper.setMapFunction(NoOfFlightsFromAirportsUserCode.mapUnusedAirports)
    reducer.setRedFunction(NoOfFlightsFromAirportsUserCode.redUnusedAirports)
    reducer.setOutputFile("./results/Airports.csv")
    unusedAirports = mapper.run()
    reducer.run(unusedAirports, 'w')

    # Produce a list of all the airports used in the passenger data file in a csv file with the headings 'Airport Code', and 'Number of flights from that airport'
    mapper.setInputFile("./inputFiles/AComp_Passenger_data_no_error_DateTime.csv")
    mapper.setMapFunction(NoOfFlightsFromAirportsUserCode.mapUsedAirports)
    reducer.setRedFunction(NoOfFlightsFromAirportsUserCode.redUsedAirports)
    usedAirports = mapper.run()
    reducer.run(usedAirports, 'a')

    # Combine the two above results to give a list of all flights from each airport, including those that aren't used
    # Heading titles: 'Airport code', 'No. of flights from that airport'
    mapper.setMapFunction(NoOfFlightsFromAirportsUserCode.mapMakePairs)
    mapper.setInputFile("./results/Airports.csv")
    reducer.setOutputFile("./results/NumberOfFlightsFromEachAirport.csv")
    allAirports = mapper.run()
    reducer.setRedFunction(NoOfFlightsFromAirportsUserCode.redCountFlights)
    reducer.run(allAirports, 'w')
