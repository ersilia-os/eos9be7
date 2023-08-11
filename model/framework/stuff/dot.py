from rdkit import Chem

smiles = "O.O.O.CC1(C)S[C@@H]2[C@H](NC(=O)[C@H](N)c3ccc(O)cc3)C(=O)N2[C@H]1C(O)=O.CCCC" # Contains the DOT separated smiles read from a single column
smiles_to_remove = [] # Stores indices
mols = [Chem.MolFromSmiles(smi) for smi in smiles] # Convert to Molecule objects

i = 0
while i < len(mols):
    if mols[i] is None:
        i += 1
        continue
    
    num_atoms = len(mols[i].GetAtoms())  # Get Atoms in a given Molecule
    if num_atoms == 1:
        smiles_to_remove.extend([i, i+1])
        i += 2
    else:
        i += 1

modified_smiles = []

for idx, smi in enumerate(smiles):
    if idx not in smiles_to_remove:
        modified_smiles.append(smi)

print("modified_smiles",modified_smiles)
