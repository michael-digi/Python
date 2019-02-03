import time
start=time.time()
has2={}
def collatz(x):
    count = 1
    temp = x  
    while temp > 1:
        if temp % 2 == 0:
            temp = int(temp/2)
            if temp in has2:  # calculate temp and check if in cache
                count += has2[temp]
                break
            else:
                count += 1
        else:
            temp = 3*temp + 1
            if temp in has2:            
                count += has2[temp]
                break
            else:
                count += 1

    has2[x] = count
    return count

num=0
greatest=0
for i in range(500000,1000000,1):
    c=collatz(i)
    if num<c:
        num=c
        greatest=i
print('{0} has {1} elements'.format(greatest,num))