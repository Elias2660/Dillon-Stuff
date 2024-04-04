roster_data = """period1 Toby
period1 John
period1 Malia
period2 Yuxin
period2 Nabiha
period2 Jonathan
period2 Carlos
period3 Sasha
period3 Alma
period3 Annie
period3 Arthur
period3 Alexander"""

def split_line(s): return [student for student in s.split("\n")]

print(split_line(roster_data))


def student_count(s): return len(split_line(s))

print(split_line(roster_data))