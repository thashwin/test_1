import pandas as pd
from datasets import load_dataset
# load the training dataset
data = load_dataset('squad')
df = pd.DataFrame(data['train'])
print(df)