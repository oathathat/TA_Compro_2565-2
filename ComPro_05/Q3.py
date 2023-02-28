def isPalin(word):
    if word == word[::-1]:
        return True
    else:
        return False
n = input(' *** Palindrome Checker ***\nInput 3 word to check: ').split()
for i in n:
    if len(i) <= 1:
        print('Input Error')
        exit()
for i in n:
    if isPalin(i):
        print(f'{i} is palindrome')
    else:
        print(f'{i} not palindrome')
