class Student:
    def getmount(self,totalamount):
        self.totalamount = totalamount
        print(f'Total Amount : {self.totalamount}')
    def spent(self,spent):
        self.spent = spent
        self.totalamount = self.totalamount - self.spent
        print(f'Spent Amount : {self.spent} Balance left : {self.totalamount}')
print("=====================Student-1 Object==============")
s1 = Student()
s1.getmount(50000)
s1.spent(5000)
print("=====================Student-2 Object==============")
s2 = Student()
s2.getmount(50000)
s2.spent(15000)
            
    