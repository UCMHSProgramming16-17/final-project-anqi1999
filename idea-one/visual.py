import pandas as pd
import requests
import csv
import datetime
import math
from bokeh.plotting import figure, output_file, save
from bokeh.models import HoverTool
import life_expectancy

life_expectancy.an_approximation_of_how_long_you_have_until_you_die()

df = pd.read_csv('uglylifechart.csv')   # read the data from the lifechart file

# life remaining
life_remaining = []
for l in df['life remaining']:      # for each 'item' in the column 'life remaining'
    life_remaining.append(l)       # add 'item' to the list 'life_remaining'

# current age
current_age = []
for c in df['age']:     # for each 'item' in the column 'age'
    current_age.append(c)       # add 'item' to the list 'current_age'


p = figure(plot_width=1500, plot_height=900, x_axis_label='current age', y_axis_label='life remaining', tools=[hover])

# create the circles
for x in range(2, 162):
    if x % 2 == 0:
        p.circle(current_age[x], life_remaining[x], size=10, color='#404387', alpha=0.5)
    else:
        p.circle(current_age[x], life_remaining[x], size=10, color='#22A784', alpha=0.5)


# file
output_file('life.html')

save(p)