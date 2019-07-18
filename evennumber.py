
a,n=map(int,input().split())

for num in range(a+1,n):
  if(num==1):
    num+=1
  elif(num%2==0):
    print(num,end=" ")
