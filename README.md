# ✈️ Flight Deal Finder

An automated Python application that tracks flight prices and sends email alerts when cheap deals are found.

---

## 🚀 What it does

This project:
- Reads flight routes and price limits from a Google Sheet (via Sheety API)
- Uses SerpAPI (Google Flights) to fetch live flight data
- Filters flights under a user-defined price threshold
- Sends email notifications when good deals are found

---

## ⚙️ Tech Stack

- **Python**
- **Sheety API** — Google Sheets integration
- **SerpAPI** — Google Flights scraping
- **SMTP** — email notifications
- **python-dotenv** — environment variable management

---

## 🧠 How It Works

1. Flight routes + max prices are stored in a Google Sheet  
2. The app retrieves this data via Sheety  
3. SerpAPI queries Google Flights for live prices  
4. Results are filtered based on price threshold  
5. If a deal is found, an email alert is sent automatically  

---

## 📦 Installation

```bash
git clone https://github.com/ac11599/flight-deal-finder.git
cd flight-deal-finder
pip install -r requirements.txt
```

---

## ▶️ Running the App

```bash
python main.py
```

---

## 🔐 Environment Variables

Create a .env file in the root directory:

```
SHEETY_BEARER_TOKEN = your_token
SERPAPI_API_KEY = your_key
MY_EMAIL = your_email
MY_PASSWORD = your_password
SHEETY_FLIGHTS_URL = your_sheety_flights_endpoint
SHEETY_EMAILS_URL = your_sheety_emails_endpoint
```
