n = input('Enter query name and guest list: ').split()
inn = str(n[0])
lst = n[1:len(n)].copy()
print(' --- searching ---')
notIn = True
for i in lst:
    if inn.upper() == i.upper():
        print(f"Welcome, you're on the list! {inn[0].upper()}{inn[1:len(inn)].lower()}")
        notIn =False
        break
if notIn:
    print(f"Sorry, you're not on the list! {inn[0].upper()}{inn[1:len(inn)].lower()}")