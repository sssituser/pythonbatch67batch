from math import *
class Calcy:
    def getnums(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def sum(self):
        print(f'sum of two numbers :{self.num1+self.num2}')
    def sub(self):
        print(f'sub of two numbers :{self.num1-self.num2}')
    def mul(self):
        print(f'mul of two numbers :{self.num1*self.num2}')
    def quo(self):
        print(f'quo of two numbers :{self.num1//self.num2}')

class scicalcy(Calcy):
    def cos(self,value):
        self.value = value
        print(f'cos {self.value} is : {cos(self.value)}')
    def sin(self,value):
        self.value=value
        print(f'sin {self.value} is : {sin(self.value)}')
s = scicalcy()
s.cos(0)
s.sin(90)
s.getnums(5,2)
s.sum()
s.sub()
s.mul()
s.quo()
        