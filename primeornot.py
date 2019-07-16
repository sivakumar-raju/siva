n=int(input())
a=2
k=1
while(a<n):
       if(n%a==0):
              k=0
              break
       else:
              a=a+1
if k==0:
       print('no')
else:
       print('yes')
