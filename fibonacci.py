hi=int(input())
constant=1
a=0
b=1
for i in range(hi):
     print(constant,end=' ')
     constant=a+b
     a=b
     b=constant
