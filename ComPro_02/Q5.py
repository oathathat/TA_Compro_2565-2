print(" *** Number Fun !!! ***")
a,b = input("Enter a b : ").split()
print("a=",a,"\ttype =",type(a))
print("b=",b,"\ttype =",type(b))
a,b = int(a),int(b)
print(f'a/b = {(a/b):.2f}')
print(f'b/a = {(b/a):.3f}')
print(f'a/b = {a//b} r {a%b}')
print(f'b/a = {b//a} r {b%a}')