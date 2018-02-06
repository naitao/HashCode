# v1.0
# Date: 2018.2.3.
# Progress: finished Data initializtion (2 hours coding)

import sys

def categorize(dict):
    maxValue = 0
    minValue = 1000
    maxValueKey = ''
    minValueKey = ''
    for key,value in dict.items():
        if int(value) > maxValue:
            maxValueKey = key
            maxValue = int(value)
        if int(value) <= minValue:
            minValueKey = key
            minValue = int(value)
    return [[minValueKey, minValue], [maxValueKey, maxValue]]

f = open("small.in")
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

# Creates a list containing R rows, each of C columns, all set to 0
Matrix = [['' for x in range(C)] for y in range(R)] 

row = 0
ingredient = {
              'M':0,
              'T':0
             }
# 1. Read lines from input.in and write 'M' or 'T' into array[][]
# 2. Construct matrix following the orders like below:
#	row 1: left -> right
#	row 2: left -> right
#	row 3: left -> right
#	...
# 3. Record the locations for each ingredient(M and T)
#    and save them into m_array_locations[] and t_array_locations[]

m_array_locations = []
t_array_locations = []
while line:
    line = f.readline().strip()
    column = 0
    for c in line:
        if c.upper() == 'M':
            m_array_locations.append([row, column])
        elif c.upper() == 'T':
            t_array_locations.append([row, column])

        Matrix[row][column] = c
        ingredient[c] += 1
        column += 1
    row += 1
#print(Matrix)
# The following code is to show what does matrix looks like, including
# the tags of ingredient
for col in Matrix:
    for c in col:
        print(c, end='')
    print('')


print("M: ", m_array_locations)
print("T: ", t_array_locations)

# Compare the different ingredients and categorize them with the appearance time for each
categorizedIngredient = categorize(ingredient)
minValueKey = categorizedIngredient[0][0]
minValue = categorizedIngredient[0][1]
maxValueKey = categorizedIngredient[1][0]
maxValue = categorizedIngredient[1][1]
print(minValueKey, minValue)
print(maxValueKey, maxValue)

if minValue % L != 0:
    sliceNumber = int(minValue/L) + 1
    reminder = minValue % L
else:
    sliceNumber = minValue/L
    reminder = 0

if minValueKey == 'M':
    base_array_locations = m_array_locations
    second_array_locations = t_array_locations
else:
    base_array_locations = t_array_locations
    second_array_locations = m_array_locations
    

# Cut slice starting from minValue ingredient, either 'M' or 'T'
# For the first cutting round (simulation), we will select the cell involving minValue
# ingredient one by one on the pizza, and we will try to add another cell (beside of it)
# which involving another ingredient to combine with it
selected_array_locations = []

# This array locaitons is saving for the 2 points' locations for each slice
# Such as [[0,0,2,1], [0, 2, 2, 2], [0, 3, 2, 4]]
slice_array_locations = []

def get_slice_locations(temp_slice_array_locations):
    """
        - Parameter: A group of cell locations
                     [[r1,c1],[r2,c2],[r3,c3],[r4,c4]...]
        - Return Value: the locations of left top cell and right bottom cell
                        [r1, c1, r2, c2]
    """
    left_r = temp_slice_array_locations[0][0]
    left_c = temp_slice_array_locations[0][1]
    right_r = temp_slice_array_locations[1][0]
    right_c = temp_slice_array_locations[1][1]
        
        
    if len(temp_slice_array_locations) == 2:
        if left_r < right_r:
            return left_r,left_c,right_r,right_c
        elif left_r == right_r:
            if left_c < right_c:
                return left_r,left_c,right_r,right_c
            else:
                return right_r,right_c, left_r, left_c
        else:
            return right_r,right_c, left_r, left_c
    print("Not implement this so far!")
    sys.exit()

def remove_location(list, index):
    list[index][0] = -1
    list[index][1] = -1
#second_select_array_locations = []
print("slice number (In theory): ", int(sliceNumber))
for i in range(int(sliceNumber)):
    # This array locations is saving for >= 2 cell locations
    temp_slice_array_locations = []
    #print("len: ", len(base_array_locations))
    for idx in range(0, len(base_array_locations)):
        #print(myindex)
        #print(base_array_locations)
        # fetch from other 4 cells around this cell, looking for another ingredient
        base_r = base_array_locations[idx][0]
        base_c = base_array_locations[idx][1]
        if base_r == -1 and base_c == -1:
            continue
        #print("base_r, base_c:", base_r, base_c)
        r1 = base_r
        c1 = base_c+1
        r2 = base_r
        c2 = base_c-1
        r3 = base_r+1
        c3 = base_c
        r4 = base_r-1
        c4 = base_c
            
        if [r1,c1] in second_array_locations:
            #print("hit cell on:", r1, c1)
            second_idx = second_array_locations.index([r1,c1])
            #selected_array_locations.append([r1,c1])
            temp_slice_array_locations.append([r1,c1])
            remove_location(second_array_locations, second_idx)
            flat = True
        elif [r2,c2] in second_array_locations:
            #print("hit cell on:", r2, c2)
            second_idx = second_array_locations.index([r2,c2])
            #selected_array_locations.append([r2,c2])
            temp_slice_array_locations.append([r2,c2])
            remove_location(second_array_locations, second_idx)
            flat = True
        elif [r3,c3] in second_array_locations:
            #print("hit cell on:", r3, c3)
            second_idx = second_array_locations.index([r3,c3])
            #selected_array_locations.append([r3,c3])
            temp_slice_array_locations.append([r3,c3])
            remove_location(second_array_locations, second_idx)
            flat = True
        elif [r4,c4] in second_array_locations:
            #print("hit cell on:", r4, c4)
            second_idx = second_array_locations.index([r4,c4])
            #selected_array_locations.append([r4,c4])
            temp_slice_array_locations.append([r4,c4])
            remove_location(second_array_locations, second_idx)
            flat = True
        else:
            continue
            
        if flat:
            #selected_array_locations.append(base_array_locations[idx])
            temp_slice_array_locations.append([base_array_locations[idx][0], base_array_locations[idx][1]])
            # remove base ingredient location from base array
            #print("before removing:", temp_slice_array_locations)
            remove_location(base_array_locations, idx)
            #print("after removing:", temp_slice_array_locations)
            break

    if len(temp_slice_array_locations) == 2:
       #print("temp slice array :", temp_slice_array_locations)
       slice_array_locations.append(get_slice_locations(temp_slice_array_locations))
    elif len(temp_slice_array_locations) > 2:
       print("There are more than 2 cells in a slice")
       print("temp slice array :", temp_slice_array_locations)
    else:
       #print("There are less than 2 cells in a slice")
       #print(temp_slice_array_locations)
       pass
print("Actual cutting slice number: ", len(slice_array_locations))
print(slice_array_locations)
f.close()
