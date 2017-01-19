import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, save

df = pd.read_csv('lifechart.csv')   # read the data from the lifechart file

# life remaining
life_remaining = []
for l in df['life remaining']:
    life_remaining.append(l)

# current age
current_age = []
for c in df['age']:
    current_age.append(c)
print(current_age)