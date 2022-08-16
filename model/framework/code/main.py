import sys
import csv
import json
import fcd

input_file = sys.argv[1]
output_file = sys.argv[2]
smiles_list1_orig = []
smiles_list2_orig = []

with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        smiles_list1_orig.append(row[0])
        smiles_list2_orig.append(row[1])
        
#Filter empty strings
smiles_list1 = [smi for smi in smiles_list1_orig if smi]
smiles_list2 = [smi for smi in smiles_list2_orig if smi]

#Get canonical smiles and filter invalid ones
can_smiles1 = [smi for smi in fcd.canonical_smiles(smiles_list1) if ((smi is not None))]
can_smiles2 = [smi for smi in fcd.canonical_smiles(smiles_list2) if ((smi is not None))]

#Make prediction using default ChemNet model
print(can_smiles1)
print(can_smiles2)
fcd_score = fcd.get_fcd(can_smiles1, can_smiles2)

#Write output
with open(output_file, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["fcd_score"]) # header
    writer.writerow([fcd_score])
