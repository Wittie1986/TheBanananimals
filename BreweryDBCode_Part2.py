# Dependencies
import requests
import json
import pandas as pd

#Build URL
url = "https://api.brewerydb.com/v2/locations/"
api_key = "?key=ce9e2cd34af4e3038e4d25477173db69&p="
new_url = url + api_key

# Lists
pages = []
####pages = list(range(151,261)) *try a small number first to avoid overloading API*

indexes = []
indexes = list(range(0,50))

names = []
local = []
region = []
country = []
est = []
bizstatus = []
closed = []    

# Request API

for page in pages:
    response = requests.get(new_url + str(page)).json()
    for index in indexes:
        try:
            est.append(response["data"][index]["brewery"]["established"])
        except KeyError:
            indexes.remove(index)
            continue
        names.append(response["data"][index]["name"])
        try:
            local.append(response["data"][index]["locality"])
        except KeyError:
            local.append(["null"])
            region.append(["null"])
            country.append(["null"])
            bizstatus.append(["null"])
            closed.append(["null"])
            continue
        try:
            region.append(response["data"][index]["region"])
        except KeyError:
            region.append(["null"])
            country.append(["null"])
            bizstatus.append(["null"])
            closed.append(["null"])
            continue
        try:
            country.append(response["data"][index]["country"]["name"])
        except KeyError:
            country.append(["null"])
            bizstatus.append(["null"])
            closed.append(["null"])
            continue
        try:
            bizstatus.append(response["data"][index]["brewery"]["isInBusiness"])
        except KeyError:
            bizstatus.append(["null"])
            closed.append(["null"])
            continue
        try:
            closed.append(response["data"][index]["isClosed"])
        except KeyError:
            closed.append(["null"])
            continue

# Count lists
len(est), len(names), len(local), len(region), len(country), len(bizstatus), len(closed)

## NOT NEEDED ## Print Lists
print(est)
print(names)
print(local)
print(region)
print(country)
print(bizstatus)
print(closed)

# Create a Data Frame
brewery_dict = {
    "Brewery Name": names,
    "City": local,
    "State": region,
    "Country": country,
    "Year Established": est,
    "In Business?": bizstatus,
    "Closed?": closed
}
brewery_data = pd.DataFrame(brewery_dict)
brewery_data.head()

## NOT NEEDED ## Double Check Data Count
brewery_data.count()

# Export to CSV file
brewery_data.to_csv("Output/brewery_data_part2.csv",
                   encoding="utf-8", index=False, header=True)

## Will need to merge Part 1 and Part 2 CSV files into 1 CSV file