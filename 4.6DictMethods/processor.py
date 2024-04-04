import pprint as p
import string

def return_freqs(text):
    freqs = {}
    line_split = text.split("\n")
    fully_processed = []
    for index in range(len(line_split)):
        for word in line_split[index].split():
            fully_processed.append(word.strip().lower())

    for word in fully_processed:
        if word not in freqs:
            freqs[word] = 1
        else:
            freqs[word] += 1
    
    return freqs

with open("text.txt", "r") as text:
    text = text.read()
    text = text.replace("-"," ").replace("—"," ").translate(str.maketrans('', '', string.punctuation))
    p.pprint(return_freqs(text)) 


