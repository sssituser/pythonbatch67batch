class InvalidAgeException(Exception):
    def __init__(self,msg):
        self.msg=msg
        super().__init__(self.msg)
        print("Invalid Age exception")
        
while True:
    try:
        age = int(input('Enter Age : '))
        if age<0 or age>=120:
            raise InvalidAgeException("Hi Iam in if block")
    except InvalidAgeException as ex:
        print("hello",ex)
    except  Exception as ex:
        print(f"Error Occured : {ex}")
    
    

