n = int(input(' *** Pyramid-XV ***\nEnter height : '))
ascii_count = ord('A')
first_time = True
reset_count = 0
for i in range(n):    
    for j in range(2*n-1):
        if  i+j < n-1:
             print('-',end='')
        elif i+j>=n-1 and j-i <= n-1:            
            if i%2==1: 
                if j < n-1:
                    print('.',end='')
                else:
                    print(f'{chr(ascii_count)}',end='')
                    ascii_count = ascii_count+1
                    if ascii_count> ord('Z'):
                        ascii_count = ascii_count-26
            else:
                if j > n-1:
                    print('.',end='')
                else:                    
                    if first_time:
                        ascii_count = ascii_count+i
                        if ascii_count > ord('Z'):
                            ascii_count = ascii_count-26
                        first_time = False
                    print(f'{chr(ascii_count)}',end='')      
                    if reset_count < i:                                 
                            ascii_count = ascii_count-1    
                            if ascii_count < ord('A'):
                                ascii_count = ascii_count+26
                    reset_count = reset_count +1 
        elif j-i > n-1:
            print('-',end='')
    print()
    reset_count = 0 
    if not first_time:
        ascii_count = ascii_count + i + 1
        first_time = True
    if ascii_count > ord('Z'):
            ascii_count = ascii_count-26
    if ascii_count < ord('A'):
            ascii_count = ascii_count+26
print('===== End of program =====')

