import sys
import csv
import json
import os
from fcd import canonical_smiles, get_fcd
import numpy as np
import warnings
import pandas as pd
warnings.filterwarnings('ignore')


def replace_zero_with_none(array):
    # Replace 0.0 with None
    array_with_none = np.where(array == 0.0, None, array)
    return array_with_none

input_file = sys.argv[1]
output_file = sys.argv[2]

df = pd.read_csv(input_file, names=["smiles_1", "smiles_2"], header=0)
smiles_lists = df.apply(lambda row: [row['smiles_1'].split('.'), row['smiles_2'].split('.')], axis=1)
print(smiles_lists)

fcd_scores = []
count =0
for d in smiles_lists:
    can_smiles1 = [canonical_smiles(smi) for smi in d[0] if smi is not None]
    can_smiles2 = [canonical_smiles(smi) for smi in d[1] if smi is not None]
   
    try:
        fcd_score = get_fcd(can_smiles1, can_smiles2)
        print(fcd_score)

    except (ValueError, ZeroDivisionError):
        # Handle cases where fcd_score is inf or NAN by setting it to None
        fcd_score = 0.0
        fcd_score = replace_zero_with_none(fcd_score)
        
	
    fcd_scores.append(fcd_score)

with open(output_file, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["fcd_score"])
    for fcd_score in fcd_scores:
        writer.writerow([fcd_score])
