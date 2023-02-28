'''
Fibonacci sequence
 ให้เขียนโปรแกรมคำนวณและแสดงผล Finbonacci sequence โดยใช้ loop
https://en.wikipedia.org/wiki/Fibonacci_number

ตัวอย่าง input output
input เลขจำนวนเต็ม n>=0 แทนลำดับ(เลขตัวแรกเป็นลำดับที่ 0)
 0
 1 
 5
output 
 0
 0 1
 0 1 1 2 3 5
'''
n = int(input())
a0 =0 
a1 =1
#print ลำดับ 0 
print(f'{a0} ',end='')
#print ลำดับ 1
if n>0:
    print(f'{a1} ',end='')
#print ลำดับ 2 ถึง n
for i in range(1,n):
    print(f'{a1+a0} ',end='')
    a0 , a1 = a1, a1+a0
    