from pprint import pprint
#==================================================
print(('=' * 10) + "Problem 0" + ('=' * 10))
# There is a file called 'nyc_pop.csv' that you can find in
# the same place as this lab file. Download it and put it
# in the same directory as this file. It may help to view the
# "Raw" version of the nyc_pop.csv file on github.

# Write code that will open 'nyc_pop.csv' and the read its
# contents into a string called text.
#
# YOUR CODE HERE
pop_file = 0
text = ''

# You may notice an extra newline after the file, this can
# happen if there are any blank lines after the file. There
# is a python method called strip that will return a copy of
# with extra whitespace (space, newlines, tabs) removedfrom the
# beginning and end of a string. The code below uses strip to
# get rid of any extra whitespace on the ends of text.
text = ''
print(text)

# End Problem 0
#==================================================

#==================================================
print(('=' * 10) + "Problem 1" + ('=' * 10))
# Problem 1
#
# You should notice that the file contains population data for
# The boroughs of NYC from 1790 - 2010. It is formatted such that
# Each line represents one year, and contains a series of numbers
# separated by ','. This is a common way of representing data in
# plain text, since it is easily accessible in programming. The
# file type is called 'comma separated value' or 'csv'.

# Often, the first line of a .csv file will contain the headers
# that describe what each value represents.

# Write a function that will take a string representing the text
# of a file that looks similar to 'nyc_pop.csv' and returns a list
# that contains only the headers.
def get_headers(s):
    g = []
    return g


# End Problem 1
#==================================================

#==================================================
print(('=' * 10) + "Problem 2" + ('=' * 10))
# Problem 2
#
# Write a function that will take a string representing the text
# of file that looks similar to 'nyc_pop.csv' and returns a list of
# lists.
# Each sublist should represent a line from the file.
# Each element in a sublist should represent one value.
def get_data(s):
    data = []
    return data

# Should print:
# [['1790', '33131', '4549', '6159', '1781', '3827'], ['1800', '60515', '5740', '6642', '1755', '4563'],
# There will be more sublists after that.
pop_data = get_data(text)
pprint(pop_data)

# End Problem 2
#==================================================

#==================================================
print(('=' * 10) + "Problem 3" + ('=' * 10))
# Problem 3
#
# Write a function that will take a list of lists similar to pop_data,
# where every element is a string, and creates a dictionary where the
# the keys are the years, as strings, and the values are the lists of
# population numbers for the given year, as numbers. Note that the
# key is also at index 0 in a given list.

# The first list is: ['1790', '33131', '4549', '6159', '1781', '3827']
# As a dictionary entry, it would look like this:
# {'1790': [33131, 4549, 6159, 1781, 3827]}
#
def make_year_dict(data):
    year_d = {}
    return year_d

pop_dict = make_year_dict(pop_data)
pprint(pop_dict)

# End Problem 3
#==================================================

#==================================================
print(('=' * 10) + "Problem 4" + ('=' * 10))
# Problem 4

# The data in each value of pop_dict represents borough information,
# but that is currently not clear.

# Write a function that takes a dictionary created by make_year_dict,
# and a list of headers.
# Ths function should modify each value in the paramater dictionary to
# be dictionaries where the keys are headers from the provided header list
# and the values are the corresponding numbers from the existing value list.

# For example, the first year entry is currently:
# {'1790': [33131, 4549, 6159, 1781, 3827],
# After this function runs, it should be:
# {'1790': {'Bronx': 1781, 'Brooklyn': 4549, 'Manhattan': 33131, 'Queens': 6159,'Staten Island': 3827},

# Note the header list contains 'Year', but that does not have a corresponding
# value in the value lists.

def combine_dict(year_dict, headers):
    year_dict = {}
        
combine_dict(pop_dict, pop_headers)
pprint(pop_dict)

# End Problem 4
#==================================================

#==================================================
print(('=' * 10) + "Problem 5" + ('=' * 10))

# Write a function that will take as a parameter a dictionary
# created by make_year_dict and then modified by combine_dict.
# It should add a new entry to each year dictionary with a key of
# 'total' and a value that is the total population of all 5 boroughs.

def add_totals(d):
    d = {}
            
add_totals(pop_dict)
pprint(pop_dict)

# End Problem 5
#==================================================

#==================================================
print(('=' * 10) + "Problem 6" + ('=' * 10))
# Problem 6
#
# What was all of this for?

# Computer programming is an invaluable tool when it comes to
# data analysis. But before we can analyze the data, we need to
# get it in a form that python understands, as opposed to text.
# You've just taken raw text, and converted it into a python structure
# (specifically, a dictionary), that we can now use to help answer
# real questions about the data.

# Use code to answer the following questions. Print statements are
# already provided, update each ansX variable with the correct answer.
# you made add other variables if needed.

# What years do we have population data for?
ans0 = []
print('years with data:', ans0)

# How many people lived in NYC in 1880?
ans1 = 0
print('nyc population 1880:', ans1)

# How many people lived in NYC in 2010?
ans2 = 0
print('nyc population 2010:', ans2)

# How many people lived in Brooklyn in 1970?
ans3 = 0
print('bk population 1970:', ans3)

# What was the change in total population from 1900 to 2000?
ans4 = 0
print('nyc population change, 1900 - 2000:', ans4)

# What percentage of the total NYC population did Queens account for in 2010?
ans5 = 0
print('% queens of total nyc population 2010:', ans5)


# Come up with your own question that can be answered using the population data.
# What is your question:
question = ''
#
# What is the answer? (also the code to find your answer)
ans6 = ''
print(question, ans6)

# End Problem 6
#==================================================
