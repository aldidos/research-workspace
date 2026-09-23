import sys
sys.path.append('.')
import pandas as pd

raw_data = [1,2,3,4,5]

sd = pd.Series(raw_data)
df = pd.DataFrame({ 'data' : sd })

print(df['data'].values)
print(len(df['data']))