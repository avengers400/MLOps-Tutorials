import pandas as pd
import os


# Create a sample DataFrame with column names
data = {'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
    }


df = pd.DataFrame(data)

df.loc[len(df.index)] = {'Name':'GF1', 'Age':'20', 'City': 'katihar'}

data_dir = 'data'

os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False )
print(f"File saved to {file_path}")
