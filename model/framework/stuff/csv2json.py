import pandas as pd
import json

# Assuming you have the CSV file named "data.csv" with the following content:
# Name,Age,City
# John,25,New York
# Alice,30,London
# Bob,22,Paris

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('input.csv')

# Convert the DataFrame to JSON
json_data = df.to_json(orient='records')

# Save JSON data to a file
with open('data.json', 'w') as json_file:
    json_file.write(json_data)
