class Student:
    collegeName:str = "SSSIT" # class variables or static variables
    collegeAddress:str = "KPHB"  # 2-3 examples
    def setstudent(self,stuid,stuname,stumarks): #stuid,stuname,stumarks local variables
        self.stuid = stuid
        self.stuname = stuname
        self.stumarks = stumarks
        
    def getstudent(self):
        print(self.stuid) # instance variables or non static variables
        print(self.stuname)
        print(self.stumarks)
        
    def getcollegeInfo():
        print(Student.collegeName)
        print(Student.collegeAddress)
        
s1 = Student()
s1.setstudent(111,"abc",500)
s1.getstudent()
Student.getcollegeInfo()