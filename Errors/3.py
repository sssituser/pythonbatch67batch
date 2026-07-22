while True:
    try:
      num1 = int(input('Enter number 1: '))
      num2 = int(input('Enter number 2: '))
      if num2==0:
        raise ZeroDivisionError("Iam In try block at if else stmt")
      print(f'{num1/num2}')
    
    except ZeroDivisionError as zx:
      print(f"num2 can't be zero : {zx}")
    except ValueError as vx:
      print("Enter only Integers")
    except Exception as ex:
     print(f'Error {ex}')
    finally:
      print("Hi Iam finally blok,Thanku visit Again")