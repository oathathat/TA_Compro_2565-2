a0,a1,repeat = [int(i) for i in input(' *** Fibonacci sequence ***\nEnter a0 a1 n : ').split()]

for i in range(repeat-1):
    if i==0:
        print(f'{a0}',end='')    
    print(f', {a1}',end='')
    a0 , a1 = a1, a1+a0
print('\n===== End of program =====')