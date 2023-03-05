import numpy as np
import pandas as pd
from rdkit import DataStructs
from rdkit.Chem import AllChem, MolFromSmiles

# read SMILES strings
df = pd.read_csv("data.csv")

# generate Mol objects
df["mol"] = [MolFromSmiles(smiles) for smiles in df["smiles"]]

# calculate extended connectivity fingerprints (ECFP) =
# Morgan fingerprint with radius 2 and 1024 bits
df["fps"] = [
    AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=1024)
    for mol in df["mol"]
]

# convert the RDKit explicit vectors into numpy arrays
np_fps = []
for fp in df["fps"]:
    arr = np.zeros((1,))
    DataStructs.ConvertToNumpyArray(fp, arr)
    np_fps.append(arr)

np_fps = pd.DataFrame(np_fps)
np_fps.to_csv("morgan_fp.csv", index=False)
