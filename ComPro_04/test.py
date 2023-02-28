print ("*** Alphabet Sequence (A-Z) ***")
char,step,length=input("Enter character step length : ").split()
#step=int(step)
l=int(length)
start=ord("A")
stop=ord("Z")
l=l-1
step=int(step)
if 40<ord(char)<stop :
    if step>0:
        print(f"{char}",end="=")
        for x in range(l):
            if x<=24:
                next=ord(char)+step
                char=chr(next)
                print(f"{char}=",end="")
            elif x>24:  
                char="A"
                l=l-24
                for x in range(l):
                    new=start-step
                    char=chr(new)
                    print(f"{char}",end="=")
            #continue
    else : 
     print("Invalid input !!!",end="")
else : 
    print("Invalid input !!!",end="")
print("\n===== End of program =====")