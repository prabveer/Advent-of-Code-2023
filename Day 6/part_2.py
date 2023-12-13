time = 53916768
distance = 250133010811025


cal = 0
margin = 0
for i in range(1, time, 1):
    cal = i * (time - i)
    if cal > distance:
        margin += 1
        
print(margin)