print(' *** Min Max Avg ***')
a = [float(i) for i in input("Enter 3 numbers : ").split()]
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j+1] , a[j] = a[j],a[j+1]

print(f'min, mid, max ==> {a[0]}, {a[1]}, {a[2]}')
sum =0
for i in a: 
    sum += i
print(f'Average ==> {sum/3:.2f}')