
word = input(' *** Word Triangle ***\nEnter Word: ')
n = len(word)

for i in range(n):
    for j in range(n):
        if j<=i:
            print(word[j],end='')
    print()