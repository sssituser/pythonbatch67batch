class Employee:  # class with static variables
   EmpId:int
   EmpName:str
   EmpSal:int
   
Employee.EmpId = 111
Employee.EmpName ="kiran"
Employee.EmpSal = 70000

print(Employee.EmpId,Employee.EmpName,Employee.EmpSal)