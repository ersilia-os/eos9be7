import sys
import csv
import json
import os
import fcd
import tensorflow as tf
import numpy as np
import warnings
import pandas as pd
warnings.filterwarnings('ignore')

tf.get_logger().setLevel('INFO')


def replace_zero_with_none(array):
    # Replace 0.0 with None
    array_with_none = np.where(array == 0.0, None, array)
    return array_with_none

input_file = sys.argv[1]
output_file = sys.argv[2]

df = pd.read_csv(input_file, names=["smiles_1", "smiles_2"], header=0)
print("dataframe", df.columns)
smiles_lists = df.apply(lambda row: [row['smiles_1'].split('.'), row['smiles_2'].split('.')], axis=1)
print(smiles_lists)

fcd_scores = []
count =0
for d in smiles_lists:
    can_smiles1 = [fcd.canonical(smi) for smi in d[0] if smi is not None]
    print("List 1", can_smiles1)
    can_smiles2 = [fcd.canonical(smi) for smi in d[1] if smi is not None]
    print("List 2",can_smiles2)
   
    try:
        fcd_score = fcd.get_fcd(can_smiles1, can_smiles2)
        print(fcd_score)

    except (ValueError, ZeroDivisionError):
        # Handle cases where fcd_score is inf or NAN by setting it to None
        print("here")
        fcd_score = 0.0
        fcd_score = replace_zero_with_none(fcd_score)
        
	
    fcd_scores.append(fcd_score)

with open(output_file, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["fcd_score"])
    for fcd_score in fcd_scores:
        writer.writerow([fcd_score])
