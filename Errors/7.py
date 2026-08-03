class Dept:
    def __init__(self,DeptId,DeptName,DeptLoc):
        self.DeptId = DeptId
        self.DeptName = DeptName
        self.DeptLoc = DeptLoc
    def getDept(self):
        print(f'DetpId : {self.DeptId}\nDeptName : {self.DeptName}\nDeptLoc : {self.DeptLoc}')
class Employee(Dept):
    def __init__(self,eid,ename,esal,DeptId,DeptName,DeptLoc):
        super().__init__(DeptId,DeptName,DeptLoc)
        self.eid = eid
        self.ename = ename
        self.esal = esal
    def getEmployee(self):
            print(f'Employee ID:{self.eid}\nEmployee Name :{self.ename}\nEmployee Salary : {self.esal}')
            super().getDept()
emp = Employee(111,"kiran",50000,123,"HR","Hyd")
emp.getEmployee()        
