class Employee:
    def setemployee(self,eid,ename,esal):
        self.EmpId = eid
        self.EmpName = ename
        self.EmpSal = esal
    def getemployee(self):
        print(f'Employee ID :{self.EmpId}\tEmployee Name :{self.EmpName}\tEmployee Salary : {self.EmpSal}')
 
print("===================Emp-1 Object===================") 
emp1 = Employee()   
emp1.setemployee(111,"sirisha",50000)
emp1.getemployee()    

print("===================Emp-1 Object===================") 
emp2 = Employee()   
emp2.setemployee(112,"Shivanandn",42000)
emp2.getemployee()    