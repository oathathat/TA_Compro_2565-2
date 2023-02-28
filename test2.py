import re
s ='MCMXCIV'
sum =0
dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

if re.search("IV",s):
    s = re.sub("IV", "", s)
    sum +=4
elif re.search("IX",s):
    s = re.sub("IX","",s)
    sum +=9

if re.search("XL",s):
    s = re.sub("XL", "", s)
    sum +=40
elif re.search("XC",s):
    s = re.sub("XC","",s)
    sum +=90

if re.search("CD",s):
    s = re.sub("CD", "", s)
    sum +=400
elif re.search("CM",s):
    s = re.sub("CM","",s)
    sum +=900

for i in s:
    sum = sum + dic[i]

print(sum)