class Student:
    def __init__(self,sid,sname,smarks):
        self.sid = sid
        self.sname = sname
        self.smarks = smarks
        
    def getstudent(self):
        print(f'Student Id    : {self.sid}')
        print(f'Student Name  : {self.sname}')
        print(f'Student Marks : {self.smarks}')
        
print("========================s1-Object========================")
s1 = Student(111,"abc",500)
s1.getstudent()

print("========================s2-Object========================")
s2 = Student(112,"def",600)
s2.getstudent()

        