#Created_By_rohithgoud30
import requests
from bs4 import BeautifulSoup
import pandas as p

page = requests.get("https://mausam.imd.gov.in/")
soup = BeautifulSoup(page.content, "html.parser")
weather = soup.find(id="today")
cities = weather.find_all("h3")
today_cities = [city.get_text()[:-1] for city in cities]
temp_val = soup.find_all(class_="val")
temp_val_cities  = [str(val)[18:-7] for val in temp_val]
winds = soup.find_all(class_="wind")
wind_val_cities  = [str(wind)[16:-4] for wind in winds]
wind_val_cities1 = [wind_cities.split("<br/>") for wind_cities in wind_val_cities]
unzipped = list(zip(*wind_val_cities1))
wind_val_cities2 = list(unzipped[0])
wind_val_cities3 = list(unzipped[1])

weather_stuff = p.DataFrame({
    "Cities": today_cities,
    "Winds": temp_val_cities,
    "Wind_Direction": wind_val_cities2,
    "Wind_Speed" : wind_val_cities3,
    })

name = str(input("Enter Name of CSV file : "))
if name == "":
    weather_stuff.to_csv("weather_default.csv")
else:
    save_name = name + ".csv"
    weather_stuff.to_csv(save_name)


