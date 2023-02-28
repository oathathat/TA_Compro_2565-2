print(' *** Transform second ***')
n = input('Enter seconds : ')
if not n.isdigit():
    print(f'! ! ! please enter in whole number --> {n}')
    print(" --- program end ---") 
    exit()
n = int(n)

week   = n//(60*60*24*7)
day    = n//(60*60*24)
hour   = n//(60*60) 
minute = n//60
second = n%60

print(f'{n} seconds ==> ',end='')
if week != 0:
    print(f'{week} weeks ',end='')    
if day !=0 and day%7 != 0:
    day = day%7
    print(f'{day} days ',end='')
if hour !=0 and hour%24 !=0 :
    hour = hour%24
    print(f'{hour} hours ',end='')
if minute !=0 and minute%60!=0:
    minute = minute%60
    print(f'{minute} minutes ',end='')
if second !=0 and second<=60:
    print(f'{second} seconds',end='')

print("\n --- program end ---") 