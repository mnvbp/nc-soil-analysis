"""Plotting data"""

import pandas as pd
import matplotlib.pyplot as plt

data = '/Users/manavparikh/Desktop/output/data_edit2.csv'

#named constants
CATEGORY = 'HMA RESULT'


#plot using matplotlib
def plt_continuous(category: str, data: str) -> None:
    data = pd.read_csv(data, delimiter=",", header=0)
    df = data[f'{category}']
    #counting
    df = df.value_counts().rename_axis(f'{category}').reset_index(name='counts')
    #changing column type, sorting, grouping duplicates
    df[f'{category}'] = df[f'{category}']#.astype(float)
    df = df.groupby([f'{category}'], as_index=False).sum()
    df = df.sort_values(by=[f'{category}'], ascending=True)
    #plotting
    x=df[f'{category}']
    y=df['counts']
    plt.plot(x, y)
    plt.xticks(rotation=90)
    plt.show()
    plt.xlabel(f'{category}')
    plt.ylabel('counts')


plt_continuous(category=CATEGORY, data=data)