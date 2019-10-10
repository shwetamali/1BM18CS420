class brackets:
    def valid_parentheses(str1):
        stack,pchar =list(),{"(":")","[":"]","{":"}"}
        for parentheses in str1:
            if parentheses in pchar:
                stack.append(parentheses)
            elif len(stack)==0 or pchar[stack.pop()]!=parentheses:
                print("Invalid string")
                return False
        print("valid string")       
        return len(stack)==0
str1=input("Enter string:")
print(brackets.valid_parentheses(str1))
            


*************************OUTPUT********************************
================= RESTART: /home/bmsce/week6_parentheses.py =================
Enter string:()[]{}
valid string
True
>>> 
================= RESTART: /home/bmsce/week6_parentheses.py =================
Enter string:([}
Invalid string
False
>>> 
================= RESTART: /home/bmsce/week6_parentheses.py =================
Enter string:{{{
valid string
False
>>> 
================= RESTART: /home/bmsce/week6_parentheses.py =================
Enter string:()
valid string
True
>>> 
