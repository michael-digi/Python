for i in range(20000):
    tri_num = (i*(i+1))/2
    divisor_count = 0
    for j in range(1,int(tri_num**.5 + 1),1):
        if int(tri_num) % j == 0:
            divisor_count += 2
    if divisor_count > 500:
        print(divisor_count)
        print(tri_num)
        break