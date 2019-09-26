class CallDetail:
    def __init__(self):
        self.dialer=None
        self.receiver=None
        self.duration=None
        self.type=None
    def set_details(self,a):
        self.dialer=a[0]
        self.receiver=a[1]
        self.duration=a[2]
        self.type=a[3]
        self.get_details()
    def get_details(self):
        print(self.dialer.ljust(20),end=" ")
        print(self.receiver.ljust(20),end=" ")
        print(self.duration.ljust(20),end=" ")
        print(self.type.ljust(20))
class Util:
    def __init__(self):
        self.list_of_call_objects= []

    def parse_customer(self,list_of_call_string):
        for i in range(len(list_of_call_string)):
            a=list_of_call_string[i].split(",")
            self.list_of_call_objects.append(CallDetail())
            self.list_of_call_objects[i].set_details(a)
call='9351692398,9925617843,20,STD'
call1='9927415902,9623490131,25,ISD'
call2='7352619205,6348108235,30,LOCAL'
list_of_call_string=[call,call1,call2]
print("\n\n\t\t\tCOMPANY CALL RECORDS\n ")
print("Dailer:".ljust(20),end=" ")
print("Receiver:".ljust(20),end=" ")
print("Duration:".ljust(20),end=" ")
print("Type:".ljust(20))
Util().parse_customer(list_of_call_string)
