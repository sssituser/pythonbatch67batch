class Home:
    totalamount=10000
    
    def getamount(self,spent):
        self.spent = spent
        print(f"Total Amount : {Home.totalamount}")
        
        
    def spentamount(self,spent):
        self.spent = spent
        Home.totalamount = Home.totalamount-self.spent
        print(f'After spenting : {self.spent} Balance Amount : {self.totalamount}')
print("====================Bro1=================")
br1 = Home()
br1.getamount(0)
br1.spentamount(2000)

print("====================Bro2=================")
br2 = Home()
br2.getamount(0)
br2.spentamount(3000)