class exam:
    def __init__(self):
        self.name=""
        self.age=0
        self.marks=0
    def setdata(self):
        self.name=str(input("enter the name  "))
        self.age=int(input("eneter the age   "))
        self.marks=int(input("enetr the marks  "))
    def getdata(self):
        print("[",end=" ")
        print(self.name,end=" ")
        print(self.age,end=" ")
        print(self.marks,end=" ")
        print("]",end=" : ")
    def valid_marks(self):
        if self.marks>=0 and self.marks<=100:
            return True
        else:
            return False
    def valid_age(self):
        if self.age>20:
            return True
        else:
            return False
    def check_qual(self):
        if self.valid_age() and self.valid_marks():
            if self.marks>65:
                return True
            else:
                return False
        else:
            return False
    def result(self):
        if self.check_qual():
            self.getdata()
            print("student qualified")
        else:
            self.getdata()
            print("student not qualified")
           
#driver code
stu1=exam()
stu1.setdata()
stu1.result()
