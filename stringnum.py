
hi=str(input())
co=0
co1=0
for i in hi:
   if i.isnumeric():
       co+=1
   else:
        pass
for i in hi:
    if i.isalpha():
        co1+=1
    else:
        pass
if co>=1 and co1>=1 :
    print('Yes')
else:
    print('No')
     
        
