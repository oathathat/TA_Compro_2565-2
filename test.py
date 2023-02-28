print ("*** Alphabet Sequence (A-Z) ***")
char,step,length=input("Enter character step length : ").split()
#step=int(step)
l=int(length)
print(f"{char}",end="")
start=ord("A")
stop=ord("Z")
# print(stop,"this is")
temp = ord(char[0])
for x in range(l):
    step=int(step)
    char=chr(temp)
    if x != 0:
        print(f"={char}",end="")
    temp = temp+step        
    if temp > stop:
        temp = temp -26