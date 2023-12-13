time1 = 53        
time2 = 91
time3 = 67
time4 = 68

distance1 = 250     
distance2 = 1330
distance3 = 1081   
distance4 = 1025

cal = 0
margin1 = 0
for i in range(1, time1, 1):
    cal = i * (time1 - i)
    if cal > distance1:
        margin1 += 1

cal = 0
margin2 = 0
for i in range(1, time2, 1):
    cal = i * (time2 - i)
    if cal > distance2:
        margin2 += 1

cal = 0
margin3 = 0
for i in range(1, time3, 1):
    cal = i * (time3 - i)
    if cal > distance3:
        margin3 += 1

cal = 0
margin4 = 0

for i in range(1, time4, 1):
    cal = i * (time4 - i)
    if cal > distance4:
        margin4 += 1

print(margin1*margin2*margin3*margin4)