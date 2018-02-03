# v1.0
# Date: 2018.2.3.
# Progress: finished Data initializtion (2 hours coding)

import sys
f = open("input.txt")
line = f.readline().strip().split(' ')
values = [int(x) for x in line]
# the number of rows
R = values[0]
# the number of columns
C = values[1]
# the minimum number of each ingredient cells in a slice
L = values[2]
# the maximum total number of cells of a slice
H = values[3]

if R > 1000 or R < 1:
    print("R is out of the range 1 - 1000: {}".format(R))
    sys.exit()
if C > 1000 or C < 1:
    print("C is out of the range 1 - 1000: {}".format(C))
    sys.exit()
if L > 1000 or L < 1:
    print("L is out of the range 1 - 1000: {}".format(L))
    sys.exit()
if H > 1000 or H < 1:
    print("H is out of the range 1 - 1000: {}".format(H))
    sys.exit()
#print(values)

# Creates a list containing R rows, each of C columns, all set to 0
Matrix = [['' for x in range(C)] for y in range(R)] 

print(Matrix)
row = 0
ingredient = {
              'M':0,
              'T':0
             }
while line:
    line = f.readline().strip()
    column = 0
    for c in line:
        Matrix[row][column] = c
        ingredient[c] += 1
        column += 1
    row += 1
#print(Matrix)
for col in Matrix:
    for c in col:
        print(c, end='')
    print('')
print(ingredient)
f.close()
