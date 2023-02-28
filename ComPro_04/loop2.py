'''
harmonic sum
 ให้เขียนโปรแกรมคำนวณ harmonic sum โดยให้ loop
 https://en.wikipedia.org/wiki/Harmonic_series_(mathematics)

ตัวอย่าง input output
input เลขจำนวนเต็ม n>=0
 0
 2
 5
output ให้แสดงผล harmonic sum ทศนิยม 5 ตำแหน่ง
 0 = 0
 1 + 1/2 + 1/3 = 1.83333
 1 + 1/2 + 1/3 + 1/4 + 1/5 = 2.28333
'''
a = int(input())
sum = 0
if a>0:
    print(1,end="")
    for i in range(1,a+1):
        if i >1 :
            print(f" + 1/{i}",end="")
        sum += 1/i
    print(f" = {sum:.5f}")
else:
    print("0 = 0")