# test_with_pytest.py
from sklearn import datasets
import pandas as pd
from ..Script.example_notebook import read_sk_dataset

def test_read_sk_dataset():
    new_dataset = datasets.load_iris()
    df_iris = read_sk_dataset(new_dataset)
    assert type(df_iris) == pd.DataFrame