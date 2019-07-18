a,n=map(int,input().split())
for num in range(a,n+1):
  if(num==1):
    num+=1
  elif(num%2!=0):
    print(num,end=" ")
