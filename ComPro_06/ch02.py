n = [int(i) for i in input(' *** Sequence Verification ***\nEnter Input : ').split()]

state =-1
for i in range(0,len(n)-1):    
    if  n[i]<=n[i+1] and state!=2:
        state =1
    elif n[i]>=n[i+1] and state!=1:
        state =2
    else:
        state =3
        break
    
if state==1:
    print('Ascending sequence !!!')
elif state==2:
    print('Descending sequence !!!')
elif state==3:
    print('Neither ascending or descending sequence !!!')

