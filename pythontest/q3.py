import random as sus
   
def rand_list(length, span):
    return [sus.randrange(span) for item in range(length)]


print(rand_list(10, 5))