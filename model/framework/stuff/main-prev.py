import sys
import csv
import json
import os
import sys
import fcd
import warnings
import tensorflow as tf


# Suppress specific warning using a filter
warnings.filterwarnings("ignore")

tf.get_logger().setLevel('INFO')

input_file = sys.argv[1]
output_file = sys.argv[2]


# Read CSV and store data in a list
data = []
with open(input_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # Skip the header row
    for row in csv_reader:
        data.append(row[0])  # Assuming single column, extract the first element (SMILES)

# Pair the SMILES strings into a list of lists
pairs = [[data[i], data[i+1]] for i in range(len(data) - 1)]

# Convert the data to the desired JSON format
json_data = json.dumps(pairs)
ROOT = os.path.dirname(os.path.abspath(__file__))
output_json_file = os.path.abspath(os.path.join(ROOT, "..", "input_data.json"))

# Write the JSON data to a file
with open(output_json_file, 'w') as json_file:
    json_file.write(json_data)
	
# Check whether the json file loaded successfully or not	
try:
    with open(output_json_file, "r") as f:
        data = json.load(f)
    print("JSON data is loaded successfully.")
    # You can now work with the 'loaded_data' variable, which contains the parsed JSON.
except json.JSONDecodeError as e:
    print("Failed to load JSON data:", str(e))
    # Handle the exception or show an error message.
except FileNotFoundError:
    print("File not found. Make sure the 'data.json' file exists in the current directory.")
    # Handle the case when the file is not found.
	
# Now calculating fcd_scores based on json smile pairs
fcd_scores = []
count =0
for d in data:

    print("d0",d[0])
    print("d1",d[1])
    count = count+1
    print("count",count)
    can_smiles1 = [smi for smi in fcd.canonical_smiles(d[0]) if ((smi is not None))]
    can_smiles2 = [smi for smi in fcd.canonical_smiles(d[1]) if ((smi is not None))]
    print("can1",can_smiles1)
    print("can2",can_smiles2)
    fcd_scores += [fcd.get_fcd(can_smiles1, can_smiles2)]

# Writing the fcd_scores against each smiles pair in an output.csv file
print("Total Lists in the json file", count)
with open(output_file, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["fcd_score"])
    for fcd_score in fcd_scores:
        writer.writerow([fcd_score])
		
# Remove output_json_file if you want otherwise comment it
if os.path.isfile(output_json_file):
     os.remove(output_json_file)
