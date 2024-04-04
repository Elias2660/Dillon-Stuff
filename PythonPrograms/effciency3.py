import time
"""
2.9.Efficiency Lab Day 3
"""

start = time.time()
start_num = 0
for number in range(1, 1001):
    #add up every number from 1 to 1001
    start_num += number

print(start_num)
end = time.time()

print(f"Time Elapsed in Seconds: {end - start}")