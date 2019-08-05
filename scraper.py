import requests
from bs4 import BeautifulSoup

"""
Webscraper for https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168
"""

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_days = soup.find(id="seven-day-forecast")
forecast_days = seven_days.find_all(class_="forecast-tombstone")

for item in forecast_days:
    period_date = item.find(class_="period-name").get_text()
    long_desc = item.find("img").get('alt', '')
    short_desc = item.find(class_="short-desc").get_text()
    temp = item.find(class_="temp").get_text()

    print(period_date)
    print("==============================")
    print(long_desc)
    print(short_desc)
    print(temp + "\n\n\n\n\n")
