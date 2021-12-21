import math
import sys
import re

# Open file1 and read radius and coords for the center of the circle
with open(sys.argv[1], 'r') as file1: #sys.argv[1] - file1.txt
    for line in file1:
        line = line.rstrip() #delete \n after each row
        x = re.findall("[\d+]",line)
        if len(x) > 1:
            #print("coords for the center of the cirlce")
            xk = float(x[0])
            yk = float(x[1])
        else:
            #print("radius")
            r = float(x[0])
    #print(xk,yk,r)

# Open file2 and read coords which should be verified
with open(sys.argv[2], 'r') as file1: #sys.argv[1] - file1.txt
    lst = list()
    for line in file1:
        line = line.rstrip() #delete \n after each row
        x = re.findall("[\d+]",line)
        lst.append(x)
    #print(lst)

for i in lst:
    #print(i)
    x, y = float(i[0]) , float(i[1])

    total = (x - xk)**2 / r**2 + (y - yk)**2 / r**2
    #print(total)
    if total < 1:
        print("Точка лежит на окружности")
    elif total == 1:
        print("Точка внутри")
    else:
        print("Точка снаружи")
