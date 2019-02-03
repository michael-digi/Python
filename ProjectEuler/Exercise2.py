list1 = [1,2]
total = 2

for i in range(1,2000,1):
    if list1[i] >= 4000000:
        list1.pop(len(list1) - 1)
        break
    else:
        fib = list1[i] + list1[i-1]
        list1.append(fib)
        if fib % 2 == 0 and fib < 4000000:
            total += fib
    

print(list1)
print(total)