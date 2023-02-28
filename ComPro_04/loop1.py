'''
อนุกรมเลขคณิต
 ให้เขียนโปรแกรมคำนวณอนุกรมเลขคณิตโดยใช้ loop
https://th.wikipedia.org/wiki/%E0%B8%A5%E0%B8%B3%E0%B8%94%E0%B8%B1%E0%B8%9A%E0%B9%80%E0%B8%A5%E0%B8%82%E0%B8%84%E0%B8%93%E0%B8%B4%E0%B8%95

ตัวอย่าง input output
input เลขจำนวนเต็ม 3 จำนวน 
 1 10 1
 2 20 2
 20 50 7
output 
 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
 2 + 4 + 6 + 8 + 10 + 12 + 14 + 16 + 18 + 20 = 110
 20 + 27 + 34 + 41 + 48 = 170
'''
a,b,c = [int(i) for i in input().split()]
sum = 0
print(a,end="")
for i in range(a,b+1,c):
    if i !=a:
        print(f" + {i}",end="")
    sum += i
print(f" = {sum}")
