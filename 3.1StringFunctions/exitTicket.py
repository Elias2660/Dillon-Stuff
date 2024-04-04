"""
Directions
Write the documentation and code for a function called count_consonants(s)
 that returns the number of occurrences of consonants in the string s. 
 Assume s is 0 or more characters long.

Your screenshot should include documentation, code, and results
"""

"""
DESCIPTION
Returns the number of occurances of consonats in string s.

CONTRACT
string -> int

"""

consonants = list("BCDFGHJKLMNPQRSTVWXYZ".lower())

def count_consonants(str):
    num = 0
    for char in str:
        num += 1 if char.lower() in consonants else 0
    return num



#unit tests
print(
    count_consonants("hello world"), #7
    count_consonants("rick astley"), #7
    count_consonants("845234636347529[[';;['/.;'/.]]]") #0
)