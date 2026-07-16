class Employee:
    # def __init__(self):
    #     print("Hi Iam  constructor")
    
    def __init__(self,eid,ename,esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal
        print('hi Iam consturctor with paramter')
        
    def getemploye(self,eid,ename,esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal
        print(f'Given values are{self.eid}     {self.ename}      {self.esal}')


emp1 = Employee(111,"abc",60000)
emp1.getemploye(111,"abc",5000)
emp2 = Employee(112,"dddd",5555)
emp3 = Employee(114,"ffff",9999)
emp4 = Employee(115,"kkkk",8888)
    