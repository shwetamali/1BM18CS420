class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
s = Stack()
str1= input("Enter the string:")
for parentheses in str1:
    if parentheses == '(':
        s.push(1)
    elif parentheses== ')':
        if s.is_empty():
            is_balanced = False
            break
        s.pop()
    elif parentheses== '[':
        s.push(1)
    elif parentheses== ']':
        if s.is_empty():
            is_balanced = False
            break
        s.pop()
    elif parentheses== '{':
        s.push(1)
    elif parentheses == '}':
        if s.is_empty():
            is_balanced = False
            break
        s.pop()
else:
    if s.is_empty():
        is_balanced = True
    else:
        is_balanced = False
if is_balanced:
    print("Valid string")
else:
    print("Invalid string")



*******************************OUTPUT******************************************
=================== RESTART: /home/bmsce/parentheses_6.py ===================
Enter the string:()[]{}
Valid string
>>> 
=================== RESTART: /home/bmsce/parentheses_6.py ===================
Enter the string:{([
Invalid string
>>> 
=================== RESTART: /home/bmsce/parentheses_6.py ===================
Enter the string:{{{
Invalid string
>>> 
