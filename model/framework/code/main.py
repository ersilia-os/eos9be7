import sys
import csv
import json
import os
import fcd
import tensorflow as tf

#Disable different Tensorflow error messages/outputs
tf.get_logger().setLevel('INFO')


input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r") as f:
    data = json.load(f)

fcd_scores = []
for d in data:
    can_smiles1 = [smi for smi in fcd.canonical_smiles(d[0]) if ((smi is not None))]
    can_smiles2 = [smi for smi in fcd.canonical_smiles(d[1]) if ((smi is not None))]
    fcd_scores += [fcd.get_fcd(can_smiles1, can_smiles2)]

with open(output_file, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["fcd_score"])
    for fcd_score in fcd_scores:
        writer.writerow([fcd_score])
