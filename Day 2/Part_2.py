file = open("C:\\Users\pprab\Advent-of-Code-2023\Day 2\Puzzle.txt", "r")

def my_function(stri):
    L = stri.split(':')
    num = L[0].split(' ')
    M = L[1].replace(';', '')
    M = M.replace(',', '')
    N = M.split(' ')
    greenval = 0
    blueval = 0
    redval = 0
    count = 1

    if str(N[len(N)-1]) == "green\n":
        greenval = int(N[len(N)-2])
    elif str(N[len(N)-1]) == "blue\n":
        blueval = int(N[len(N)-2])
    elif str(N[len(N)-1]) == "red\n":
        redval = int(N[len(N)-2])
    #print(N)
    while(count < len(N)):  
        if str(N[count+1]) == "green"  and int(N[count]) > greenval:
            greenval = int(N[count])
        elif str(N[count+1]) == "blue"  and int(N[count]) > blueval:
            blueval = int(N[count])
        elif str(N[count+1]) == "red"  and int(N[count]) > redval:
            redval = int(N[count])
        #print(N[count+1], N[count])
        count += 2
    print(int(num[1]), greenval, blueval, redval)
    return (greenval*blueval*redval)
    
count = 0
for x in file:
   count += my_function(x)
print(count)
