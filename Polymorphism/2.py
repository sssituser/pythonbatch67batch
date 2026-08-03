class Employee:
    def setemployee(self,eid,ename,esal):
        self.__eid = eid
        self.__ename = ename
        self.__esal = esal
    def getemployee(self):
        print(f'{self.__eid} {self.__ename}  {self.__esal}  ')
emp1 = Employee()
emp1.setemployee(111,'Niharika',42000)
emp1.getemployee()
emp1.__eid = 123
emp1.__esal = 50000
emp1.getemployee()