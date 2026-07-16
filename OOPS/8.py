class Product:
    
    def setproduct(self,pid,pname,price):
        self.pid = pid
        self.pname = pname
        self.price = price
        
    def getproduct(self):
        print(f'Product Id : {self.pid}\nProduct Name : {self.pname}\nPricie : {self.price}')  

print("=====================Object-1================")
p1 = Product()
p1.setproduct(334,"abc",600)
p1.getproduct()

print("=====================Object-2================")
p2 = Product()
p2.setproduct(335,"def",500)
p2.getproduct()