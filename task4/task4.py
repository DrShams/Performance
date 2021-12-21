import math
import sys
from statistics import mean

nums = list()
with open(sys.argv[1], 'r') as file: #sys.argv[1] - file1.txt
    for line in file:
        line = line.rstrip()
        nums.append(int(line))

meanvalue = round(mean(nums))

value = 0
for x in nums:
    if x < meanvalue:
        value += meanvalue - x
    else:
        value += x - meanvalue
print(value)
