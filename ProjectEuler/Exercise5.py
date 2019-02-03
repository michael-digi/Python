true_count = 0
divisors = [11,12,13,14,15,16,17,18,19,20]
multiples = []

for num in range(2520,1000000000, 2520):
    if all(num % i == 0 for i in divisors):
        multiples.append(num)
print(min(multiples))
    
    