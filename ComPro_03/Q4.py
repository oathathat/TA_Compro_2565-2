print(' *** Grade Classification ***')
score = float(input('Enter your score : '))
if 0 <= score <= 100:
    if score>=80:
        print("Grade A")
    elif score>=75:
        print('Grade B+')
    elif score>= 70:
        print('Grade B')
    elif score>= 65:
        print("Grade C+")
    elif score >= 60:
        print('Grade C')
    elif score >= 55:
        print('Grade D+')
    elif score >= 50:
        print('Grade D')
    else:
        print('Grade F')
else:
    print(f'{score} is invalid ! ! !')