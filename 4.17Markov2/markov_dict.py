
from pprint import pprint
from random import randint

def random_picker(lst):
    return lst[randint(0, len(lst)-1)]


def make_markov(string):
    words = string.split()
    markov = {}
    for index in range(len(words)-2):
        if f"{words[index]} {words[index+1]}" not in markov:
            markov[f"{words[index]} {words[index+1]}"] = [words[index+2]]
        else:
            markov[f"{words[index]} {words[index+1]}"].append(words[index+2])

    return markov

words = open("1.txt", "r")
text = words.read()


# pprint(make_markov(text))
word_dict = make_markov(text)

words.close()


def make_sentence(m_dict, word_length):
    sentence = f"{random_picker(list(m_dict.keys()))} "
    while word_length > len(sentence.split()):
        sentence += " "+random_picker(m_dict[f"{sentence.split()[-2]} {sentence.split()[-1]}"]) 
    return sentence

pprint(make_sentence(word_dict, 5))