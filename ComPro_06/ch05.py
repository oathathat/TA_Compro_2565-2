n = input(' *** Odd/Even at Left/Right ***\nEnter numbers : ').split()
odd= []
even =[]
for i in n :
    if int(i)%2==0:
        even.append(int(i))
    else:
        odd.append(int(i))
print(f'odd = {odd}\neven = {even}\nodd+even = {odd+even}\nnew = {odd[::-1]+even}')
