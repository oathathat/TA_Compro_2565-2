n = int(input('How big is the triangle : '))
if n<0:
    print('Input Error')
else:
    for i in range(n):
        for j in range(n):
            if j<=i:
                print('*',end='')
        print()