# Reference solution (rewritten after original work was lost)

import sys

import httpx
import pandas as pd
import matplotlib.pyplot as plt

api_key="U6KXJTZC2E8VGH39PD7UMG4BZ"   # your API key

city="Leeds"     # city location
country="UK"     # country location

# request daily data: the date plus max/min/average temperature and rainfall (precip)
elements = "include=days&elements=datetime,tempmax,tempmin,temp,precip"

# URL location of the API for time history forecasts
base = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

# construct the URL string for the API call
url = base + city + "," + country + "?key=" + api_key + "&" + elements

# http request
response = httpx.get(url)

# status code - check it and stop the program if the request failed
print(response.status_code)
if response.status_code != 200:
    print(response.text)      # the API usually explains what went wrong
    sys.exit(f"Request failed with status code {response.status_code}")

# json data
data = response.json()

# raw data output
print(data)

# extract the temperature data as lists from the JSON dictionary
# data['days'] is a LIST of dictionaries, one dictionary per day
temp_data = data['days']

print(temp_data)

# use pandas to convert data to  dataframe
# each dictionary becomes a row; each key becomes a column
df = pd.DataFrame(temp_data)

# use the date as the index so it appears along the x-axis
df = df.set_index("datetime")
print(df)

# note that temperature is in Farenheit (F)
# convert to Celcius before plotting:  C = (F - 32) * 5 / 9
for column in ["tempmin", "temp", "tempmax"]:
    df[column] = (df[column] - 32) * 5 / 9
print(df)

# using matplotlib plot the 3 data sets: (tempmin,temp,tempmax) as line graphs
df[["tempmin", "temp", "tempmax"]].plot(title=f"Temperature forecast for {city}")

# annotate the graph with axis labels
plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# using the documentation explore other data, eg. rainfall
# 'precip' (added to the elements above) is rainfall per day, in inches by default
df["precip"].plot(kind="bar", title=f"Rainfall forecast for {city}")
plt.xlabel("Date")
plt.ylabel("Rainfall (inches)")
plt.tight_layout()
plt.show()
