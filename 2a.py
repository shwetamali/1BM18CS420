num=[1,7,3,0,4,2,8,11,88]
print(num)
num.sort()
print(num)
a=int(input("Enter number to check"))
def find():
    if a in num:
        print(a,'present in list')
        return True
    else:
        print(a,'not present')
        return False
print(find())
    
