import pandas as pd

df = pd.read_csv("big-mac-full-index.csv")

print("Using iterrows() method:")
for index, row in df.iterrows():
    big_mac_index = row['local_price'] / row['dollar_ex']
    print(row['name'], "- Big Mac Index:", big_mac_index)

def calculate_big_mac_index(row):
    return row['local_price'] / row['dollar_ex']

print("\nUsing apply() method:")
df['Big Mac Index'] = df.apply(calculate_big_mac_index, axis=1)
for index, row in df.iterrows():
    print(row['name'], "- Big Mac Index:", row['Big Mac Index'])
