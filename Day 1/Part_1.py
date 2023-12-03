file = open("C:\\Users\pprab\Advent-of-Code-2023\Day 1\Part_1_Puzzle.txt", "r")

maxval = -1
minval = -1
total = 0

for x in file:
    for i in x:
        if i.isdigit() :
            i = int(i)
            if maxval == -1 | minval == -1:
                minval = i
                maxval = i
            else:
                maxval = i
    print(int(str(minval) + str(maxval)))
    total += int(str(minval) + str(maxval))
    maxval = -1
    minval = -1
print(total)
