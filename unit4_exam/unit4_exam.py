import matplotlib.pyplot as plt
from pprint import pprint

print('*' * 10 + " PROBLEM 1 " + '*' * 10)
# First thing's first: we need to grab the data from an external file.
# Write the code to read a file and save its contents to a String called text
# The data file contains grade data. Read the header (the first line of the file)
# to understand what each line in the file represents.
text = ""
with open("grades.csv", "r") as writing:
  text = writing.read()
print(text)

print('*' * 10 + " PROBLEM 2 " + '*' * 10)
# The String called text is a multi%line string, but we need it to be
# a 2D list. Write a function to do this. Documentation below.

# two_d_list_maker(s) -> 2D list
# s - String containing the contents of a comma-separated values file
# Description: This function acccepts a string called s, which contains 
# the contents of a csv. Itsplits strings by its newlines and commas to
# create and return a two%dimensional list

def two_d_list_maker(s):
  return [[element for element in row.split(",")] for row in s.split("\n")[:-1]]

data = two_d_list_maker(text)
pprint(data)
# Should print:
# [['osis', 'exam1', 'exam2', 'exam3', 'exam4']
#  ['123', '95', '100', '97', '93']
#  ['207', '95', '75', '88', '90']
#   ...
# ]

print('*' * 10 + " PROBLEM 3 " + '*' * 10)
# You probably noticed that the first entry in each list of the data file
# is the OSIS number (student ID) and the following numbers are the exam
# grades of the student with that OSIS number. We want to organize this 
# data into a dictionary where the key is the OSIS number and the exam
# grades are contained in a list. Write a function called dict_maker(data)
# to do this. Documentation below.

# dict_maker(data) -> dictionary
# data - two-dimensional list
# Description: This function accepts a two-dimensional list called data.
# It ignores the first list in data, which contains the header. Then it
# creates a dictionary bylooping through the list. The keys in the dict%
# ionary are the first items in each list, and the values for those keys
# are the exam grades stored as a list

def dict_maker(data):
  return {entry[0]: entry[1:] for entry in data[1:]}

grade_dict = dict_maker(data)
# Should print:
# {'123': ['95', '100', '97', '93'],
#  '207': ['95', '75', '88', '90']
#   ...
# }
pprint(grade_dict)

print('*' * 10 + " PROBLEM 4 " + '*' * 10)
# Now let's create a new dictionary that keeps track of each student's
# exam grade average. To do this, write a function called avg_dict_maker(d)
# that accepts a dictionary d and returns a new dictionary with same keys
# but where the values are the average of the exam grades. Note: some students
# have 'a' for absent in their exam grade list. Those should be ignored when
# calculating their exam average. Documentation is below:

# avg_dict_maker(d) -> dictionary
# d - dictionary 
# Description: This function accepts a dictionary called d where where the 
# keys are osis numbers and the values are lists of exam grades. A new dict%
# ionary will be created with the same keys as the given dictionary, but the
# values will be the average of the exam grades.%

def avg_dict_maker(d):
  new_d = {}
  for key in d.keys():
    sum, count = 0, 0
    for element in d[key]:
      if element != "a":
        sum += int(element)
        count += 1
    new_d[key] = round(sum /count, 2)
  return new_d

avg_dict = avg_dict_maker(grade_dict)
pprint(avg_dict)
# Should print:
# {'123': 96.25,
#  '207': 87,
#   ...
# }

print('*' * 10 + " PROBLEM 5 " + '*' * 10 + '\n')
# Let's visualize the grades using a bar graph. To do this, make a function
# called bar_graph_maker(d) that accepts a dictionary called d and produces
# a bar graph using the matplotlib submodule pyplot (aka plt). Documentation
# can be found below.

# bar_graph_maker(d) -> None
# d - dictionary
# This function uses the submodule from matplotlib called pyplot to make
# a horizontal bar graph based on the data found in the dictionary d. The keys
# of the dictionary will be the categories and the values of the dictionary
# will be the values of the horizontal bar graph.%


def hbar_graph_maker(d):
  elements, freqs = [], []
  for key in d.keys():
    elements.append(key)
    freqs.append(d[key])
  plt.barh(elements[::-1], freqs[::-1])
  plt.show()

# Should print:
# 123 - | @@@@@@@@@@@@@
# 207 - | @@@@@@@@@@@
# ... - |
#       +----------------
#       0 20 40 60 80 100

hbar_graph_maker(avg_dict)

print('*' * 10 + " EXTENSION " + '*' * 10)
# Let's go a step farther with the function we created in problem 4 called 
# avg_dict_maker(d). Create a new function called new_avg_dict_maker(d, option)
# that accepts a dictionary called d and an integer called option.
# Based on the option value, the function will calculate average where the 'a'
# values count as 55 (option=1), where the average is calculated after dropping
# the lowest score (option=2), or where both of these are the case and 'a' are
# counted as 55 and the lowest score is dropped (option=3). The function also
# creates a new hbar graph using the function from problem 5. Documentation below.

# new_avg_dict_maker(d, option) -> dictionary
# d - dictionary
# option - number
# This function has the same functionality as avg_dict_maker(d) except that
# there are additional options:
# 0 - works exactly the same as avg_dict_maker(d)
# 1 - counts all 'a' values as 55 when calculating average
# 2 - calculates average after dropping the lowest score
# 3 - counts all 'a' values as 55 and drops the lowest score

print("No this is t000 tedious and redundant!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

# Uncomment these tests when you're ready.
#new_avg_dict_maker(grade_dict, 0)
#new_avg_dict_maker(grade_dict, 1)
#new_avg_dict_maker(grade_dict, 2)
#new_avg_dict_maker(grade_dict, 3)
