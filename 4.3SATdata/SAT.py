with open("2012_Sat_Results.csv", "r") as text:
    data = text.read().split("\n")


data.pop()
new = []
for d in data:
    new.append(d.split(","))
data = new

"""
Remove any schools that contain "s" as the scores
(remove that entire line from the dataList, not just the name or the s's)
"""
new = []
for d in data:
    if "s" not in d:
        new.append(d)

data = new


"""
Remove the DBN column from each list. (including the header)
"""

for d in data:
    d.pop(0)


"""
Replace the headers for the Reading/Math/Writing to just be
a single word. e.g. 'SAT Critical Reading Avg. Score' becomes 'Reading'
"""

data[0][2], data[0][3], data[0][4] = map(str, ["Reading", "Math", "Writing"])

"""
append a new column "Average Score" that calculates theb
mean of all 3 portions of the exam.
"""
def find_average(d):
    return round(sum([int(num) for num in d[-3:]])/3, 2)

for d in data[1:]:
    d.append(find_average(d))
    

print(data[:4])

def makeHTMLTable(listz):
    end = "<table>\n"
    for list in listz:
        end += "    <tr>\n"
        for item in list:
            end += f"        <td>{item}</td>\n"
        end += "    </tr>\n"
        
    end += "</table>"
    return end

whole_table = makeHTMLTable(data)

top = []
for d in data[1:]:
    if d[-1] >= 550:
        top.append(d)

top_table = makeHTMLTable(top)

import sys
sys.stdout = open("toptable.out", "w")

print(top_table)

sys.stdout = open("wholetable.out", "w")
print(whole_table)