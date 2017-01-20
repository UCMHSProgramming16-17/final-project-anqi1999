import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, save

df = pd.read_csv('uglylifechart.csv')   # read the data from the lifechart file

# life remaining
life_remaining = []
for l in df['life remaining']:      # for each 'item' in the column 'life remaining'
    life_remaining.append(l)       # add 'item' to the list 'life_remaining'

# current age
current_age = []
for c in df['age']:     # for each 'item' in the column 'age'
    current_age.append(c)       # add 'item' to the list 'current_age'

# output to static html file
output_file('line.html')

p = figure(plot_width=400, plot_height=400)

# create the circles
p.circle(current_age, life_remaining, size=10, color='lavender', alpha=0.5)

save(p)