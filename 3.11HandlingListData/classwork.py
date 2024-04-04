def studentAverageDropLowest(data):
    data= data.split()
    list = [int(num) for num in data[2:]]
    return (sum(list) - min(list)) / (len(data) - 3)


def studentAverage(data):
    data = data.split()
    list = [int(num) for num in data[2:]]
    return (sum(list)/(len(data) - 2))

def compareAverages(data):
    data = data.split("\n")
    for student in data:
        names = student.split()
        print(" ".join([names[0], names[1], str(studentAverage(student)), str(studentAverageDropLowest(student))]))

data = """period1 Dave 10 20 30
          period1 Kay 100 20 90 88 95"""

#evaluates to "period1 Dave 20.0 25.0"
# and "period1 Kay 78.6 93.25"

compareAverages(data)