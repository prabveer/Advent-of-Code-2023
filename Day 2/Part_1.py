file = open("C:\\Users\pprab\Advent-of-Code-2023\Day 2\Puzzle.txt", "r")

def my_function(stri):
    L = stri.split(':')
    num = L[0].split(' ')
    M = L[1].replace(';', '')
    M = M.replace(',', '')
    N = M.split(' ')
    count = 1

    if str(N[len(N)-1]) == "green\n" and int(N[len(N)-2]) > 13:
        return 0
    elif str(N[len(N)-1]) == "blue\n" and int(N[len(N)-2]) > 14:
        return 0
    elif str(N[len(N)-1]) == "red\n" and int(N[len(N)-2]) > 12:
        return 0
    
    while(count < len(N)):
        if str(N[count+1]) == "green"  and int(N[count]) > 13:
            return 0
        elif str(N[count+1]) == "blue"  and int(N[count]) > 14:
            return 0
        elif str(N[count+1]) == "red"  and int(N[count]) > 12:
            return 0
        count += 2
    print(int(num[1]))
    return int(num[1])
    
count = 0
for x in file:
   count += my_function(x)
print(count)
