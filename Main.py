"""File to control each mapReduce task for the coursework"""
from Controllers import StripErrors
from Controllers import NoOfFlightsFromAirports
from Controllers import PassengersOnEachFlight
from Controllers import FlightInformation
from Controllers import CalcDistance

# Strip duplicate entries from the input file and re-write it
StripErrors.start()

# Determine the number of flights from each airport, including those with no flights
NoOfFlightsFromAirports.start()

# Calculate the number of passengers on each flight
PassengersOnEachFlight.start()

# Create a list of flights based on the Flight id, this output should include the
# passenger Id, relevant IATA/FAA codes, the departure time, the arrival time
# (times to be converted to HH:MM:SS format), and the flight times.
FlightInformation.start()

# Calculate the line-of-sight (nautical) miles for each flight and the total
# travelled by each passenger
CalcDistance.start()
