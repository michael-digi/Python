one_through_nine = {'0':'','1': 'One', '2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine'}

teens = {'10':'Ten','11':'Eleven','12':'Twelve','13':'Thirteen','14':'Fourteen','15':'Fifteen','16':'Sixteen','17':'Seventeen','18':'Eighteen', '19':'Nineteen'}

tens = {'2':'Twenty','3':'Thirty','4':'Forty','5':'Fifty','6':'Sixty','7':'Seventy','8':'Eighty','9':'Ninety'}

total = 0

temp = 0


for a in range(1,1001,1):
    a = str(a)
    if len(a) == 3:
        if a[1] == '0' and a[2] == '0':
            temp = one_through_nine.get(a[0]) + "hundred"
        elif a[1] == '0':
            temp = one_through_nine.get(a[0]) + "hundredand" + one_through_nine.get(a[2])
        elif a[1] == '1':
            temp =one_through_nine.get(a[0]) + 'hundredand' + teens.get(a[1]+a[2])
        else:
            temp =one_through_nine.get(a[0]) + 'hundredand' + tens.get(a[1])+ one_through_nine.get(a[2])
    if len(a) == 2:
        if a[0] == '1':
            temp = teens.get(a[0]+a[1])
        else:
            temp = tens.get(a[0]) + one_through_nine.get(a[1])
    if len(a) == 1:
        temp = one_through_nine.get(a[0])
    if len(a) == 4:
        temp = 'Onethousand'
    total += len(temp)
print(total)
