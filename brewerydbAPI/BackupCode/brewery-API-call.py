# Dependencies

import requests
import json
import pandas as pd
import time

#Build URL

url = "https://api.brewerydb.com/v2/locations/"
api_key = "?key=ce9e2cd34af4e3038e4d25477173db69&p="
new_url = url + api_key

# Note: API is tempermental | Only have 200 requests / day

# Lists

pages = []
pages = list(range(195,210))

# try a small number first to test & avoid overloading API
# run in 15page ranges to avoid overloading API:

# Amanda: (1,15), (15,30), (30,45), (45,60), (60,75), (75,90), (90,105)
# Amanda: (105,120), (120,135), (135,150), (150,165), (165,180), (180,195)
# Nathan: (195,210), (210,225), (225,240), (240,255), (255,261)
# Amanda: Last Page has less indexes, so run it solo: (261,262)   

# Lists Part 2

indexes = []
indexes = list(range(0,50))

# Amanda/Nathan: use range (0,50) for all pages except last page (261,262)
# Amanda: use range (0,15) for last page, it has 16 indexes

# Lists Part 3

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
        names.append(response["data"][index]["brewery"]["name"])
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
time.sleep(5)

# Count length of lists to check API call was correct

len(est), len(names), len(local), len(region), len(country), len(bizstatus), len(closed)

# Create a Data Frame

brewery_dict = {
    "Brewery Name": names,
    "City": local,
    "State": region,
    "Country": country,
    "Year Established": est,
    "Still in Business?": bizstatus,
    "Closed?": closed
}
brewery_data = pd.DataFrame(brewery_dict)
brewery_data.head()

# Export data to CSV file

brewery_data.to_csv("Output/brewery_data_page195-209.csv",
                   encoding="utf-8", index=False, header=True)

# Change File name for each 15pages called & Merge after all are completed
# Base CSV Name: brewery_data_page
# With page numbers: brewery_data_page001-014.csv

# Amanda: 001-014, 015-029, 030-044, 045-059, 060-074, 075-089, 090-104
# Amanda: 105-119, 120-134, 135-149, 150-164, 165-179, 180-194
# Nathan: 195-209, 210-224, 225-239, 240-254, 255-261
# Amanda: 261

# Merge all CSV files in next steps