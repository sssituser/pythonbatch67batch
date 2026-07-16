class Test:
    def getnums(self,a,b):
        self.a = a
        self.b = b;
    def shownums(self):
        print(f'a = {self.a}\tb = {self.b}')
class Sample(Test):
    def sum(self):
        print(f'Sum of a and b is : {self.a+self.b}')
    def sub(self):
        print(f'Sub of a and b is : {self.a-self.b}')
class Simple(Test):
    def mul(self):
        print(f'Mul of a and b is : {self.a*self.b}')
    def div(self):
        print(f'Quo of a and b is : {self.a/self.b}')
        
class Child(Test):
    def avg(self):
        print(f'Average of number is : {(self.a+self.b)/2}')
    def rem(self):
        print(f'remainer : {self.a%self.b}')

s = Sample()
s.getnums(5,2)
s.shownums()
s.sum()
s.sub()

s1 = Simple()
s1.getnums(4,2);
s1.shownums()
s1.mul()
s1.div()

c  = Child()
c.getnums(3,2)
c.shownums()
c.avg()
c.rem()   
    