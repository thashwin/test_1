import pandas as pd

# load the training dataset
data = pd.read_csv('data/wine.csv')
data.sample(10)
