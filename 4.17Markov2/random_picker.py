from random import randint

def random_picker(lst):
    return lst[randint(0, len(lst)-1)]


words = ["red","blue","green","fuchsia"]

for i in range(20):
  print(random_picker(words),end=" ")#should print all 4 words.
print()


