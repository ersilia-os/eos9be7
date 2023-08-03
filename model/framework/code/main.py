import sys
import csv
import json
import os
import fcd
import tensorflow as tf
import numpy as np
import warnings
warnings.filterwarnings('ignore')

tf.get_logger().setLevel('INFO')


def replace_zero_with_none(array):
    # Replace 0.0 with None
    array_with_none = np.where(array == 0.0, None, array)
    return array_with_none


input_file = sys.argv[1]
print("input file", input_file)
output_file = sys.argv[2]

try:
    with open(input_file, "r") as f:
        data = json.load(f)
    print("JSON data is loaded successfully.")
    # You can now work with the 'loaded_data' variable, which contains the parsed JSON.
except json.JSONDecodeError as e:
    print("Failed to load JSON data:", str(e))
    # Handle the exception or show an error message.
except FileNotFoundError:
    print("File not found. Make sure the 'data.json' file exists in the current directory.")
    # Handle the case when the file is not found.

fcd_scores = []
count =0
for d in data:
    print("d0",d[0])
    print("d1",d[1])
    print("d",d)
    count = count+1
    print("count",count)
    can_smiles1 = [smi for smi in fcd.canonical_smiles(d[0]) if ((smi is not None))]
    print("Second line", can_smiles1)
    can_smiles2 = [smi for smi in fcd.canonical_smiles(d[1]) if ((smi is not None))]
    print("Third line",can_smiles2)
    try:
        fcd_score = fcd.get_fcd(can_smiles1, can_smiles2)

    except (ValueError, ZeroDivisionError):
        # Handle cases where fcd_score is inf or NAN by setting it to None
        fcd_score = 0.0
        fcd_score = replace_zero_with_none(fcd_score)
        
	
    fcd_scores.append(fcd_score)

print("Total Lists in the json file", count)
with open(output_file, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["fcd_score"])
    for fcd_score in fcd_scores:
        writer.writerow([fcd_score])
