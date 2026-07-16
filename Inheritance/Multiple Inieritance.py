class Dept:
    def getdept(self,did,dname):
        self.did = did
        self.dname = dname
    def showdept(self):
        print(f'Dept ID : {self.did}\tDeptName : {self.dname}')
class Education:
    def setstudentinfo(self,sid,sname,smarks):
        self.sid = sid
        self.sname = sname
        self.smarks = smarks
    def getstudentinfo(self):
        print(f'Student ID : {self.sid}\tStudent Name :{self.sname}\nMarks : {self.smarks}')
class Employee(Education,Dept):
    def setempinfo(self,eid,ename,esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal
    def getempinfo(self):
        print(f'Employee Id {self.eid}\nEmployee Name : {self.ename}\tEmployee Sal : {self.esal}')
emp = Employee()
emp.setstudentinfo(111,"abc",500)
emp.setempinfo(123,"abc",50000)
emp.getdept(1,"Developer")
emp.getstudentinfo()
emp.getempinfo()
emp.showdept()