import re
file = open("C:\\Users\pprab\Advent-of-Code-2023\Day 4\Puzzle.txt", "r")

def my_function(stri):
    val = 0
    L = stri.split(':')
    nums = L[1].split('|')
    totalnums = re.split("\s+", nums[1])
    winningnums = re.split("\s+", nums[0])
    totalnums.remove('')
    winningnums.remove('')
    totalnums.pop()
    winningnums.pop()
    for x in totalnums:
        for y in winningnums:
            if x == y:
                if val == 0:
                    val = 1
                else:
                    val *= 2 
    return val
    
    
count = 0
num = 1
for x in file:
   count += my_function(x)

print(count)
