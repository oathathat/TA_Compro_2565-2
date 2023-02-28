a,step,length = input(" *** Alphabet Sequence (A-Z) ***\nEnter character step length : ").split()
char_ascii = ord(a)
if  char_ascii<ord("A") or char_ascii>ord("Z") or int(step)<0:
    print('Invalid input !!!',end='')
else:   
    for i in range(int(length)):
        if i ==0:
            print(f'{chr(char_ascii)}',end='')
        else:
            print(f'={chr(char_ascii)}',end='')            
        char_ascii = char_ascii+int(step)        
        if char_ascii > 90:
            char_ascii = char_ascii - 26
print()
print("===== End of program =====")