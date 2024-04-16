import pandas as pd


input = '/Users/manavparikh/Desktop/output/data_edit2.csv'
output = '/Users/manavparikh/Desktop/output/county.csv'

df = pd.read_csv(input)

df2 = df.groupby('COUNTY')

df2 = df2.mean()
#df2 = df2['COUNTY'].str.lower()
#df2 = df2['COUNTY'].str.capitalize()
df2n = df2.rename(columns={'COUNTY': 'County'})

print(df2n)
print(df2)

#df2.to_csv(output)