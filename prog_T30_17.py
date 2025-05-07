import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime
import re

def get_weather(city_url):
    url = f"https://sinoptik.ua/погода-{city_url}"
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")

    UA_MONTHS = {
        "січня": "January", "лютого": "February", "березня": "March",
        "квітня": "April", "травня": "May", "червня": "June",
        "липня": "July", "серпня": "August", "вересня": "September",
        "жовтня": "October", "листопада": "November", "грудня": "December"
    }

    data = []
    for i in range(1, 6):
        day = soup.find("div", id=f"bd{i}")
        if not day:
            continue
        day_text = day.find("p", class_="date").text.strip()
        month_ua = day.find("p", class_="month").text.strip().lower()
        month_en = UA_MONTHS.get(month_ua, "January")

        date_str = f"{day_text} {month_en}"
        date = datetime.strptime(date_str, "%d %B")

        max_temp = day.find("div", class_="temperature").find_all("span", class_="max")[0].text
        min_temp = day.find("div", class_="temperature").find_all("span", class_="min")[0].text

        max_temp_val = int(re.findall(r'-?\d+', max_temp)[0])
        min_temp_val = int(re.findall(r'-?\d+', min_temp)[0])

        data.append({
            "date": date.replace(year=datetime.now().year).strftime("%Y-%m-%d"),
            "min": min_temp_val,
            "max": max_temp_val
        })
    return data

def save_to_excel(weather_data, filename="weather.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.append(["Дата", "Мін. температура", "Макс. температура"])

    for entry in weather_data:
        ws.append([entry["date"], entry["min"], entry["max"]])

    wb.save(filename)

if __name__ == "__main__":
    city = input("Введіть назву міста (напр. kyiv): ").strip().lower()
    data = get_weather(city)
    save_to_excel(data)
    print("Дані збережено у weather.xlsx")