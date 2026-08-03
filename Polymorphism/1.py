class Test:
    def show(self,name):
        self.name = name
        print(f'Hi {self.name}')
        
class Sample(Test):
    def show(self,name):
        self.name = name
        print(f'Welcome  {self.name}')
    def get(self):
        print("Hi this get method ")
s = Sample()
s.show("Ankitha")
s.get()
s = Test()
s.show("Ankith")