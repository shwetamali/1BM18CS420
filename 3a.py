a=int(input("Enter an integers:"))
LRange=list(range(1,a+1))
ans=[]
for num in LRange:
      if a%num==0:
          ans.append(num)
print("The divisor of that number:"+str(ans))
