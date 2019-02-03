high = 999
low = 0

palindrome_list = []

for i in range(999,99,-1):
    for j in range(999, 99,-1):
        product = i * j
        if (str(product) == str(product)[::-1]):
            palindrome_list.append(product)

print(max(palindrome_list))