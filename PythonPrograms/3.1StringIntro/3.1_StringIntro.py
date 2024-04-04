"""
Write a function called even_chars(str) that
 accepts a string called str and returns True
 if there are an even number of characters in
 the string str and False otherwise.

even_chars(‘real’) → True
even_chars(‘for real’) → True
even_chars(‘not really.’) → False
even_chars(‘4’) → False
even_chars(‘33’) → True
"""

def even_chars(str):
    return len(str) % 2 == 0

even_chars("real")
even_chars("for real")
even_chars("not really.")
even_chars("4")
even_chars("33")

"""
Write a function called middle_char(str)
 that accepts a string called str and 
 returns the middle character in the string.
  If the string has an even number of 
characters, choose the middle character
 with the lower index.

middle_char(‘abc’) → ‘b’
middle_char(‘abcd’) → ‘b’
middle_char(‘abcde’) → ‘c’
middle_char(‘123’) → ‘2’
"""

def middle_char(str):
    return str[(len(str)//2) - 1]

middle_char("abc")
middle_char("abcd")
middle_char("abcde") 
middle_char("123") 



