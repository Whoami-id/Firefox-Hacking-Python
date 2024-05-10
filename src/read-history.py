import sqlite3
import pandas as pd
import datetime

from helper import get_firefox_path

path = get_firefox_path("places.sqlite")
conn = sqlite3.connect(path)

history = pd.read_sql("SELECT * FROM moz_historyvisits", conn)
places = pd.read_sql("SELECT * FROM moz_places", conn)

print(history.head())

print(places.head())


# https://docs.python.org/3.6/library/datetime.html?highlight=datetime#strftime-and-strptime-behavior
for key, item in history.iterrows():
    place_id = item["place_id"]
    url = places[places["id"] == place_id].iloc[0]["url"]
    
    timestamp = datetime.datetime.fromtimestamp(item["visit_date"] / 1000000)
    
    print(timestamp.strftime("%d.%m.%Y %H:%M") + " - " + url)