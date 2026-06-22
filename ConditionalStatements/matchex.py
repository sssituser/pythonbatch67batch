num1 = int(input('Enter num1 : '))
num2 = int(input('Enter num2 : '))
choice = int(input('1.Add  2.Sub  3.Mul  4.Div  5.FloorDiv  6.Rem  7.Expo  Enter your choice: '))
match choice:
    case 1:
        print(f'{num1} + {num2} = {num1+num2}')
    case 2 :
        print(f'{num1} - {num2} = {num1-num2}')
    case 3:
        print(f'{num1} * {num2} = {num1*num2}')
    case 4:
        print(f'{num1} / {num2} = {num1/num2}')
    case 5:
        print(f'{num1} // {num2} = {num1//num2}')
    case 6:
        print(f'{num1} % {num2} = {num1%num2}')
    case 7:
        print(f'{num1} ** {num2} = {num1**num2}')
    case _:
        print("Invalid choice......")
        