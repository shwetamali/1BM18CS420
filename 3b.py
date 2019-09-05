import random
a="ABCDEFGHIJKLMNOPQRSRUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$^*&!"
length=int(input("Enter password length:"))
b="".join(random.sample(a,length))
print(b)
