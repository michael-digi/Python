total1 = 0
total2 = 0

for i in range(1,101,1):
    total1 += i
for j in range(1,101, 1):
    total2 += (j**2)

print(total1**2 - total2)
    
    