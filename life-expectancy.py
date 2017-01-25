# How much longer am I expected to live, given my sex, age, and country?
import requests
import csv
import datetime
import math

# PARAMETERS:
# sex
sex = ['male', 'female']

u_sex = []
for each in range(82):
    u_sex.append('male')
    u_sex.append('female')

# country
c_url = 'http://api.population.io:80/1.0/countries'     # get the available list of countries
c = requests.get(c_url)
c_list = c.json()
c_available = c_list['countries']

country = input('Country? Preferably its official name, and in proper English. ')      # get user's input
if country not in c_available:
    for each in c_available:
        print(each)
    country = input('Sorry, what you typed is invalid. :/ Here is a list of the available countries, with, hopefully, the correct version of your country on there. Either you misspelled, did not capitalize properly, or mistyped the official name of your country. Try again. ')

# age
age = []
for num in range(81):
    age.append(str(num) + 'y')
    
actual_age = [0]    # this one will be used for 'uglylifechart'
num = 0
while num != 83:
    actual_age.append(num)
    num += 1
    actual_age.append(num)

# date
date = str(datetime.date.today())

# ~~~~~~~~~~~~~~~~~~~~~~~~~

# FUNCTION TO CONVERT FROM YEARS DECIMAL TO 'YEARS, MONTHS, DAYS':
# set empty variable
life_expectancy = 'blah'

# define function
def years(remaining):
    global life_expectancy
    
    rem = float(remaining)       # convert 'remaining' to a float
    year = math.floor(rem)       # number of full years
    m = (rem - year) * 12       # months left over
    month = math.floor(m)       # number of full months
    d = (m - month) * 30.4375       # days left over (30.4375 is the average number of days per month)
    day = math.floor(d)       # number of full days
    
    life_expectancy = str(year) + ' years, ' + str(month) + ' months, ' + str(day) + ' days'

# ~~~~~~~~~~~~~~~~~~~~~~~~~

# FUNCTION FOR THE REMAINING LIFE API:
# set empty variable
remaining = 'blah'

# define function
def api():
    global remaining
    
    endpoint = 'http://api.population.io:80/1.0/life-expectancy/remaining/'     # remaining lifetime api
    url = endpoint + s + '/' + country + '/' + date + '/' + a
    r = requests.get(url)
    stats = r.json()
    remaining = stats['remaining_life_expectancy']

# ~~~~~~~~~~~~~~~~~~~~~~~~~

# CSV:
# new csv file
lifechart = open('lifechart.csv', 'w', newline='')

# create the writer
w = csv.writer(lifechart, delimiter=',')

# write to the file
w.writerow(['age', 'sex', 'life remaining'])
for a in age:
    for s in sex:
        api()       # call api function for remaining life expectancy
        years(remaining)        # call years converter function
        w.writerow([a, s, life_expectancy])     # write 'age', 'sex', and 'remaining life expectancy' to the file
            
# close file
lifechart.close()

print('Open the lifechart, and scroll through until you reach your age. Happy searching.')

# ~~~~~~~~~~~~~~~~~~~~~~~~~

# UGLIER CSV FILE:
# new file
uglylifechart = open('uglylifechart.csv', 'w', newline='')

# create the writer
u = csv.writer(uglylifechart, delimiter=',')

# write to the file
u.writerow(['age', 'sex', 'life remaining'])
u_remaining = []
for a in age:
    for s in sex:
        api()
        u_remaining.append(remaining)
        
for x in range(162):
    u.writerow([actual_age[x], u_sex[x], u_remaining[x]])
        
uglylifechart.close()