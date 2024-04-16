from geopy.geocoders import Nominatim
import pandas as pd
import numpy as np
from time import sleep
from geopy.extra.rate_limiter import RateLimiter

#input and output
data = '/Users/manavparikh/Desktop/output/data_edit2.csv'
output = '/Users/manavparikh/Desktop/output/data_edit2_latlong.csv'

#Named Constants
ADDRESS = "ADDRESS"
ZIP = "ZIP"
CITY = "CITY"
STATE = "STATE"

#Latitude and longitude columns
COLUMN1 = "LAT"
COLUMN2 = "LON"

#Setting up geopy
geolocator = Nominatim(user_agent="PAL_scraper", timeout=100)
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1.01)

#df manipulation
df = pd.read_csv(data, delimiter=",", header=0)
df = df.drop_duplicates(subset=[ADDRESS], keep='first')

df[COLUMN1] = np.nan
df[COLUMN2] = np.nan

df = df.reset_index()

print(df)

attributecounter = 0
connectioncounter = 0

#query, save to df in memory, export to csv every count of 100
for index, row in df.iterrows():
    if int(index) % 500 == 0:
        df.to_csv(output,index=False)
        print("csv saved:", index)
    if int(index) % len(df.index) == 0:
        df.to_csv(output,index=False)
        print("csv saved:", index)
    if df.loc[index, COLUMN1] == "":
        query = ((f'{row[ADDRESS]}' + ', ' 
                    + f'{row[CITY]}'+ ', ' 
                    + f'{row[STATE]}' + ' '
                    + f'{row[ZIP]}'
                    )
                )
        location = geocode(query)
        try: 
            df.loc[index, COLUMN1] = location.latitude
            df.loc[index, COLUMN2] = location.longitude
        except AttributeError:
            attributecounter += 1
            if attributecounter % 50 == 0:
                print("Attribute Error count:", attributecounter)
        except ConnectionError:
            connectioncounter += 1
            if connectioncounter % 50 == 0:
                print("ConnectionError count", connectioncounter)