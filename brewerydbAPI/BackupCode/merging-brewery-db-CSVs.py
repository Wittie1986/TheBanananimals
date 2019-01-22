# Import Dependencies

import pandas as pd
import numpy as np

# Define File Path for CSVs

brew1 = "Output/brewery_data_page001-014.csv"
brew2 = "Output/brewery_data_page015-029.csv"
brew3 = "Output/brewery_data_page030-044.csv"
brew4 = "Output/brewery_data_page045-059.csv"
brew5 = "Output/brewery_data_page060-074.csv"
brew6 = "Output/brewery_data_page075-089.csv"
brew7 = "Output/brewery_data_page090-104.csv"
brew8 = "Output/brewery_data_page105-119.csv"
brew9 = "Output/brewery_data_page120-134.csv"
brew10 = "Output/brewery_data_page135-149.csv"
brew11 = "Output/brewery_data_page150-164.csv"
brew12 = "Output/brewery_data_page165-179.csv"
brew13 = "Output/brewery_data_page180-194.csv"
brew14 = "Output/brewery_data_page195-209.csv"
brew15 = "Output/brewery_data_page210-224.csv"
brew16 = "Output/brewery_data_page225-239.csv"
brew17 = "Output/brewery_data_page240-254.csv"
brew18 = "Output/brewery_data_page255-260.csv"
brew19 = "Output/brewery_data_page261.csv"

# Read in CSVs

brewdf1 = pd.read_csv(brew1)
brewdf2 = pd.read_csv(brew2)
brewdf3 = pd.read_csv(brew3)
brewdf4 = pd.read_csv(brew4)
brewdf5 = pd.read_csv(brew5)
brewdf6 = pd.read_csv(brew6)
brewdf7 = pd.read_csv(brew7)
brewdf8 = pd.read_csv(brew8)
brewdf9 = pd.read_csv(brew9)
brewdf10 = pd.read_csv(brew10)
brewdf11 = pd.read_csv(brew11)
brewdf12 = pd.read_csv(brew12)
brewdf13 = pd.read_csv(brew13)
brewdf14 = pd.read_csv(brew14)
brewdf15 = pd.read_csv(brew15)
brewdf16 = pd.read_csv(brew16)
brewdf17 = pd.read_csv(brew17)
brewdf18 = pd.read_csv(brew18)
brewdf19 = pd.read_csv(brew19)

# Merge CSVs

brewerydf = pd.concat((brewdf1, brewdf2, brewdf3, brewdf4, brewdf5, brewdf6, brewdf7, brewdf8,
                       brewdf9, brewdf10, brewdf11, brewdf12, brewdf13, 
                        brewdf14, brewdf15, brewdf16, brewdf17, brewdf18, 
                        brewdf19), join="outer")
brewerydf.head()

## Clean up the Data Frame

# Initial count
brewerydf.count()

# Remove non-USA Breweries

usabrewerydf = brewerydf.loc[(brewerydf["Country"] == "UNITED STATES")]
usabrewerydf.count()

# Remove Breweries before 2009

brewerydf2009 = usabrewerydf.loc[(usabrewerydf["Year Established"] >= 2009)]
brewerydf2009.count()

# Replace "null" with NaN values

#brewerydfnull = brewerydf2009.replace(['null'], np.nan)
#brewerydfnull.count()

# Drop all rows with missing information

#cleanbrewerydf = brewerydfnull.dropna(axis=0, how='any')
#cleanbrewerydf.count()

final_df = brewerydf2009
final_df.head()

# Export Merged & Cleaned CSV

final_df.to_csv("Output/brewerydb_final.csv",
                   encoding="utf-8", index=False, header=True)