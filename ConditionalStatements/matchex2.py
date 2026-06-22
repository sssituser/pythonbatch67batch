num1 = int(input('Enter num1 : '))
num2 = int(input('Enter num2 : '))
choice = input('Add   Sub   Mul  Div  FD  Mode  Exp\nEnter Your choice : ')
match choice:
    case "Add":
        print(f'Hero : {num1+num2}')
    case "Sub":
         print(f'zero : {num1-num2}')
    case "Mul":
        print(f'Sruthi : {num1*num2}')
    case "Div":
         print(f'Quo : {num1/num2}')
    case "FD":
        print(f'Fd : {num1//num2}')
    case "Mode":
        print(f'Rem : {num1%num2}')
    case "Exp":
        print(f'Power : {num1**num2}')
    case _:
        print("Fello Enter Right Choice...")
        
    
    
        