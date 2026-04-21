# import secrets
import os
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

load_dotenv()

# 1. Fetch data from Google Sheets (Sheety API)
SHEETY_FLIGHTS_URL = os.environ.get("SHEETY_FLIGHTS_URL")
SHEETY_EMAILS_URL = os.environ.get("SHEETY_EMAILS_URL")

data_manager = DataManager(os.environ.get("SHEETY_BEARER_TOKEN"))

flights_parameters = data_manager.get_data(SHEETY_FLIGHTS_URL)
email_list = data_manager.get_email_list(SHEETY_EMAILS_URL)

# 2. Search for flights using SerpAPI (Google Flights)
flight_searcher = FlightSearch(flights_parameters, os.environ.get("SERPAPI_API_KEY"))
flights_data = flight_searcher.get_flights_data()

# 3. Process and filter flight data into deals
flight_data_processor = FlightData(flights_data)

# 4. Send email notifications for valid deals
notification_manager = NotificationManager(os.environ.get("MY_EMAIL"), os.environ.get("MY_PASSWORD"))

for deal in flight_data_processor.get_structured_deals():
    notification_manager.send_mail(email_list = email_list, subject = deal["Subject"], body = deal["Body"])
