#Please do all parts of this lab. Answer questions in a way that demonstrates you understand.
#Curt, lazy answers will be penalized appropriately.

#==================================================
# Problem 0

# Reminder:  For the first 128 characters, ASCII and UTF-8 are the same and interchangeable.

# Write a function, encode_table(), that should print out
# each letter from a-z, along with its UTF-8 value, use one line per character.
# Each line should look like this:
#     a: 97
# The function does not need to return anything.

def encode_table():
    for x in range(97, 97 + 26):
        print(f"{chr(x)} : {x}")


print(('=' * 10) + "Problem 0" + ('=' * 10))
encode_table()
# End Problem 0
#==================================================

#==================================================
# Problem 1

# There is a cipher (https://en.wikipedia.org/wiki/Cipher) called rot13
# The following shows how to "encrypt" something in rot13:

# a b c d e f g h i j k l m n o p q r s t u v w x y z
# n o p q r s t u v w x y z a b c d e f g h i j k l m

# 'hello' in rot13 becomes 'uryyb'

# Look at the Unicode values from encode_table()
# what can you tell about a letter and its rot13 equivalent?
# print your answer as a string below

print(('=' * 10) + "Problem 1" + ('=' * 10))
answer = 'You just have to add the equivalent of 13, if above 122, go back to 97'
print(answer)

# End Problem 1
#==================================================

#==================================================
# Problem 2

# Write a function that takes a single character string
# as a parameter and returns its rot13 equivalent.
# If the character is not a lowercase letter then
# return the original character.
# for example rot13char("b") would return "o"

def rot13char(c):
    if not (ord(c) <= 122 and  ord(c) >= 97):
        return c
    return chr((ord(c)-84)%26+97)

print(('=' * 10) + "Problem 2" + ('=' * 10))
print( 'b: ' + rot13char('b') )
print( 'q: ' + rot13char('q') )
print( 'B: ' + rot13char('B') )
print( 'Q: ' + rot13char('Q') )
print( '?: ' + rot13char('?') )
print( '$: ' + rot13char('$') )

# End Problem 2
#==================================================


#==================================================
# Problem 3

# Write a function that prints out all the characters
# from 'a' to 'z' along with their rot13 equivalents.
# Like problem 0, each letter should be on its own line.
# A line of this string might look like:
#       h <-> u

def rot13_table():
    for x in range(97, 97+26):
        print(f"{chr(x)} : {rot13char(chr(x))}")

print(('=' * 10) + "Problem 3" + ('=' * 10))
rot13_table()

# End Problem 3
#==================================================

#==================================================
# Problem 4
# Write a function that will take a string consisting of
# lowercase letters only and will return its rot13 equivalent.

# For example, rot13("skywalker") would return "fxljnyxre"

def rot13(s):
    end_str = ""
    for char_index in range(len(s)):
        end_str  += rot13char(s[char_index])
    return end_str
        

print(('=' * 10) + "Problem 4" + ('=' * 10))
tester = 'skywalker'
rotted = rot13(tester)
print( tester + ' -> ' + rotted )

# What happens when you call rot13 on a string that was created by rot13?
# print out your answer as a string
answer = 'It rotates back to itself.'
print(answer)

# End Problem 4
#==================================================

#==================================================
# Problem 5

# Go back to problem 2, create a new version below such
# that it now works with both upper and lower case letters.
def rot13char_anycase(c):
    if c.upper() == c:
        return rot13char(c.lower()).upper()
    return rot13char(c)

# Test your function here


print(('=' * 10) + "Problem 5" + ('=' * 10))

print(rot13char_anycase("T"))
print(rot13char_anycase("汉"))
print(rot13char_anycase("字"))



# End Problem 5
#==================================================

#==================================================
# Problem 6

# Look back to problem 4, create a new version below
# that can take a string with any characters in it,
# but will only modify letters, upper or lowercase,
# leaving spaces, numbers and punctuation unchanged.
#
# Hint: If you've gotten to this point, most of the
# work has already been done.

def rot13_full(s):
    end_str = ""
    for char_index in range(len(s)):
        end_str  += rot13char_anycase(s[char_index])
    return end_str


print(('=' * 10) + "Problem 6" + ('=' * 10))
print(rot13_full("Nerf Ares, gel sync pyrex. Terra hey!"))
# Test your function here


lyrics = """Almost heaven, West Virginia
Blue Ridge Mountains, Shenandoah River
Life is old there, older than the trees
Younger than the mountains, growin' like a breeze\n\n
Country roads, take me home
To the place I belong
West Virginia, mountain mama
Take me home, country roads\n\n
All my memories gather 'round her
Miner's lady, stranger to blue water
Dark and dusty, painted on the sky
Misty taste of moonshine, teardrop in my eye\n\n
Country roads, take me home
To the place I belong
West Virginia, mountain mama
Take me home, country roads\n\n
I hear her voice in the mornin' hour, she calls me
The radio reminds me of my home far away
Drivin' down the road, I get a feelin'
That I should've been home yesterday, yesterday\n\n
Country roads, take me home
To the place I belong
West Virginia, mountain mama
Take me home, country roads\n\n
Country roads, take me home
To the place I belong
West Virginia, mountain mama
Take me home, country roads\n\n
Take me home, (down) country roads
Take me home, (down) country roads

"""

print(rot13_full("HDHJHjdsHdksaD"))
print(rot13_full("The quick brown fox jumps over the lazy dog"))
print(rot13_full(lyrics))

lyrics_2 = """
r'er ab fgenatref gb ybir
Lbh xabj gur ehyrf naq fb qb V (qb V)
N shyy pbzzvgzrag'f jung V'z guvaxvat bs
Lbh jbhyqa'g trg guvf sebz nal bgure thl
V whfg jnaan gryy lbh ubj V'z srryvat
Tbggn znxr lbh haqrefgnaq
Arire tbaan tvir lbh hc
Arire tbaan yrg lbh qbja
Arire tbaan eha nebhaq naq qrfreg lbh
Arire tbaan znxr lbh pel
Arire tbaan fnl tbbqolr
Arire tbaan gryy n yvr naq uheg lbh
Jr'ir xabja rnpu bgure sbe fb ybat
Lbhe urneg'f orra npuvat, ohg lbh'er gbb ful gb fnl vg (fnl vg)
Vafvqr, jr obgu xabj jung'f orra tbvat ba (tbvat ba)
Jr xabj gur tnzr naq jr'er tbaan cynl vg
Naq vs lbh nfx zr ubj V'z srryvat
Qba'g gryy zr lbh'er gbb oyvaq gb frr
Arire tbaan tvir lbh hc
Arire tbaan yrg lbh qbja
Arire tbaan eha nebhaq naq qrfreg lbh
Arire tbaan znxr lbh pel
Arire tbaan fnl tbbqolr
Arire tbaan gryy n yvr naq uheg lbh
Arire tbaan tvir lbh hc
Arire tbaan yrg lbh qbja
Arire tbaan eha nebhaq naq qrfreg lbh
Arire tbaan znxr lbh pel
Arire tbaan fnl tbbqolr
Arire tbaan gryy n yvr naq uheg lbh
Jr'ir xabja rnpu bgure sbe fb ybat
Lbhe urneg'f orra npuvat, ohg lbh'er gbb ful gb fnl vg (gb fnl vg)
Vafvqr, jr obgu xabj jung'f orra tbvat ba (tbvat ba)
Jr xabj gur tnzr naq jr'er tbaan cynl vg
V whfg jnaan gryy lbh ubj V'z srryvat
Tbggn znxr lbh haqrefgnaq
Arire tbaan tvir lbh hc
Arire tbaan yrg lbh qbja
Arire tbaan eha nebhaq naq qrfreg lbh
Arire tbaan znxr lbh pel
Arire tbaan fnl tbbqolr
Arire tbaan gryy n yvr naq uheg lbh
Arire tbaan tvir lbh hc
Arire tbaan yrg lbh qbja
Arire tbaan eha nebhaq naq qrfreg lbh
Arire tbaan znxr lbh pel
Arire tbaan fnl tbbqolr
Arire tbaan gryy n yvr naq uheg lbh
Arire tbaan tvir lbh hc
Arire tbaan yrg lbh qbja
Arire tbaan eha nebhaq naq qrfreg lbh
Arire tbaan znxr lbh pel
Arire tbaan fnl tbbqolr
Arire tbaan gryy n yvr naq uheg lbh
"""

print(rot13_full(lyrics_2))
# End Problem 6
#==================================================
# Rot13 is very weak encryption. The Caesar Ciper can rotate by any number.
#How much does this help if you applied it to a sentence in English?
#What could you do to break this kind of encryption with the power of python?
# print out your answer as a string 
answer = '''There are only 26 possible rotations, so its easy to shift
this by 26 times and find the thing that makes sense. First shift by one,
then by two, etc.'''
print(answer)
