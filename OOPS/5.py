class Employee:
    TotalAmount=50000 # class or static variables
    def showbalance():
        print(f'Total Amount :{Employee.TotalAmount}')
        
    def spent(self,amount): # local variables
        self.amount = amount #instance variable
        Employee.TotalAmount = Employee.TotalAmount - self.amount
        print(f'Amount Spent : {self.amount} Balance Left : {Employee.TotalAmount}')

print(f"================Employee-1 Object=================")
emp1 = Employee()
Employee.showbalance() #50000
emp1.spent(10000) # 10000   Balleft 40000

print(f"================Employee-2 Object=================")
emp2 = Employee()
Employee.showbalance() ## 40000    n-50000
emp2.spent(5000) # spent 5000 Ballenf 35

print(f"================Employee-3 Object=================")
emp3 = Employee()
Employee.showbalance() ## 40000    n-50000




        