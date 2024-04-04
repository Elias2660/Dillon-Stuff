# This is a python library that we will use to generate random numbers
import random


#==================================================
# Problem 0

# random.randrange( limit ) is a python function that returns a
# random integer in the range [0, limit)

# Write a function that will create and return a list of size n that
# is filled with random integers in the range [0, limit)

def rand_list(n, limit):
    g = []
    for x in range(n):
        g.append(random.randrange(limit))
    
    return g

# When printed, a and b should have different values.
print( 'Random List Tests')
a = rand_list(10, 10)
b = rand_list(10, 10)
print(a)
print(b)
print('==================================================')

# End Problem 0
#==================================================


#==================================================
# Problem 1
# Write a function that takes a list of non-negative integer
# values and returns a string of a bar graph representation of the list.
# The length of each bar should be the same as the value at that index.
# That means if g[0] = 9, then the first bar should have a length of 9.

def bar_graph(g):
    s = ""
    for index in range(10):
        equals = "=" * g[index]
        s += f"{index}: {equals}\n"
    return s

# The code below should have this output:
# 0: =========
# 1: =====
# 2: =====
# 3: ===
# 4: =
# 5: =====
# 6: =========
# 7: =====
# 8: =======
# 9: ========
print('Bar Graph Tests')
test = [9, 5, 5, 3, 1, 5, 9, 5, 7, 8]
print(bar_graph(test))

# This should print out the bar graph for your random
# lists from Problem 0
print(bar_graph(a))
print(bar_graph(b))
print('==================================================')

# End Problem 1
#==================================================


#==================================================
# Problem 2

# Write a function that returns the average of the
# values in a list. You may assume that the argument
# provided is a list that only contains number.

def list_avg( g ):
    return sum(g)/len(g)

print('Average tests')
# This should print 5.7
print( list_avg(test) )

# This should print out the averages of your random
# lists from Problem 0
print( list_avg(a) )
print( list_avg(b) )
print('==================================================')

# End problem 2
#==================================================


#==================================================
# Problem 3

# Write a function that returns the number of times
# the value n appears in list g.

def count(n, g):
    c = 0
    for number in g:
        c += 1 if number == n else 0
    return c

print('Count Test')
# This should print 4
print( count(5, test) )
print('==================================================')

# End Problem 3
#==================================================


#==================================================
# Problem 4

# Write a function that returns the mode (most frequently
# appearing value) of a given list.
# It should only return a single value, even if there are
# multiple modes, just return one of them.


def find_mode(g):
    dict = {x:0 for x in range(10)}
    for item in g:
        dict[item] += 1
    best_num = 0
    for index in range(1, 10):
        if dict[index] > dict[best_num]:
            best_num = index
    return best_num

print('Mode Tests')
# Should print 5
print( find_mode(test) )

print( find_mode(a) )
print( find_mode(b) )
print('==================================================')

#==================================================
# Problem 5

# Write a function that keeps track of the frequencies of values
# from a list containing only integers.
# For example, if the provided list only contained 0s and 1s,
# and there were 8 0s and 23 1s, then the fucntion should
# return this list: [8, 23]
# It is important to understand that each index in the new
# list represents a value from the parameter list. So the new
# list needs to be as large as the biggest value in the parameter.
def list_counts(g, max_value):
    counts = [0] * (max_value) 
    dict = {x:0 for x in range(max_value)}
    for item in g:
        dict[item] += 1

    for index in range(max_value):
        counts[index]  = dict[index]
    return counts

print('List Count Tests')
# Should print
# [0, 1, 0, 1, 0, 4, 0, 1, 1, 2]
test_counts = list_counts( test, 10 )
print( test_counts )

print( list_counts(a, 10) )
print( list_counts(b, 10) )

# create a new list of 10 random values in the range [0, 5)
# print that list
# YOUR CODE HERE


# create a list that correctly counts all the values in
# the new list you just made.
# print that list
# YOUR CODE HERE

print('==================================================')

# End Problem 5
#==================================================

#==================================================
# Problem 6
# If you use bar_graph on a list with sufficiently large
# values, you'll have a problem with the bars taking up
# more than one line.

# Write a new bar_graph function that will draw a scaled bar
# graph. It should take an argument for the scale factor,
# such that 1 piece of a bar represents 1 quantity equal
# to the scale factor.

def bar_graph_scaled(g, scale_factor):
    s = ""
    for index in range(len(g)):
        equals = "=" * (g[index] // scale_factor)
        s += f"{index}: {equals}\n"
    return s

print('Scaled Bar Graph Test')
# Should print:
# 0: =====
# 1: ======
# 2: =
scale_test = [500, 670, 125]
print(bar_graph_scaled(scale_test, 100))

# now let's try it on a list with very large values
big_list = rand_list(10, 1000)
print( bar_graph_scaled(big_list, 25))
print('==================================================')

# End Problem 6
#==================================================


#==================================================
# Problem 7

# random.randrange() distributes numbers evenly, meaning
# that every possible random value has an equal chance
# of being returned.

# How could you test how evenly random.randrange()
# distributes the results?
# YOUR ANSWER AS COMMENTS BELOW
"""
ANSWER

you could use a large test, get the frequencies of the numbers, and then
graph them in a bar graph"""
#
# Write code below that performs the test you described.
# YOUR ANSWER BELOW
lst = rand_list(10000, 10)
freq_list = list_counts(lst, 10)
bar = bar_graph_scaled(freq_list, 100)
print(bar)




print('==================================================')

# End Problem 7
#==================================================


#==================================================
# Problem 8

# There is a different way of getting random numbers
# random.normalvariate(m, s) returns a random floating point
# value using what is called a "normal distribution".

# The function below will generate a list of n integers
# using a normal distribution that will have a mean
# value of m
def normal_rand_list(n, m):
    g = []
    i = 0
    while i < n:
        g.append( int(random.normalvariate(m, 1)) )
        i+= 1
    return g

# This is an example of using normal_rand_list
# Feel free to look at its values
normal_list = normal_rand_list(10, 5)


# Use a similar process as you did in problem 7
# to try and figure out what the differece is between
# the normal distribution and the distribution of random.randrange

lst =  normal_rand_list(10000, 5)
freq_list = list_counts(lst, 10)
bar = bar_graph_scaled(freq_list, 100)
print(bar)


# Describe the difference between the two distributions below.
# Cite the evidence from your tests
"""
ANSWER

The randrange gives a random list that gives equally random probabilities
 for each number in the range (approx. equal lengths for bars),
 while
the normalvariate function gives a list that gives a higher priority
 for numbers closer to the mean (the longer the bars the closer to five)

RANDRANGE
0: =========
1: ==========
2: =========
3: =========
4: =========
5: ==========
6: ==========
7: ==========
8: =========
9: =========

NORMAL VARIATE:
0: 
1: 
2: =
3: ==============
4: =================================
5: ==================================
6: =============
7: ==
8: 
9: 
"""
# End Problem 8
#==================================================
