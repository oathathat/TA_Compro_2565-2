n = input(' *** Display vowel in capital ***\nEnter something : ')
print(n)
for i in n:
    if i in "aeiou":
        print(f"{chr(ord(i)-(ord('a')-ord('A')))}",end='')
    else:
        print(i,end='')
print()
print('===== End Program =====')
