import pandas as pd

"""
Read data from Qiong-Yang's GitHub repo
(corresponding paper: https://pubmed.ncbi.nlm.nih.gov/33406817/)
They used the METLIN small molecule data set and these files are more
convenient to use as they already contain the SMILES strings.
"""

base_url = "https://raw.githubusercontent.com/Qiong-Yang/GNN-RT/master/data/"
train_set_url = base_url + "SMRT_train_set.txt"
test_set_url = base_url + "SMRT_test_set.txt"

df = pd.concat(
    [pd.read_csv(train_set_url, sep="\t"), pd.read_csv(test_set_url, sep="\t")]
)

df.to_csv("data.csv", index=False)
