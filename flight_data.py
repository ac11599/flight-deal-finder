class FlightData:
    """
    Transforms raw flight API data into structured, readable deal alerts.
    Filters flights based on user-defined maximum price.
    """

    def __init__(self, flights_data):
        self.structured_deals = []

        # Process each route's flight data
        for f in flights_data:
            self.structure_deal(f)
    
    def structure_deal(self, data):
        """
        Extracts cheap flights and formats them into email-ready deals.
        """

        max_price = data["max price"]
        flight_data = data["flight data"]

        # Combine different flight categories from API response
        flights = []
        flights.extend(flight_data.get("best_flights", []))
        flights.extend(flight_data.get("other_flights", []))

        # Filter flights based off of price
        cheap_flights = [flight for flight in flights if flight["price"] <= max_price]

        for flight in cheap_flights:
            deal = {}

            departure_city = flight_data["airports"][0]["departure"][0]["city"]
            departure_country = flight_data["airports"][0]["departure"][0]["country"]
            arrival_city = flight_data["airports"][0]["arrival"][0]["city"]
            arrival_country = flight_data["airports"][0]["arrival"][0]["country"]
            
            price = flight["price"]

            deal["Subject"] = f"{departure_city}, {departure_country} -> {arrival_city}, {arrival_country} for ${price}"

            body = "Flight details:\n"
            for segment in flight["flights"]:
                departure_airport = segment["departure_airport"]
                arrival_airport = segment["arrival_airport"]
                body += f"Departure - {departure_airport["name"]} ({departure_airport["id"]}) at {departure_airport["time"]}\n"
                body += f"Arrival - {arrival_airport["name"]} ({arrival_airport["id"]}) at {arrival_airport["time"]}\n"
                
                body += f"Details -\n"                  
                body += f"- Duration: {segment["duration"] // 60} hours {segment["duration"] % 60} minutes\n"
                body += f"- Airline: {segment["airline"]}\n"
                body += f"- Travel Class: {segment["travel_class"]}\n"
                body += f"- Flight Number: {segment["flight_number"]}\n"

                extensions = segment.get("extensions", [])
                if extensions:
                    body += f"- Additional Details: \n"
                    for detail in segment["extensions"]:
                        body += f"    -{detail}\n"
                body += "\n"
            
            print(type(flight["total_duration"]))

            body += f"Total Duration: {flight["total_duration"] // 60} hours {flight["total_duration"] % 60} minutes\n"
            body += f"Price: ${price}\n"

            extensions = flight.get("extensions", [])
            if extensions:
                body += f"Additional Details:\n"
                for detail in extensions:
                    body += f"    -{detail}\n"

            deal["Body"] = body

            self.structured_deals.append(deal)


    def get_structured_deals(self):
        """Returns final formatted deals ready for email notification."""
        return self.structured_deals