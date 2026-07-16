class Test:
    def getnums(self,a,b):
        self.a = a
        self.b = b
    def shownums(self):
        print(f'a = {self.a}\tb = {self.b}')
class Sample(Test):
    def sum(self):
        print(f'Sum of {self.a} and {self.b} is : {self.a+self.b}')
    def sub(self):
        print(f'Sub of {self.a} and {self.b} is : {self.a-self.b}')
class Simple(Sample):
        def mul(self):
            print(f'Mul of {self.a} and {self.b} is : {self.a*self.b}')
        def div(self):
            print(f'Div of {self.a} and {self.b} is : {self.a/self.b}')
s = Simple()
s.getnums(5,2)
s.shownums()
s.sum()
s.sub()
s.mul()
s.div()            
        
        