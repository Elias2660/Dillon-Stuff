"""
Directions
Write a function called is_question(str) that accepts a string called
 str and returns True only if the last character of str is ‘?’ and returns False otherwise.
Include documentation (contract, description, three tests) and code.

Please include a screenshot of your documentation, code, and test results.
"""

"""
CONTRACT
is_question(str)
str -> bool

DESCRIPTION
returns True if the last letter is "?," otherwise return false

"""

def is_question(str):
    return str[-1] == "?"


print(is_question("helloworld")) #false
print(is_question("helloworld?")) #true
print(is_question("no!!!!")) #false
print(is_question("Yes? Whoops!")) #false