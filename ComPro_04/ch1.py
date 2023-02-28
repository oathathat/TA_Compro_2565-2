n = int(input("Sum from 1 to : "))
if n<1:
    print('Input Error')
else:
    sum =0
    print('',end='')
    for  i in range(1,n+1):
        sum += i
    print(f'Sum from 1 to {n} is {sum}')