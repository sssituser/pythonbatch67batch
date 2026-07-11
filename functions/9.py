'''
Define a function which can swap two numbers ?
a =  5 b = 2
After swaping
a = 2 b = 5
# '''
# def swap(num1,num2):#num1 = 5 num2 = 2
#     print(f'Values Before Swaping num1 = {num1}  num2 = {num2}')
#     num2 = num1+num2  #num2 = 7
#     num1 = num2-num1 # num1 = 2
#     num2 = num2-num1 # num2 = 5
#     print(f'Values  After Swaping num1 = {num1}  num2 = {num2}')
# swap(5,2)

# def swap1(num1,num2): # num1 = 10  num2 = 20
#     print(f'Values Before Swaping num1 = {num1}   num2 = {num2}')
#     copy = num1 # copy =10
#     num1 = num2 # num1 = 20
#     num2 = copy # num2 = 10
#     print(f'Values After  Swaping num1 = {num1}   num2 = {num2}')
# swap1(10,20)

def swap2(num1,num2):
    print(f'Values Before Swaping num1 = {num1}   num2 = {num2}')
    num1,num2=num2,num1
    print(f'Values After  Swaping num1 = {num1}   num2 = {num2}')
    
swap2(4,5)