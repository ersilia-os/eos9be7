from rdkit import Chem
import fcd
import tensorflow as tf

def convert_smiles_to_canonical(smi):
    mol = Chem.MolFromSmiles(smi)
    if mol is None:
        return None
    canonical_smiles = Chem.MolToSmiles(mol)
    return canonical_smiles

def are_smiles_exact_same(smi1, smi2):
    mol1 = Chem.MolFromSmiles(smi1)
    mol2 = Chem.MolFromSmiles(smi2)

    if mol1 is None or mol2 is None:
        return False

    return mol1.HasSubstructMatch(mol2) and mol2.HasSubstructMatch(mol1)

if __name__ == "__main__":
    # Example usage
    smi = "CC1C2C(CC3(C=CC(=O)C(=C3C2OC1=O)C)C)O"
    # CC1C2C(CC3(C=CC(=O)C(=C3C2OC1=O)C)C)O
    # C1=CN=CC=C1C(=O)NN
    # CC(CN1C=NC2=C(N=CN=C21)N)OCP(=O)(O)O
    can_smiles1 = [smi for smi in fcd.canonical_smiles(smi) if ((smi is not None))]
    print("fcs",can_smiles1)
    canonical_smi = convert_smiles_to_canonical(smi)
    print("Original SMILES:", smi)
    print("Canonical SMILES:", canonical_smi)

    if are_smiles_exact_same(smi, canonical_smi):
        print("Both SMILES are exactly the same.")
    else:
        print("SMILES are different.")