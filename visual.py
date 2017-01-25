import pandas as pd
import numpy as np
from bokeh.charts import Scatter, output_file, save

df = pd.read_csv('uglylifechart.csv')   # read the data from the lifechart file

# life remaining
life_remaining = []
for l in df['life remaining']:      # for each 'item' in the column 'life remaining'
    life_remaining.append(l)       # add 'item' to the list 'life_remaining'

# current age
current_age = []
for c in df['age']:     # for each 'item' in the column 'age'
    current_age.append(c)       # add 'item' to the list 'current_age'

p = Scatter(df, x='age', y='life remaining', xlabel='current age', ylabel='life remaining', title='determine how long you have left to live')

# file
output_file('life.html')

# create the circles
p.circle(current_age, life_remaining, size=10, color='lavender', alpha=0.5)

save(p)