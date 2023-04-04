"""
Python file for running some example code
"""

from sklearn.datasets import load_iris
import pandas as pd

DATA_DESTINATION = "data/iris.parquet"

# load iris dataset from sklearn
iris = load_iris()

# load a sample dataset into a Pandas dataframe
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# export the dataset to parquet
df.to_parquet(DATA_DESTINATION)

print(pd.read_parquet(DATA_DESTINATION).head())
