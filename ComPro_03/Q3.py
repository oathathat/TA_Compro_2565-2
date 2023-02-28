print(' *** Data type integer float string ***')
n = input("Enter a word : ")

try:
    n = int(n)   
    print(f'{n} * 2 = {n*2}')
except ValueError:
    try:
        n = float(n)
        print(f'{n:.3f} / 3 = {n/3:.3f}')
    except ValueError:
        print(f'{n} {n} {n}')

