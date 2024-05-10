from helper import get_firefox_path
import sqlite3
import pandas as pd

path = get_firefox_path("places.sqlite")

conn = sqlite3.connect(path)

#http://kb.mozillazine.org/Places.sqlite

df = pd.read_sql("SELECT * FROM moz_bookmarks", conn)
print(df)