import requests

class DataManager:
    """
    Handles all communication with the Sheety API.
    Responsible for retrieving flight data and emails from an email list from Google Sheets.
    """

    def __init__(self, bearer_token : str):
        # Authorization header used for all Sheety API requests
        self.header = {
            "Authorization" : f"Bearer {bearer_token}"
        }
    
    def get_data(self, api_url : str):
        """
        Fetches flight data from Google Sheet via Sheety API.
        """
        self.response = requests.get(url = api_url, headers = self.header)
        self.response.raise_for_status()
        return self.response.json()["flights"]
    
    def get_email_list(self, api_url : str):
        """
        Fetches emails from an email list from Google Sheet via Sheety API.
        """
        self.response = requests.get(url = api_url, headers = self.header)
        self.response.raise_for_status()
        email_list = [email["whatIsYourEmail?"] for email in self.response.json()["emails"]]
        return email_list
