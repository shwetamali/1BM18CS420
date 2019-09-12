class student:
    def __init__(self):
        self.sid=None
        self.sage=None
        self.smarks=None
    def setter(self):
        self.sid=input("Enter student id:")
        self.sage=int(input("Enter student age:"))
        self.smarks=int(input("Enter student marks:"))
    def validate_age(self):
        if(self.sage>20):
            return True
        else:
            return False
    def validate_marks(self):
        if(self.smarks > 0 and self.smarks<=100):
            return True
        else:
            return False
    def check_qualification(self):
        if(self.validate_age() and self.validate_marks()):
            if(self.smarks > 65):
                return True
            else:
                return False
        else:
            return False
    def getter(self):
        print("\n\n       STUDENT DETAILS:")
        print("Student id:",self.sid)
        print("Student age:",self.sage)
        print("Student marks:",self.smarks)
        if(s.check_qualification()):
            print("Eligible for university admission")
        else:
            print("Not eligible")
s=student()
s.setter()
s.getter()
    
