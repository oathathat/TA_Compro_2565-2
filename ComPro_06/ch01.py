sum =0 
for i in [int(i) for i in input(" *** Sum even / Subtract odd ***\nEnter numbers : ").split()]:
    if i%2==0:
        sum += i
    else:
        sum -= i
print(f'Sum is {sum}')