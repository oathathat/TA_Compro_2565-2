n = [int(i) for i in input(' *** Maximum occurence ***\nEnter numbers : ').split()]
temp =[]
count =0
max_count =0
for i in range(len(n)):
    for j in range(len(n)):
        if n[i] in temp or n[i] ==-1 or n[j] ==-1:
            break

        elif n[i] == n[j]:
            count = count+1       
    if count > max_count:
        max_count = count
        temp.clear()
        temp.append(n[i])
    elif count == max_count:
        temp.append(n[i])
    count = 0

print(f'{n}\nMax count = {max_count}\nMax occurence = {temp}\n===== End of program =====')
