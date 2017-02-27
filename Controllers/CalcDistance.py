"""Defines the tasks for the mapper and the reducer to perform on the data file"""
from Mapper import Mapper
from Reducer import Reducer
from UserCode import CalcDistanceUserCode

def start():
    mapper = Mapper()
    reducer = Reducer()

    mapper.setInputFile("./inputFiles/PassengerData.csv")
    mapper.setMapFunction(CalcDistanceUserCode.mapCalcFlightDistances)
    reducer.setRedFunction(CalcDistanceUserCode.redCalcFlightDistance)
    reducer.setOutputFile("./results/FlightDistances.csv")
    flightDistances = mapper.run()
    reducer.run(flightDistances, 'w')

    mapper.setInputFile("./results/FlightDistances.csv")
    mapper.setMapFunction(CalcDistanceUserCode.mapTotalPassengerDistance)
    reducer.setRedFunction(CalcDistanceUserCode.redTotalPassengerDistance)
    reducer.setOutputFile("./results/TotalDistanceTravelledByEachPassenger.csv")
    passengerDistance = mapper.run()
    reducer.run(passengerDistance, 'w')

    mapper.setInputFile("./results/FlightDistances.csv")
    mapper.setMapFunction(CalcDistanceUserCode.mapDistaces)
    reducer.setRedFunction(CalcDistanceUserCode.redDistances)
    reducer.setOutputFile("./results/DistanceOfEachFlight.csv")
    distances = mapper.run()
    reducer.run(distances, 'w')

    print(":: Task 4 complete")
