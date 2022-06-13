import pandas as pd

df = pd.concat(map(pd.read_csv,['Kuwait.csv','Turkey.csv']), ignore_index=True)
print(df)