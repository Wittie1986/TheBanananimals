# Import Dependencies
import pandas as pd

# Define File Path for CSVs
brewery1_csv = "Output/brewery_data_part1.csv"
brewery2_csv = "Output/brewery_data_part2.csv"

# Read in CSVs
brewerydf_1 = pd.read_csv(brewery1_csv)
brewerydf_2 = pd.read_csv(brewery2_csv)

# Merge CSVs
brewerydf = pd.merge(brewerydf_1, brewerydf_2, how="outer")
brewerydf.head()

# Export new Merged CSV
brewerydf.to_csv("Output/brewery_data_merged.csv",
                   encoding="utf-8", index=False, header=True)