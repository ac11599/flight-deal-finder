import requests
import datetime as dt

# Set to 44 days based on data that shows fares tend to be the lowest around 44 days before departure
OUTBOUND_DATE_DAYS_FROM_TODAY = 44

class FlightSearch:
    """
    Handles interaction with SerpAPI (Google Flights).
    Searches for flights and returns raw flight data.
    """

    def __init__(self, flights_parameters : list, api_key :str):
        self.api_key = api_key
        self.flights_data = []

        outbound_date = (dt.datetime.now() + dt.timedelta(days = OUTBOUND_DATE_DAYS_FROM_TODAY)).strftime("%Y-%m-%d")
        
        # Run search for each route from Google Sheet
        for flight in flights_parameters:
            self.search_flight(outbound_date, flight["departureId"], flight["arrivalId"], flight["lowestPrice"])
    
    def search_flight(self, outbound_date : str, departure_id : str, arrival_id : str, max_price : int):
        """
        Fetches Google Flights data from SerpAPI for a given route.
        """
        
        url = "https://serpapi.com/search"
        
        parameters = {
            "engine": "google_flights",
            "deep_search" : "true",
            "currency" : "USD",
            "api_key" : self.api_key,
            "type" : "2",
            "outbound_date" : outbound_date,
            "departure_id" : departure_id,
            "arrival_id" : arrival_id,
        }

        response = requests.get(url = url, params = parameters)
        response.raise_for_status()

        self.flights_data.append({"flight data" : response.json(), "max price" : max_price})
    
    def get_flights_data(self):
        """Returns raw flight results for processing."""
        return self.flights_data
