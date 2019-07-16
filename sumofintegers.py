N,K= map(int,input().split())
arr = list(input().split())
arr = [int(x) for x in arr]
sum = 0
for i in range(0,K):
   sum = sum + arr[i]
print(sum)
