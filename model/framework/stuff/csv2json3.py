import csv
import json

input_csv_file = '/home/zakia/eos9be7/model/framework/input.csv'
output_json_file = '/home/zakia/eos9be7/model/framework/smiles_input2.json'

# Read CSV and store data in a list
data = []
with open(input_csv_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # Skip the header row
    for row in csv_reader:
        data.append(row[0])  # Assuming single column, extract the first element (SMILES)

# Pair the SMILES strings into a list of lists
pairs = [[data[i], data[i+1]] for i in range(len(data) - 1)]

# Convert the data to the desired JSON format
json_data = json.dumps(pairs)

# Write the JSON data to a file
with open(output_json_file, 'w') as json_file:
    json_file.write(json_data)
